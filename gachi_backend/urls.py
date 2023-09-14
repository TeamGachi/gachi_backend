from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/authentication/', include('authentication.urls', namespace='authentication')),
    path('api/friend/', include('friend.urls', namespace='friend')),
    path('api/trip',include('trip.urls',namespace='trip')),
]
