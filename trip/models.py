from django.db import models
from authentication.models import User
from django.utils.timezone import localdate

# Trip 
class Trip(models.Model):
    place = models.CharField(max_length=50)
    departing_date = models.DateField(default=localdate)
    arriving_date = models.DateField(default=localdate)
    
# Trip list 
class TripList(models.Model):
    member = models.ForeignKey(User,on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip,on_delete=models.CASCADE)