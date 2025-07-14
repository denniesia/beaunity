from beaunity.common.permissions import IsCreator
from beaunity.post.serializers import PostCreateSerializer, PostViewSerializer, PostEditDeleteSerializer
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
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

class PostEditDeleteView(UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostEditDeleteSerializer
    permission_classes = [IsCreator]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)