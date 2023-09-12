from django.urls import path
from .views import *

app_name = 'trip'

urlpatterns = [
    path('informations/', TripView.as_view()),
    path('detail/<int:pk>/',TripDetailView.as_view())
]