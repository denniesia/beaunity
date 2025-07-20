from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from beaunity.category.permissions import CanAddCategory
from beaunity.category.serializers import CategorySerializer

from .models import Category


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [CanAddCategory]
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        user = self.request.user
        category = serializer.save(created_by=user)
