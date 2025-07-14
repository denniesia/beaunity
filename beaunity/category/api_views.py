from beaunity.category.permissions import IsModeratorOrSuperuser
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet
from .models import Category
from beaunity.category.serializers import CategoryCreateSerializer, CategoryEditDeleteSerializer, CategoryViewSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [IsModeratorOrSuperuser]

    def get_serializer_class(self):
        if self.action == 'create':
            return CategoryCreateSerializer
        elif self.action in ['update', 'partial_update', 'destroy']:
            return CatedoryEditDeleteSerializer
        else:
            return CategoryViewSerializer

    def perform_create(self, serializer):
        user = self.request.user
        category = serializer.save(created_by=user)
