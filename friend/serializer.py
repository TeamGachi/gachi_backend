from rest_framework.serializers import ModelSerializer
from .models import Friend,FriendshipRequest
from rest_framework import serializers
from authentication.models import User


class FriendSerializer(ModelSerializer):
    class Meta:
        model  = Friend
        fields = ["to_user"]

class FriendshipRequestSerializer(ModelSerializer):
    class Meta:
        model = FriendshipRequest
        fields = ["from_user","to_user"]

    def validate(self, data):
        if User.objects.get(email=data['from_user']) and User.objects.get(email=data['to_user']):
            return data
        return serializers.ValidationError(
            {"error":"unalbe to find users"}
        )

    def create(self, validated_data):
        from_user = self.context['request'].user
        to_user = User.objects.get(email=validated_data['request_to'])
        friendship = FriendshipRequest.objects.create(
            from_user = from_user,
            to_user = to_user
        )
        friendship.save() 
        return friendship

    
    


    
    

        