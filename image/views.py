from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from .serializer import TripImageSerializer
from .models import TripImage
from service import ImageClassifier
from django.shortcuts import get_object_or_404
from service import *
from permissions import TripMembersOnly

class ImageCreateView(generics.CreateAPIView):
    '''
        POST
        /api/image/
        TripImage생성 VIEW
    '''
    authentication_classes = [JWTAuthentication]
    permission_classes = [TripMembersOnly] 
    serializer_class = TripImageSerializer

class ImageListView(generics.ListAPIView):
    '''
        GET
        /api/image/<int:pk>
        Trip에 속하는 이미지 조회 요청 VIEW 
    '''
    authentication_classes = [JWTAuthentication]
    permission_classes = [TripMembersOnly] 
    serializer_class = TripImageSerializer

    def get_queryset(self):
        queryset = TripImage.objects.filter(trip=self.kwargs['pk'])
        return queryset
    
    def list(self, request, *args, **kwargs):
        email = self.request.GET.get("email",None)
        if email is None: # PK에 속하는 모든 여행 이미지 리턴 
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset,many=True)
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        else: # user가 포함된 이미지 리턴 
            trip = get_object_or_404(Trip,id=kwargs['pk'])
            user = get_object_or_404(User,email=email)
            image_classifier = ImageClassifier(trip=trip,user=user)
            user_included_queryset = image_classifier.get_user_included_images() # trip 의 이미지에서 user가 포함된 이미지 queryset만 반환 
            serializer = self.get_serializer(user_included_queryset,many=True)
            return Response(data=serializer.data,status=status.HTTP_200_OK)

    
