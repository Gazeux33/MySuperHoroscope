from django.core.management.base import BaseCommand
from Signa.gen_horo import database # Remplacez 'yourapp.scripts' par le chemin vers votre fonction 'database'.

class Command(BaseCommand):
    help = 'Updates the horoscopes'

    def handle(self, *args, **kwargs):
        database()