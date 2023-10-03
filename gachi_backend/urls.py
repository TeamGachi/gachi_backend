from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/authentication/', include('authentication.urls', namespace='authentication')),
    path('api/friend/', include('friend.urls', namespace='friend')),
    path('api/trip/',include('trip.urls',namespace='trip')),
    path('api/image/',include('image.urls',namespace='iamge')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
