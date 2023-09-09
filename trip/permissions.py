from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied, NotAuthenticated
from django.shortcuts import get_object_or_404
from authentication.models import User
from .models import TripList

# Trip 멤버만이 접근할 수 있음 
class TripMembersOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    # trip session에 대한 권한을 가지고 있는지 검사 
    def has_object_permission(self, request, view, obj):  # trip object
        if request.user.is_authenticated:
            user_trips = TripList.objects.filter(member=request.user)
            if obj in user_trips:
                return True
            raise PermissionDenied()
        raise NotAuthenticated()


