from rest_framework import serializers

from beaunity.accounts.serializers import UserSerializer

from .models import Category


class CategorySimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "title",
            "description"
        )


class CategorySerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    last_updated = serializers.DateTimeField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Category
        fields = [
            "id",
            "title",
            "image",
            "description",
            "last_updated",
            "created_by",
            "created_at",
        ]
