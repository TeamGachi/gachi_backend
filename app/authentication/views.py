from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status
from .serializer import SignUpSerializer, LoginSerializer
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from config import KAKAO
from django.shortcuts import redirect
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import User
import requests
import json


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = authenticate(
                request,
                email=serializer.validated_data["email"],
                password=serializer.validated_data["password"],
            )
            if user is not None:
                refreshtoken = RefreshToken.for_user(user)
                return Response(
                    {
                        "refresh": str(refreshtoken),
                        "access": str(refreshtoken.access_token),
                    },
                
                )
            else:
                return Response(
                    data={"message": "해당 유저가 존재하지 않습니다."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        else:
            return Response(
                data={"message": "유효하지 않은 정보입니다."}, status=status.HTTP_400_BAD_REQUEST
            )


class KakaoLoginView(APIView):
    def get(self, request):
        """
        카카오 인가코드 요청
        """
        kakao_login_uri = KAKAO["KAKAO_LOGIN_URI"]
        client_id = KAKAO["REST_API_KEY"]
        redirect_uri = "http://localhost:8000/api/authentication/login/kakao/callback"
        uri = f"{kakao_login_uri}?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code"
        res = redirect(uri)
        return res


class KakaoLoginCallbackView(APIView):
    def get(self, request):
        data = request.query_params.copy()
        code = data.get("code", None)
        if code is None:
            return Response(
                {"message": "해당 코드가 존재하지 않습니다."}, status.HTTP_400_BAD_REQUEST
            )

        request_data = {
            "grant_type": "authorization_code",
            "client_id": KAKAO["REST_API_KEY"],
            "redirection_uri": "http://localhost:8000/api/authentication/login/kakao/callback/",
            #'client_secret': KAKAO['KAKAO_CLIENT_SECRET_KEY'],
            "code": code,
        }
        token_headers = {
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8"
        }

        kakao_token_api = "https://kauth.kakao.com/oauth/token"
        token_res = requests.post(
            kakao_token_api, headers=token_headers, data=request_data
        ).json()

        property_keys = "[kakao_account.email]"
        kakao_url = "https://kapi.kakao.com/v2/user/me?" + property_keys

        access_token = token_res["access_token"]
        res = requests.get(
            kakao_url,
            headers={
                "Authorization": f"Bearer {access_token}",
                "Content-type": f"Content-type: application/x-www-form-urlencoded;charset=utf-8",
            },
        ).json()
        user_email = res["kakao_aacount"]["email"]

        try:
            User.objects.get(email=user_email)
        except User.DoesNotExist:
            pass

        return Response(status.HTTP_200_OK)


class LogoutView(APIView):
    def get(self, request):
        return Response({"message": "로그아웃되었습니다."}, status.HTTP_200_OK)


class SignUpView(generics.CreateAPIView):
    serializer_class = SignUpSerializer


class WithDrawView(APIView):
    """
    회원탈퇴 View
    /api/authentication/withdraw/
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        try:
            request.user.delete()
        except:
            return Response(
                {"message": "회원탈퇴에 실패하였습니다."}, status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        return Response({"message": "성공적으로 탈퇴했습니다."}, status.HTTP_202_ACCEPTED)
