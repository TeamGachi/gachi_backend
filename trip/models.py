from django.db import models
from authentication.models import User
from django.utils.timezone import localdate

# Trip 
class Trip(models.Model):
    place = models.CharField(max_length=50)
    departing_date = models.DateField(default=localdate)
    arriving_date = models.DateField(default=localdate)
    users = models.ManyToManyField(User,blank=True)
    

