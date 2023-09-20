from django.db import models
from trip.models import Trip

class TripImage(models.Model):
    trip = models.ForeignKey(Trip,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    upload_date = models.DateField()

    def __str__(self):
        return self.trip