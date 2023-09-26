from django.db import models
from trip.models import Trip
from authentication.models import User
import datetime

def image_upload_path(instance, filename):
    # Construct the upload path based on the user's email
    return f'images/{instance.trip.id}/{filename}'

class TripImage(models.Model):
    trip = models.ForeignKey(Trip,on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload_path)
    upload_date = models.DateField(null=False,default=datetime.date.today)

    def __str__(self):
        return str(self.upload_date)