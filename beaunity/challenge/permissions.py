from rest_framework.permissions import BasePermission

class CanApprove(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('challenge.can_approve_challenge')


class IsCreator(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.created_by == request.user


