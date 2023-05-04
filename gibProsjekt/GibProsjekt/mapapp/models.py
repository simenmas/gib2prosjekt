from django.db import models
from django.contrib.auth.models import User
import geocoder

# Create your models here.

class Point(models.Model):
    name = models.CharField(max_length=50)

    lat = models.FloatField()
    lon = models.FloatField()
    description = models.TextField()

    category = models.CharField(max_length=50)
    visibility = models.CharField(max_length=50, default = "Privat")

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def adress(self):

        g = geocoder.osm([self.lat,self.lon], method='reverse')
        if g.street != None and g.city != None:
            adress_string = f"{g.street}, {g.city}"
            if g.housenumber != None:
                adress_string = f"{g.street} {g.housenumber}, {g.city}"

        return adress_string
    
    class Meta:
        unique_together=['name','lat','lon','user']
