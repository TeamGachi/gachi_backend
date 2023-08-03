from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics,status
from .models import User
from .serializer import SignUpSerializer,LoginSerializer
# Create your views here.
# generics -> CRUD 뷰
# GenericAPI view의 attribute로 시리얼라이저 클래스를 가지고 있고 기본 시리얼라이저로 지정함 

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data
        return Response({'token':token.key},status=status.HTTP_200_ok)
    
class LogoutView(APIView):
    def get(self,request):
        return Response(status=200)
    
# generic API를 상속 및 사용한 유저 회원가입 뷰 
class SignUpView(generics.CreateAPIView):

    queryset = User.objects.all()
    #SignUpView의 시리얼라이저를 지정 
    serializer_class = SignUpSerializer
    
    
class TokenObtainView(APIView):
    def post(self, request):
        # 로그인 로직을 구현하고 인증이 성공한 경우 토큰을 발급
        # Refresh 토큰과 Access 토큰을 생성
        pass


class TokenRefreshView(APIView):
    def post(self, request):
        # Refresh 토큰을 이용하여 Access 토큰을 갱신
        pass

class TokenLogoutView(APIView):
    def post(self, request):
        # 로그아웃 로직을 구현하고 토큰을 무효화
        pass