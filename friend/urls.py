from django.urls import path
from .views import FriendView,FriendRequestView

app_name = 'friend'

urlpatterns = [
    path('', FriendView.as_view(), name='friend'),
    path('request/',FriendRequestView.as_view(),name='friend_request')
]