from django.db import models

class Horoscope(models.Model):
    date = models.DateField()
    sign = models.CharField(max_length=20)
    travail = models.TextField(default="pas d'horoscopes pour le moment")
    argent = models.TextField(default="pas d'horoscopes pour le moment")
    sante = models.TextField(default="pas d'horoscopes pour le moment")
    amour = models.TextField(default="pas d'horoscopes pour le moment")
    nombre = models.TextField(default="pas d'horoscopes pour le moment")
    famille  = models.TextField(default="pas d'horoscopes pour le moment")  

    class Meta:
        unique_together = ('date', 'sign')

    def __str__(self):
        return f"{self.sign} - {self.date}"

