from django.contrib import admin
from Signa.models import Horoscope

@admin.register(Horoscope)
class HoroscopeAdmin(admin.ModelAdmin):
    pass
