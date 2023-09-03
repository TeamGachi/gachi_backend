from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import Token
from rest_framework import status
from .models import Friend,FriendshipRequest
from .serializer import FriendSerializer,FriendshipRequestSerializer
from authentication.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication

# 친구 목록 조회
class FriendView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        user = request.user
        return Response({"user_id":user.id,"email":user.name})
    def post(self,request):
        try:
            token = Token(str(request.data.get('token')))
        except Exception as e:
            raise Exception("Invalid Token")
        return token
    
# 친구 요청 CREATE 
class FriendRequestView(APIView):
    def post(self,request):
        serializer = FriendshipRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
         
# 친구 요청 승낙 
class FriendRequestAcceptView(APIView):
    pass


