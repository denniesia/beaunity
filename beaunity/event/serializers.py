from rest_framework import serializers

from beaunity.category.models import Category
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"