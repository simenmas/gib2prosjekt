from django.db import models

# Create your models here.
class Punkt(models.Model):
    tittel = models.CharField(max_length=30)
    lat = models.DecimalField(decimal_places=3, max_digits=5)
    lon = models.DecimalField(decimal_places=3, max_digits=5)
    typ = models.CharField(max_length=20)
    synlighet = models.CharField(max_length=30)
    beskrivelse = models.CharField(max_length=200)