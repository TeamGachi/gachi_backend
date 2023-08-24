from django.urls import path
from .views import FreindRequestView,AcceptRequestView

app_name = 'authentication'

urlpatterns = [
    path('request/', FreindRequestView.as_view(), name='request'),
    path('accept/',AcceptRequestView.as_view(),name='accept')
]