from rest_framework.permissions import BasePermission

class CanApprove(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('challenge.can_approve_challenge')

