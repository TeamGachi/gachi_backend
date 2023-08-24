from django.db import models

class FriendshipRequest(models.Model):
    """ Model to represent friendship requests """
    from_user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='friendship_requests_sent')
    to_user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='friendship_requests_received')

class Friend(models.Model):
    """ Model to represent Friendships """
    to_user = models.ForeignKey(AUTH_USER_MODEL, models.CASCADE, related_name='friends')
    from_user = models.ForeignKey(AUTH_USER_MODEL, models.CASCADE, related_name='_unused_friend_relation')