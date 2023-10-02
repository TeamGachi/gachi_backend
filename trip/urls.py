from django.urls import path
from .views import *

app_name = 'trip'

urlpatterns = [
    path('', TripView.as_view()),
    path('<int:pk>/',TripView.as_view()),
    path('invite/',TripInviteView.as_view()),
    path('invite/<int:pk>/',TrpInviteHandleView.as_view()),
]