from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied,NotAuthenticated
from trip.models import Trip

class TripMembersOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
    # User가 Trip의 멤버인지 검사 
    def has_object_permission(self, request, view, obj):  
        if request.user.is_authenticated:
            user_trips = Trip.objects.filter(users=request.user)
            if obj in user_trips:
                return True
            raise PermissionDenied()
        raise NotAuthenticated()


