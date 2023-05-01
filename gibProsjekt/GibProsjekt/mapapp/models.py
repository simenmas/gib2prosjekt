from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Point(models.Model):


    name = models.CharField(max_length=50)
    lat = models.FloatField()
    lon = models.FloatField()
    description = models.TextField()

    category = models.CharField(max_length=50)
    visibility = models.CharField(max_length=50, default = "Privat")

    user = models.ForeignKey(User, on_delete=models.CASCADE)
