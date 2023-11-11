from django.urls import path
from .views import *

app_name = "trip"

urlpatterns = [
    path("", TripView.as_view()),
    path("<int:pk>/", TripUpdateView.as_view()),
    path("invite/", TripInviteView.as_view()),
    path("invite/<int:pk>/", TrpInviteUpdateView.as_view()),
]
