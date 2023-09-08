from rest_framework import serializers
from models import Trip

class TripSerializer(serializers.ModelSerializer):
    # 일치하는 jwt를 가지고 있는지 검사 
    def validate(self, data):
        pass
    
    def create(self,validated_data):
        trip = Trip.objects.create(
            place = validated_data['place'],
            department = validated_data['department'],
            arrival = validated_data['arriaval']
        )
        return trip
    



