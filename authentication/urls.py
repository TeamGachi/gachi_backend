from django.urls import path
from .views import LoginView,LogoutView,SignUpView,KakaoLoginView,KakaoLoginCallbackView,WithDrawView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

app_name = 'authentication'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('login/kakao/',KakaoLoginView.as_view(),name='kakao_login'),
    path('login/kakao/callback/',KakaoLoginCallbackView.as_view(),name='kakao_login_callback'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/',SignUpView.as_view(),name='signup'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/',TokenVerifyView.as_view(),name="token_verify"),
    path('withdraw/',WithDrawView.as_view(),name='withdraw')
]
