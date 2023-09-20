from rest_framework.serializers import ModelSerializer
from .models import Trip

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
    

    



