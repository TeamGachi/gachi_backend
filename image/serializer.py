from rest_framework import serializers
from .models import TripImage
from trip.models import Trip

class ImageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripImage
        fields = "__all__"

    

class ImageListSerialzier(serializers.ModelSerializer):
    pass 