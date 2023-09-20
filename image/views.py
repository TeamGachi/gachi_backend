from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from trip.permissions import TripMembersOnly
from rest_framework import generics
import os 

# 이미지 업로드 API
class ImageView(generics.ListCreateAPIView):
    '''authentication_classes = [JWTAuthentication]
    permission_classes = [TripMembersOnly]'''

    def get_queryset(self):
        return super().get_queryset()

    def create(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        if not os.path.isdir(f"../media/{pk}"):
            os.mkdir(f"../media/{pk}")
        
        return super().create(request, *args, **kwargs)
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


# 이미지 다운로드 API 
class ImageDownloadView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [TripMembersOnly]
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

