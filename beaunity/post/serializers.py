from rest_framework import serializers
from .models import Post
from beaunity.category.models import Category


class PostSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        help_text='Please choose one or more categories.'
    )
    class Meta:
        model = Post
        fields = ["banner", "title", "content", "category"]

class PostCreateSerializer(PostSerializer):
    pass

class PostEditDeleteSerializer(PostSerializer):
    pass


class PostViewSerializer(PostSerializer):
    class Meta(PostSerializer.Meta):
        fields = PostSerializer.Meta.fields + ["last_updated", "created_by", "created_at" ]