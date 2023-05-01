from django.db import models

# Create your models here.

class Point(models.Model):


    name = models.CharField(max_length=50)
    lat = models.FloatField()
    lon = models.FloatField()
    desc = models.TextField()

    category = models.CharField(max_length=50)
