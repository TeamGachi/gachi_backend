from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics,status
from .serializer import SignUpSerializer,LoginSerializer
from django.contrib.auth import authenticate
from config import *
from django.shortcuts import redirect
import requests

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self,request):
        serializer = self.get_serializer(data=request.data) 
        if serializer.is_valid(raise_exception=True): 
            user = authenticate( 
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
                return Response(data={"message" : "해당 유저가 존재하지 않습니다." },
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data={"message" : "유효하지 않은 정보입니다." },
                            status=status.HTTP_400_BAD_REQUEST)
        
# 카카오 로그인 API 
class KakaoLoginView(APIView):

    def get(self,request):
        '''
            카카오 인가코드 요청
        '''
        kakao_login_uri = KAKAO["KAKAO_LOGIN_URI"]
        client_id = KAKAO["REST_API_KEY"]
        redirect_uri = "http://localhost:8000/api/authentication/login/kakao/callback" 
        uri = f"{kakao_login_uri}?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code"
        res = redirect(uri)
        return res

# Kakao Authentication Redirection View , 인가 token 발급 요청 
class KakaoLoginCallbackView(APIView):

    def get(self,request):
        data = request.query_params.copy()
        code = data.get('code')
        if not code:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        request_data = {
            "grant_type" : "authorization_code",
            "cliend_id" : KAKAO["REST_API_KEY"],
            "redirection_uri" : "http://localhost:8000/api/authentication/login/kakao/callback/",
            'client_secret': KAKAO['KAKAO_CLIENT_SECRET_KEY'],
            "code" : code
        }
        token_headers = {
            'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'
        }
     
        kakao_token_api = "https://kauth.kakao.com/oauth/token"
        token_res = requests.post(kakao_token_api,data=request_data,headers=token_headers).json()        
        return Response(status=status.HTTP_200_OK)

# 로그아웃      
class LogoutView(APIView):
    
    def get(self,request):
        return Response(status=200)
    
# 회원가입 
class SignUpView(generics.CreateAPIView):
    serializer_class = SignUpSerializer





