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
        if email is None: # PK에 속하는 모든 여행 이미지 리턴 
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset,many=True)
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        else: # Return Task ID 
            trip = get_object_or_404(Trip,id=kwargs['pk'])
            user = get_object_or_404(User,email=email)
            image_classifier = ImageClassifier(trip=trip,user=user)
            task = image_classifier.get_user_included_images.delay() 
            return Response(data={"task":str(task)},status=status.HTTP_200_OK)
        
class ClassfiedImageListView(generics.ListAPIView):
    '''
        GET
        /api/image/classified/<str:task>/
        Trip에 속하는 분류된 이미지 요청 View 
    '''
    authentication_classes = [JWTAuthentication]
    permission_classes = [TripMembersOnly] 
    serializer_class = TripImageSerializer

    def list(self, request, *args, **kwargs):
        task_id = self.request.GET.get("task",None)
        if task_id is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        task_result = AsyncResult(task_id)
        result = {
            "task_id": task_id,
            "task_status": task_result.status,
            "task_result": task_result.result
        }
        return Response(data=result,status=status.HTTP_200_OK)



    
