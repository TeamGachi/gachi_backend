from rest_framework.serializers import ModelSerializer
from .models import Trip

class TripSerializer(ModelSerializer):
    class Meta:
        model = Trip
        fields = "__all__"
    
    def validate(self, data):
        pass
    
    def create(self,validated_data):
        trip = Trip.objects.create(
            place = validated_data['place'],
            department = validated_data['department'],
            arrival = validated_data['arriaval']
        )
        return trip
    

    



