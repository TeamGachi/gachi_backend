from django.urls import path
from .views import *

app_name = 'image'

urlpatterns = [
    path('', ImageView.as_view()),
    path('<int:pk>/',ImageView.as_view())
]