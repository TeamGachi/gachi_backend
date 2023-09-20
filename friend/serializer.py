from rest_framework.serializers import ModelSerializer
from .models import Friend,FriendshipRequest
from rest_framework import serializers
from authentication.models import User


class FriendSerializer(ModelSerializer):
    class Meta:
        model  = Friend
        fields = "__all__"

class FriendshipRequestSerializer(ModelSerializer):
    class Meta:
        model = FriendshipRequest
        fields = "__all__"

    def validate(self, data):
        if User.objects.get(email=data['sender']) and User.objects.get(email=data['receiver']):
            return data
        return serializers.ValidationError(
            {"error":"unalbe to find users"}
        )

    def create(self, validated_data):
        from_user = self.context['request'].user
        to_user = User.objects.get(email=validated_data['receiver'])
        friendship = FriendshipRequest.objects.create(
            sender = from_user,
            receiver = to_user
        )
        friendship.save() 
        return friendship

    
    


    
    

        