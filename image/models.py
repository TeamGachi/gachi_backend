from django.db import models
from trip.models import Trip
from authentication.models import User


def image_upload_path(instance, filename):
    # Construct the upload path based on the user's email
    return f'images/{instance.person.email}/{filename}'

class TripImage(models.Model):
    person = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload_path)
    upload_date = models.DateField(null=False)

    def __str__(self):
        return self.upload_date