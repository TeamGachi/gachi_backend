from django.db import models
from authentication.models import User
from django.utils.timezone import localdate


# Trip
class Trip(models.Model):
    place = models.CharField(max_length=50)
    departing_date = models.DateField(default=localdate)
    arriving_date = models.DateField(default=localdate)
    users = models.ManyToManyField(User, blank=True)


# TripInvite
class TripInvite(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="sent_trip_invites"
    )
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="received_trip_invites"
    )
