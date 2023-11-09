from rest_framework.serializers import ModelSerializer
from .models import Friend,FriendshipRequest
from rest_framework import serializers
from authentication.models import User
from rest_framework import status
from django.shortcuts import get_object_or_404

class FriendSerializer(ModelSerializer):
    class Meta:
        model  = Friend
        fields = "__all__"

class FriendshipRequestSerializer(ModelSerializer):
    class Meta:
        model = FriendshipRequest
        fields = "__all__"

    def validate(self, data): # 존재하는 유저 및 이미 친구인지 검사 
        try:
            sender = User.objects.get(email=data['sender'])
            receiver = User.objects.get(email=data['receiver'])
        except User.DoesNotExist:
            raise serializers.ValidationError(
                {"message":"해당하는 sender나 receiver가 존재하지 않습니다."},
                code=status.HTTP_404_NOT_FOUND
            )          

        query = FriendshipRequest.objects.filter(sender=sender,receiver=receiver)
        if query.exists():
            raise serializers.ValidationError(
                {"message" : "이미 친구요청이 존재합니다."},
                code=status.HTTP_409_CONFLICT
            )

        query = Friend.objects.filter(user=data['sender'],
                                      friend=data['receiver'])
        if query.exists():
            raise serializers.ValidationError(
                {"message" : "이미 친구입니다."},
                code=status.HTTP_409_CONFLICT
            )
        
        return data
    

    def create(self, validated_data):
        sender = self.context['request'].user
        receiver = User.objects.get(email=validated_data['receiver'])
        friendship = FriendshipRequest.objects.create(
            sender = sender,
            receiver = receiver
        )
        friendship.save() 
        return friendship

    
    


    
    

        