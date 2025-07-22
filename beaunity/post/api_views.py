from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from beaunity.category.models import Category
from beaunity.common.permissions import IsCreatorOrSuperuser
from beaunity.post.serializers import PostSerializer

from .models import Post


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [AllowAny]
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsCreatorOrSuperuser()]
        elif self.action == 'create':
            return [IsAuthenticated()]
        return [AllowAny()]

    def perform_create(self, serializer):
        user = self.request.user
        post = serializer.save(created_by=user)

        if user.has_perm('post.can_post_without_approval'):
            post.is_approved = True
            post.save()

