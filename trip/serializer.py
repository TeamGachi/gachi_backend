from rest_framework.serializers import ModelSerializer
from .models import Trip

class TripSerializer(ModelSerializer):
    class meta:
        model = Trip
        fields = "__all__"
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
    




