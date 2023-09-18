from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics,status
from .models import User
from .serializer import SignUpSerializer,LoginSerializer
from django.contrib.auth import authenticate
from config import *
from django.shortcuts import redirect
import requests
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
        카카오 인가코드 요청
        '''
        kakao_login_uri = "https://kauth.kakao.com/oauth/authorize"
        client_id = KAKAO["REST_API_KEY"]
        redirect_uri = "http://localhost:8000/api/authentication/login/kakao/callback" 
        uri = f"{kakao_login_uri}?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code"
        res = redirect(uri)
        return res

# Kakao Authentication Redirection View , 인가 token 발급 요청 
class KakaoLoginCallbackView(APIView):
    def get(self,request):
        '''
        카카오 인가코드로 access token 요청 
        '''
        data = {
            "grant_type" : "authorization_code",
            "cliend_id" : KAKAO["REST_API_KEY"],
            "redirection_uri" : "http://localhost:8000/api/authentication/login/kakao/callback/",
            "code" : request.GET["code"]
        }
        kakao_token_api = "https://kauth.kakao.com/oauth/token"
        access_token = requests.post(kakao_token_api,data=data).json()["access_token"]
        kakao_inforamtion_api = "https://kapi.kakao.com/v2/user/me"
        header = {
            "Authorization" : f"Bearer ${access_token}"
        }
        user_information = requests.get(kakao_inforamtion_api,headers=header).json()
        ## 신규회원이면 회원가입 및 회원이면 로그인 로직 
        
        ##
        return Response(status=status.HTTP_200_OK)

# 로그아웃      
class LogoutView(APIView):
    def get(self,request):
        return Response(status=200)
    
# 회원가입 
class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    #SignUpView의 시리얼라이저를 지정 
    serializer_class = SignUpSerializer



