from django.urls import path
from paiement.views import*


urlpatterns = [
    path('product_page',product_page,name= 'product_page'),
    path('product_suc',payment_successful,name= 'product_suc'),
    path('product_fail',payment_cancelled,name= 'product_fail'),
    path('stripe_webhook',stripe_webhook,name= 'stripe_webhook'),



]