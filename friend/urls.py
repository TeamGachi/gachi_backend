from django.urls import path
from .views import FriendView,FriendshipRequestView,FriendshipRe

app_name = 'friend'

urlpatterns = [
    path('', FriendView.as_view(), name='friend'),
    path('request/',FriendshipRequestView.as_view(),name='friend_request'),
    path('request/',FriendshipRequestView.as_view(),name='friend_request')
]