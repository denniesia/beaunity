from rest_framework import serializers

from beaunity.category.models import Category

from .models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

    def validate_details(self, value):
        plain_text = bleach.clean(value, tags=[], strip=True)
        if len(plain_text.strip()) < 100:
            raise serializers.ValidationError(
                "Description must be at least 100 characters (excluding formatting)."
            )
        return value
