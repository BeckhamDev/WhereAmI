import geocoder

from django.db import models

# Create your models here.

access_token = 'pk.eyJ1IjoiYmVja2hhbS1kZXYiLCJhIjoiY2xrdjl2aTY1MHFzbzNmcnVvMjc3ajd3YiJ9.vqsAU7gD3HR45vxmbtzK5w'

class Address(models.Model):
    address = models.TextField()
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.address, key = access_token)
        g = g.latlng
        self.lat = g[0]
        self.long = g[1]
        return super(Address, self).save(*args, **kwargs)