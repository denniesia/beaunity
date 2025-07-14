from beaunity.post.serializers import PostCreateSerializer, PostViewSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet
from .models import Post

class PostCreateAPIView(CreateAPIView):
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        post = serializer.save(created_by=user)

        if user.has_perm('post.can_post_without_approval'):
            post.is_approved = True
            post.save()

class PostViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostViewSerializer
    permission_classes = [AllowAny]

