from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'image', 'description']

class CategoryCreateSerializer(CategorySerializer):
    pass

class CategoryEditDeleteSerializer(CategorySerializer):
    pass

class CategoryViewSerializer(serializers.ModelSerializer):
    class Meta(CategorySerializer.Meta):
        fields = CategorySerializer.Meta.fields + ["last_updated", "created_by", "created_at"]