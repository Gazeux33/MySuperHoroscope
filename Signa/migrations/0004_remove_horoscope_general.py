# Generated by Django 3.1.6 on 2023-05-24 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Signa', '0003_horoscope_general'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='horoscope',
            name='general',
        ),
    ]
