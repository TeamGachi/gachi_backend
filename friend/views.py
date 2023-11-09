from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status,generics
from .models import Friend,FriendshipRequest
from .serializer import FriendSerializer,FriendshipRequestSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from django.db import transaction

class FriendView(generics.ListAPIView):
    '''
        GET
        /api/friend/
        친구 조회 VIEW
    '''
    authentication_classes = [JWTAuthentication] 
    permission_classes = [IsAuthenticated] 
    serializer_class = FriendSerializer
    
    def get_queryset(self):
        user = self.request.user
        queryset = Friend.objects.filter(user = user)
        return queryset

class FriendshipRequestView(generics.ListCreateAPIView):
    '''
        POST GET 
        /api/friend/request/
        친구요청 생성 및 친구요청 조회 
    '''
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] 
    serializer_class = FriendshipRequestSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = FriendshipRequest.objects.filter(receiver=user)
        return queryset

class FriendshipRequestHandleView(generics.UpdateAPIView):
    '''
        PATCH
        /api/friend/request/<int:pk>/
        친구요청 거부 및 친구요청 승낙 
    '''
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] 

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        '''
            친구요청 승낙 및 거절
        '''
        message = {"message":""}
        action = request.data.get('action')
        
        if action == "accept":
            friendship_request = get_object_or_404(FriendshipRequest,id=kwargs['pk'])
            sender = friendship_request.sender
            recevier = request.user
            friendship1 = Friend(user=sender,friend=recevier)
            friendship1.save()
            friendship2 = Friend(user=recevier,friend=sender)
            friendship2.save()
            friendship_request.delete()
            message["message"] = "친구요청을 수락하였습니다."
        elif action == "reject":
            friendship = get_object_or_404(FriendshipRequest,id=kwargs['pk'])
            friendship.delete()
            message["message"] = "친구요청을 거절하였습니다."
        else:
            message["message"] = "올바르지 않은 action을 입력하였습니다. "
            return Response(message,status.HTTP_400_BAD_REQUEST)
        return Response(message,status.HTTP_200_OK)


