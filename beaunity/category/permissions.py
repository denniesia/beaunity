from rest_framework.permissions import BasePermission

class IsModeratorOrSuperuser(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name__in=['Superuser','Moderator']).exists()




