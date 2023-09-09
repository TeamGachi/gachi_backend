from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Friend,FriendshipRequest
from .serializer import FriendSerializer,FriendshipRequestSerializer
from authentication.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication

# 친구 목록 조회 Create
class FriendView(APIView):
    authentication_classes = [JWTAuthentication] # 요청자 식별 
    permission_classes = [IsAuthenticated] # API 요청 권한 식별 
    def get(self,request):
        user = request.user
        try:
            queryset = Friend.objects.filter(from_user = user)
            serializer = FriendSerializer(queryset,many=True)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)

# 친구요청 Create/Read
class FriendshipRequestView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] 

    serializer_class = FriendshipRequestSerializer
    queryset = FriendshipRequest.objects.all()

    def get(self,request):
        '''
            요청받은 FriendshipRequest조회 
        '''
        user = request.user
        try:
            queryset = FriendshipRequest.objects.filter(to_user = user)
            serializer = FriendshipRequestSerializer(queryset,many=True)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)
    
    def post(self,request):
        '''
            Friendship 요청 
        '''
        from_user = request.user
        to_user_email = request.data.get('to_email')
        to_user = User.objects.get(email=to_user_email)
        try:
            friendship = FriendshipRequest.objects.create(from_user = from_user , to_user = to_user)
            friendship.save()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_201_CREATED)
         
# 친구 요청 승낙 
class FriendRequestAcceptView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] 
    def post(self,request):
        '''
            요청받은 친구요청 승낙 
        '''
        user = request.user
        friendship_request_id = request.data.get('id')
        try:
            friendship_request = FriendshipRequest.objects.get(id=friendship_request_id)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        from_user_email = friendship_request.from_user # 친구 요청을 보낸 이메일
        from_user = User.objects.get(email=from_user_email)
        # a to b && b to a 
        friendship1 = Friend(from_user=user , to_user = from_user)
        friendship1.save()
        friendship2 = Friend(from_user=from_user , to_user = user)
        friendship2.save()
        return Response(status=status.HTTP_200_OK)



