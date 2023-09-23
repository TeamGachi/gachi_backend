from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from trip.permissions import TripMembersOnly
from rest_framework import generics
from .serializer import ImageSerializer
from .models import TripImage
from django.conf import settings
import os 

# 이미지 API
class ImageView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    # permission_classes = [TripMembersOnly]
    serializer_class = ImageSerializer

    def get_queryset(self):
        queryset = TripImage.objects.filter(person=self.request.user)
        return queryset
    


""" # 이미지 다운로드 API 
class ImageDownloadView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [TripMembersOnly]
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs) """

