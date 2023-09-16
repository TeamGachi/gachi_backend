from django.db import models
from authentication.models import User

class FriendshipRequest(models.Model):
    """ 친구요청 """
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friendship_requests_sent')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friendship_requests_received')

class Friend(models.Model):
    """ 친구 """
    to_user = models.ForeignKey(User, models.CASCADE, related_name='friends')
    from_user = models.ForeignKey(User, models.CASCADE, related_name='_unused_friend_relation')