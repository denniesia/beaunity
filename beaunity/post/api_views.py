from beaunity.common.permissions import IsCreator
from beaunity.post.serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
from .models import Post

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [AllowAny]
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsCreator()]
        elif self.action == 'create':
            return [IsAuthenticated()]
        return [AllowAny()]

    def perform_create(self, serializer):
        user = self.request.user
        post = serializer.save(created_by=user)

        if user.has_perm('post.can_post_without_approval'):
            post.is_approved = True
            post.save()