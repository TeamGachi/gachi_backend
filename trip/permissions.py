from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied, NotAuthenticated
from django.shortcuts import get_object_or_404
from authentication.models import User

# Trip 멤버만이 접근할 수 있음 
class TripMembersOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    # trip session에 대한 권한을 가지고 있는지 검사 
    def has_object_permission(self, request, view, obj):  # trip object 전달
        pass 