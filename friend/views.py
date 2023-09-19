from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status,generics
from .models import Friend,FriendshipRequest
from .serializer import FriendSerializer,FriendshipRequestSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404

# 친구 R
class FriendView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication] 
    permission_classes = [IsAuthenticated] 
    serializer_class = FriendSerializer
    
    def get_queryset(self):
        user = self.request.user
        queryset = Friend.objects.filter(user = user)
        return queryset

# 친구요청 CR
class FriendshipRequestView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] 
    serializer_class = FriendshipRequestSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = FriendshipRequest.objects.filter(receiver=user)
        return queryset

    def list(self,request):
        queryset = self.get_queryset()
        serialzier = FriendshipRequestSerializer(queryset,many=True)
        return Response(serialzier.data,status=status.HTTP_200_OK)

    
# 친구요청 
class FriendshipRequestHandleView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] 

    def post(self,request,pk):
        '''
            친구요청 승낙 
        '''
        friendship_request = get_object_or_404(FriendshipRequest,id=pk)
        sender = friendship_request.sender
        recevier = request.user
        friendship1 = Friend(user=sender , friend = recevier)
        friendship1.save()
        friendship2 = Friend(user=recevier , friend = sender)
        friendship2.save()
        friendship_request.delete()
        return Response(status=status.HTTP_200_OK)
    
    def delete(self,request,pk):
        '''
            친구요청 거부 
        '''
        friendship = get_object_or_404(FriendshipRequest,id=pk)
        friendship.delete()
        return Response(status=status.HTTP_20)


