from django.urls import path
from .views import *

app_name = 'image'

urlpatterns = [
    path('',ImageView.as_view()) # 해당 PK 여행의 사진 목록 
]