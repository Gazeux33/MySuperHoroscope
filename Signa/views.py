from django.shortcuts import render
from .models import*
import datetime
from datetime import datetime, timedelta,date
from django.contrib.auth.decorators import login_required
from paiement.models import has_paid
from paiement.models import*
import random


@login_required(login_url='login')
def show_horoscope(request, sign):
    template_name = f'{sign}.html'
    date_today = date.today()
    temps_restant = time_remaining()
    temps_restant_dt = datetime(1, 1, 1) + temps_restant
    try:
       horoscope = Horoscope.objects.get(date=date_today, sign=sign)
    except:
        horoscope = Horoscope.objects.get(sign = "neure")
    
    context = {
        'sign': sign,
        'horoscope': horoscope,
        'date': date_today,
        'temps_restant': temps_restant_dt,
        'has_paid':has_paid(request.user.id),
    }
    return render(request, template_name, context)

def time_remaining():
    now = datetime.now()
    tomorrow = now.date() + timedelta(days=1)
    midnight = datetime.combine(tomorrow, datetime.min.time())
    remaining_time = midnight - now
    return remaining_time

