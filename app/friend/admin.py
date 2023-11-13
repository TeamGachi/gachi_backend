from django.contrib import admin
from .models import Friend, FriendshipRequest

# Register your models here.
admin.site.register(FriendshipRequest)
admin.site.register(Friend)
