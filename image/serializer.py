from rest_framework import serializers
from .models import TripImage

class ImageSerializer(serializers.ModelSerializer):
    # image = serializers.ImageField(use_url = True)
    class Meta:
        model = TripImage
        fields = "__all__"

