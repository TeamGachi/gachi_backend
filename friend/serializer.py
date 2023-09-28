from rest_framework.serializers import ModelSerializer
from .models import Friend,FriendshipRequest
from rest_framework import serializers
from authentication.models import User
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
        if User.objects.get(email=data['sender']) and User.objects.get(email=data['receiver']):
            query = Friend.objects.filter(user=data['sender'],friend=data['receiver'])
            if query.exists():
                raise serializers.ValidationError(
                    {"error" : "이미 친구입니다."}
                )
            return data
        raise serializers.ValidationError(
            {"error":"해당하는 sender나 receiver가 존재하지 않습니다."}
        )

    def create(self, validated_data):
        sender = self.context['request'].user
        receiver = User.objects.get(email=validated_data['receiver'])

        # 이미 친구 관계일 경우 exception 
        if Friend.objects.filter(user = sender,friend=receiver).exists():
            raise serializers.ValidationError({'name': '이미 친구관계입니다.'})
        # at least one object satisfying query exists
        else:
            # no object satisfying query exists
            friendship = FriendshipRequest.objects.create(
                sender = sender,
                receiver = receiver
            )
            friendship.save() 
            return friendship

    
    


    
    

        