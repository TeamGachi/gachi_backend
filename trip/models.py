from django.db import models
from authentication.models import User
from django.utils.timezone import localdate

# trip 세션
class Trip(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    place = models.CharField(max_length=50)
    departing_date = models.DateField(default=localdate)
    arriving_date = models.DateField(default=localdate)
    thumbnail = models.TextField(null=True)

