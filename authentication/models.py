from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    gender = models.CharField(max_length=20)
    birth = models.DateField(default="1999-08-22")



    
    
