from rest_framework.permissions import BasePermission


class CanAddEvent(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm("event.add_event")