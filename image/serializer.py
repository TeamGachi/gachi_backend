from rest_framework import serializers
from .models import TripImage
from trip.models import Trip

class TripImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripImage
        fields = "__all__"


    
