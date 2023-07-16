from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

class LoginView(APIView):
    def get(self,request):
        return Response(status=200)
    
class LogoutView(APIView):
    def get(self,request):
        return Response(status=200)
    
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