from rest_framework import serializers
from .models import TripImage
from trip.models import Trip


class TripImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripImage
        fields = "__all__"

    def validate(self, attrs):
        return super().validate(attrs)

class FaceImageSerializer(serializers.Serializer):
    face_image = serializers.ImageField(use_url=True)