from django.urls import path
from .views import*

urlpatterns = [

    path('horoscope/<str:sign>', show_horoscope, name='horoscope'),
]