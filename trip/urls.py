from django.urls import path
from .views import *

app_name = 'trip'

urlpatterns = [
    path('', TripView.as_view()),
    path('<int:pk>/',TripDetailView.as_view())
]