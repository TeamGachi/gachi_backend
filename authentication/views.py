from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics,status
from .models import User
from .serializer import SignUpSerializer,LoginSerializer
from django.contrib.auth import authenticate
from config import KAKAO
from django.shortcuts import redirect
# Create your views here.
# generics -> CRUD 뷰
# GenericAPI view의 attribute로 시리얼라이저 클래스를 가지고 있고 기본 시리얼라이저로 지정함 

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self,request):
        serializer = self.get_serializer(data=request.data) # genericAPIview의 get_serializer를 통해 시리얼라이저 지정
        if serializer.is_valid(raise_exception=True): # login 데이터가 유효한지 검사하기 위해 validate메소드 실행
            # validated data는 is_valid를 통해 validate를 진행한 딕셔너리 
            user = authenticate( # basic authentication model을 활용하여 인증 
                request,
                email = serializer.validated_data['email'],
                password = serializer.validated_data['password']
            )
            if user is not None:
                refreshtoken = RefreshToken.for_user(user)    
                return Response({
                    'refresh': str(refreshtoken),
                    'access': str(refreshtoken.access_token),
                })
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
# 카카오 로그인 API 
class KakaoLoginView(APIView):
    def get(self,request):
        '''
        카카오 코드 요청
        '''
        kakao_login_uri = "https://kauth.kakao.com/oauth/authorize"
        client_id = KAKAO["REST_API_KEY"]
        redirect_uri = "http://localhost:8000/api/authentication/login/kakao/callback" 
        uri = f"{kakao_login_uri}?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code"
        res = redirect(uri)
        return res

# Kakao Authentication 완료시 Redirection View 
class KakaoLoginCallbackView(APIView):
    '''
        신규가입시 : DB push 및 정보생성
        기존회원 : 토큰 발급 
        Code를 받고 리다이렉션됨 
    '''
    def get_queryset(self):
        search_text = self.request.GET.get('code')
    def get(self,request):
        return Response(data={"hd":"dff"},status=status.HTTP_200_OK)


# front에서 토큰 폐기              
class LogoutView(APIView):
    def get(self,request):
        return Response(status=200)
    
# generic API를 상속 및 사용한 유저 회원가입 뷰 
class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    #SignUpView의 시리얼라이저를 지정 
    serializer_class = SignUpSerializer



