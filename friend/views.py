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

# 친구 목록 조회 Create
class FriendView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        user = request.user
        email_list = []
        # User Friend list
        try:
            friends = Friend.objects.filter(from_user = user)
            for friend in friends:
                friend_email = friend.to_user.email
                email_list.append(friend_email)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        print(email_list)
        return Response({"user_id":user.id,"email":user.name})

        
    
# 친구요청 Create Read
class FriendshipRequestView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        user = request.user
        email_list = []
        try:
            friendship_requests = FriendshipRequest.objects.filter(to_user = user)
            for friendship_request in friendship_requests:
                from_user_email = friendship_request.from_user.email
                email_list.append(from_user_email)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        print(email_list)
        return Response({"user_id":user.id,"email":user.name})
    
    def post(self,request):
        serializer = FriendshipRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=False)  # Trigger Bad Request if errors exist
        serializer.save(user=request.user)         # Passing the current user
        return Response(serializer.data, status=status.HTTP_201_CREATED)
         
# 친구 요청 승낙 
class FriendRequestAcceptView(APIView):
    pass


