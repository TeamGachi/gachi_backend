from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from trip.permissions import TripMembersOnly
from rest_framework import generics
from .serializer import ImageCreateSerializer,ImageListSerialzier
from .models import TripImage
from django.conf import settings
import os 

# 이미지 생성 API view 
class ImageCreateView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    # permission_classes = [TripMembersOnly]
    serializer_class = ImageCreateSerializer

# Trip에 속하는 이미지 조회 View 
class ImageListView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    # permission_classes = [TripMembersOnly]
    serializer_class = ImageListSerialzier

    def get_queryset(self):
        queryset = TripImage.objects.filter(person=self.request.user)
        return queryset
    
# Trip에 속하는 이미지 얼굴별 분류 요청 View 
class ImageClassificationView(APIView):
    pass 

# 분류된 폴더에 대한 이름변경 요청 View 
class ImageClassificationChangeView(APIView):
    pass 


