from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from trip.permissions import TripMembersOnly
from rest_framework import generics
from .serializer import TripImageSerializer
from .models import TripImage
from service import ImageClassifier
from django.shortcuts import get_object_or_404
from service import *


class ImageCreateView(generics.CreateAPIView):
    '''
        POST
        /api/image/
        TripImage생성 VIEW
    '''
    authentication_classes = [JWTAuthentication]
    serializer_class = TripImageSerializer

class ImageListView(generics.ListAPIView):
    '''
        GET
        /api/image/<int:pk>
        Trip에 속하는 모든 이미지 조회 요청 VIEW 
    '''
    authentication_classes = [JWTAuthentication]
    serializer_class = TripImageSerializer

    def get_queryset(self):
        queryset = TripImage.objects.filter(trip=self.kwargs['pk'])
        return queryset

    
class ImageClassificationView(generics.ListAPIView):
    ''''
        GET
        /api/myimage/<int:pk>/
        Trip pk에서 User가 속하는 사진만 조회 요청 
    '''
    authentication_classes = [JWTAuthentication]
    serializer_class = TripImageSerializer

    def get(self,request,pk):
        user = request.user
        trip = get_object_or_404(Trip,id=pk)
        image_classifier = ImageClassifier(trip,user)
        query_set = image_classifier.get_user_included_images()
        serializer = self.get_serializer(query_set,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)


