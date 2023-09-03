from rest_framework.serializers import ModelSerializer
from .models import Friend,FriendshipRequest


class FriendSerializer(ModelSerializer):
    class Meta:
        model  = Friend
        fields = "__all__"

class FriendshipRequestSerializer(ModelSerializer):
    class Meta:
        model = FriendshipRequest
        fields = "__all__"

    
    

        