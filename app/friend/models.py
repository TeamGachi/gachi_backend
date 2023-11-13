from django.db import models
from authentication.models import User


class FriendshipRequest(models.Model):
    """친구요청"""

    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="friendship_requests_sent"
    )
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="friendship_requests_received"
    )


class Friend(models.Model):
    """친구"""

    user = models.ForeignKey(User, models.CASCADE, related_name="friends")
    friend = models.ForeignKey(
        User, models.CASCADE, related_name="_unused_friend_relation"
    )
