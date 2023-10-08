from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from .serializer import TripImageSerializer
from .models import TripImage
from django.shortcuts import get_object_or_404
from permissions import TripMembersOnly
from .task import * 
from celery.result import AsyncResult

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
        if email is None:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset,many=True)
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        else: 
            queryset = self.get_queryset()
            user = get_object_or_404(User,email=email)
            result = get_user_included_images(user,queryset)
            serializer = self.get_serializer(result,many=True)
            return Response(data=serializer.data,status=status.HTTP_200_OK)




    
