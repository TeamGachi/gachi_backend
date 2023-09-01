from django.urls import path
from .views import *


urlpatterns = [
    # 여행 api
    path('<int:group>/', TripView.as_view()),
    path('detail/<int:trip>/', TripDetailView.as_view()),
    ]