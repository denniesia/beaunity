from rest_framework.permissions import BasePermission

class CanAddCategory(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm("category.add_category")




