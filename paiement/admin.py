from django.contrib import admin
from paiement.models import UserPayment

@admin.register(UserPayment)
class PaymentAdmin(admin.ModelAdmin):

    list_display = ("app_user","username","payment_bool",)
