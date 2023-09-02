from django.urls import path
from .views import FreindView,AcceptRequestView

app_name = 'friend'

urlpatterns = [
    path('request/', FreindView.as_view(), name='friend'),
    path('accept/',AcceptRequestView.as_view(),name='accept')
]