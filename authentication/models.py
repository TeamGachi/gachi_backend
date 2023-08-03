from django.db import models
from django.contrib.auth.models import User,AbstractUser
# Create your models here.

class User(AbstractUser):
    
    email = models.CharField(null=False,max_length=50)
    gender = models.CharField(null=False,max_length=20)
    nickname = models.CharField(null=False,max_length=20)
    birth = models.DateField(null=False)
    password = models.CharField(null=False,max_length=20)

    
    
