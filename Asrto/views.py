from datetime import datetime
from django.shortcuts import render
#from django.http import HttpResponse
from paiement.models import UserPayment,has_paid
from django.core.mail import send_mail
def index(request):
    date = datetime.today()
    
    return render(request, 'index.html',context={"prenom": "Thesosrus","date": date,"has_paid":has_paid(request.user.id),})

def info(request):
        return render(request, 'info.html')


