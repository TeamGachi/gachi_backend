from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from trip.permissions import TripMembersOnly
from rest_framework import generics
from .serializer import TripImageSerializer
from .models import TripImage
from service import ImageClassifier


class ImageCreateView(generics.CreateAPIView):
    '''
        POST
        TripImage생성 VIEW
    '''
    authentication_classes = [JWTAuthentication]
    # permission_classes = [TripMembersOnly]
    serializer_class = TripImageSerializer

class ImageListView(generics.ListAPIView):
    '''
        GET
        Trip에 속하는 모든 이미지 조회 요청 VIEW 
    '''
    authentication_classes = [JWTAuthentication]
    # permission_classes = [TripMembersOnly]
    serializer_class = TripImageSerializer

    def get_queryset(self):
        queryset = TripImage.objects.filter(person=self.request.user)
        return queryset
    
class ImageClassificationView(APIView):
    ''''
        GET 
        Trip에서 User가 속하는 사진만 조회 요청 
    '''
    def get(self,request,pk):
        image_classifier = ImageClassifier(pk,request.user)


