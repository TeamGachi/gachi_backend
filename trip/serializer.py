from rest_framework.serializers import ModelSerializer
from .models import *
from friend.models import Friend
from rest_framework import serializers

class TripSerializer(ModelSerializer):
    class Meta:
        model = Trip
        fields = "__all__"
    
    def validate(self, data):
        return data
    
    def create(self,validated_data):
        trip = Trip.objects.create(
            place = validated_data['place'],
            departing_date = validated_data['departing_date'],
            arriving_date = validated_data['arriving_date']
        )
        return trip
    

class TripInviteSerializer(ModelSerializer):
    class Meta:
        model = TripInvite
        fields = "__all__"

    def validate(self,data):
        try: 
            friendship_one = Friend.objects.get(user=data['sender'],friend=data['receiver'])
            friendship_two = Friend.objects.get(user=data['receiver'],friend=data['sender'])
        except friendship_one.DoesNotExist or friendship_two.DoesNotExist:
            raise serializers.ValidationError(
                {"error" : "친구 관계가 아닌 사람에게는 여행 초대를 보낼 수 없습니다."}
            )
        return data



