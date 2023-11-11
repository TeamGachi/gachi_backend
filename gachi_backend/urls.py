from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)


urlpatterns = [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path("admin/", admin.site.urls),
    path(
        "api/authentication/",
        include("authentication.urls", namespace="authentication"),
    ),
    path("api/friend/", include("friend.urls", namespace="friend")),
    path("api/trip/", include("trip.urls", namespace="trip")),
    path("api/image/", include("image.urls", namespace="iamge")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
