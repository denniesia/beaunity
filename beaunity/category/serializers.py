from rest_framework import serializers
from .models import Category
from beaunity.accounts.serializers import UserSerializier

class CategorySimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'description')


class CategorySerializer(serializers.ModelSerializer):
    created_by = UserSerializier(read_only=True)
    last_updated = serializers.DateTimeField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Category
        fields = ['title', 'image', 'description', "last_updated", "created_by", "created_at"]

