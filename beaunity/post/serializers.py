from rest_framework import serializers
from .models import Post
from beaunity.category.models import Category
from beaunity.accounts.serializers import UserSerialiazier

class PostSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        help_text='Please choose one category.'
    )
    created_by = UserSerialiazier(read_only=True)
    last_updated = serializers.DateTimeField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Post
        fields = ["banner", "title", "content", "category", "last_updated", "created_by", "created_at"]

