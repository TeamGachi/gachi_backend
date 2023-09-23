from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from trip.permissions import TripMembersOnly
from rest_framework import generics
from .serializer import ImageCreateSerializer,ImageListSerialzier
from .models import TripImage

# 이미지 생성 API view 
class ImageCreateView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    # permission_classes = [TripMembersOnly]
    serializer_class = ImageCreateSerializer

# Trip에 속하는 이미지 조회 View 
class ImageListView(generics.ListAPIView):
    '''
        GET
        Trip pk에 속하는 모든 이미지 조회 요청 VIEW 
    '''
    authentication_classes = [JWTAuthentication]
    # permission_classes = [TripMembersOnly]
    serializer_class = ImageListSerialzier

    def get_queryset(self):
        queryset = TripImage.objects.filter(person=self.request.user)
        return queryset
    
# Trip에 속하는 이미지중에서 User가 속하는 image 조회 요청 
class ImageClassificationView(APIView):
    ''''
        GET 
        사진에서 User가 속하는 사진만 조회 요청 
    '''
    pass 


