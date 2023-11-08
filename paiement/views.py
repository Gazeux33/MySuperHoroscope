from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from paiement.models import UserPayment
import stripe
from accounts.models import Client
import time
from Asrto.settings import STRIPE_WEBHOOK_SECRET,PRIVATE
import logging

logger = logging.getLogger(__name__)


@login_required(login_url='login')
def product_page(request):
    stripe.api_key = PRIVATE
    if request.method == 'POST':
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'eur',
                        'unit_amount': 500,
                        'product_data': {
                            'name': 'Astro',
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            customer_creation='always',
            success_url= 'https://mysuperhoroscope.fr/paiement/product_suc?session_id={CHECKOUT_SESSION_ID}',
            cancel_url= 'https://mysuperhoroscope.fr/paiement/product_fail',
            metadata={'user_id': request.user.id},  # Ajoutez cette ligne
        )
        return redirect(checkout_session.url, code=303)
    return render(request, 'product_page.html')



def payment_successful(request):
    stripe.api_key = PRIVATE
    checkout_session_id = request.GET.get('session_id', None)
    session = stripe.checkout.Session.retrieve(checkout_session_id)
    customer = stripe.Customer.retrieve(session.customer)
    user_id = session.get('metadata', {}).get('user_id', None)

    if user_id:
        user_id = int(user_id)  # Convertissez la chaîne en entier
        # Récupère ou crée un objet UserPayment pour l'utilisateur
        user_payment, created = UserPayment.objects.get_or_create(app_user_id=user_id)

        user_payment.stripe_checkout_id = checkout_session_id
        user_payment.save()

   

        return render(request, 'payment_suc.html', {'customer': customer})
    else:
        # Gérer le cas où user_id n'est pas disponible
        return HttpResponse(status=400)



def payment_cancelled(request):
	stripe.api_key = PRIVATE
	return render(request, 'payment_fail.html')




logger = logging.getLogger(__name__)

@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = PRIVATE
    time.sleep(10)
    payload = request.body
    signature_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None
    try:
        event = stripe.Webhook.construct_event(
            payload, signature_header, STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        session_id = session.get('id', None)
        user_id = session.get('metadata', {}).get('user_id', None)  # Ajoutez cette ligne
        if user_id:
            user_id = int(user_id)  # Convertissez la chaîne en entier
            user_payment = UserPayment.objects.get(app_user_id=user_id)  # Modifiez cette ligne
            user_payment.payment_bool = True
            user_payment.save()
    return HttpResponse(status=200)
