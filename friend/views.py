from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status,generics
from .models import Friend,FriendshipRequest
from .serializer import FriendSerializer,FriendshipRequestSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404

class FriendView(generics.ListAPIView):
    '''
        GET
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
        친구요청 생성 및 친구요청 조회 VIEW 
    '''
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] 
    serializer_class = FriendshipRequestSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = FriendshipRequest.objects.filter(receiver=user)
        return queryset
    

class FriendshipRequestHandleView(APIView):
    '''
        POST DELETE
        친구요청 거부 및 친구요청 승낙 
    '''
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] 

    def delete(self,request,pk):
        friendship = get_object_or_404(FriendshipRequest,id=pk)
        friendship.delete()
        return Response(status=status.HTTP_200_OK)

    def post(self,request,pk):
        '''
            친구요청 승낙 
        '''
        try:
            friendship_request = get_object_or_404(FriendshipRequest,id=pk)
            sender = friendship_request.sender
            recevier = request.user
            friendship1 = Friend(user=sender , friend = recevier)
            friendship1.save()
            friendship2 = Friend(user=recevier , friend = sender)
            friendship2.save()
            friendship_request.delete()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        

