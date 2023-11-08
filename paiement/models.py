from django.db import models
from accounts.models import Client
from django.dispatch import receiver
from django.db.models.signals import post_save

class UserPayment(models.Model):
    app_user = models.ForeignKey(Client, on_delete=models.CASCADE)
    username = models.CharField(max_length=150,default='')  
    payment_bool = models.BooleanField(default=False)
    stripe_checkout_id = models.CharField(max_length=500,blank=True)

    def __str__(self):
         return f"{self.username}"
   



@receiver(post_save, sender=Client)
def create_user_payment(sender, instance, created, **kwargs):
    if created:
        UserPayment.objects.create(app_user=instance, username=instance.username)  # Ajoutez le champ username ici



def has_paid(user_id):
    try:
        user_payment = UserPayment.objects.get(app_user_id=user_id)
        return user_payment.payment_bool
    except UserPayment.DoesNotExist:
        return False

