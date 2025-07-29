import bleach
from rest_framework import serializers

from beaunity.accounts.serializers import UserSerializer
from beaunity.category.models import Category
from beaunity.category.serializers import CategorySimpleSerializer
from beaunity.common.validators import CloudinaryExtensionandSizeValidator

from .models import Event


class EventSerializer(serializers.ModelSerializer):
    categories = CategorySimpleSerializer(many=True, read_only=True)
    created_by = UserSerializer(read_only=True)
    is_public = serializers.BooleanField(read_only=True)
    last_updated = serializers.DateTimeField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Event
        fields = [
            'poster_image', 'title', 'details',
            'is_online', 'is_public', 'city', 'location',
            'meeting_link', 'start_time', 'end_time', 'categories',
            "last_updated", "created_by", "created_at", 'is_public'
        ]

    def validate_details(self, value):
        cleaned_value = bleach.clean(value, tags=[], strip=True)
        if len(cleaned_value.strip()) < 100:
            raise serializers.ValidationError("Description must be at least 100 characters.")
        return cleaned_value

    def validate_poster_image(self, image):
        CloudinaryExtensionandSizeValidator()(image)
        return image

    def validate(self, data):
        start_time = data.get("start_time")
        end_time = data.get("end_time")

        if start_time and end_time and end_time <= start_time:
            raise serializers.ValidationError(
                {"end_time": "End time must be after start time."}
            )
        return data

class EventCreateSerializer(EventSerializer):
    categories = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug',
        many=True,
    )