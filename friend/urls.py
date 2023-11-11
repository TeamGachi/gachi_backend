from django.urls import path
from .views import FriendView, FriendshipRequestView, FriendshipRequestHandleView

app_name = "friend"

urlpatterns = [
    path("", FriendView.as_view(), name="friend"),
    path("request/", FriendshipRequestView.as_view(), name="friendship_request"),
    path(
        "request/<int:pk>/",
        FriendshipRequestHandleView.as_view(),
        name="friendship_handle",
    ),
]
