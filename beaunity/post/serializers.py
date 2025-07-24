from rest_framework import serializers

from beaunity.accounts.serializers import UserSerializer
from beaunity.category.models import Category
from beaunity.category.serializers import CategorySerializer

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='title'
    )
    created_by = UserSerializer(read_only=True)
    last_updated = serializers.DateTimeField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    banner = serializers.URLField(
        required=False,
        allow_blank=True,
        allow_null=True,
    )

    class Meta:
        model = Post
        fields = [
            "banner", "title",
            "content", "category",
            "last_updated", "created_by",
            "created_at"
        ]
