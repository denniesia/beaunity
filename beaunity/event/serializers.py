from rest_framework import serializers
from beaunity.category.models import Category
from beaunity.common.validators import CloudinaryExtensionandSizeValidator
from .models import Event
import bleach
from beaunity.accounts.serializers import UserSerialiazier
from beaunity.category.serializers import CategorySimpleSerializer


class EventSerializer(serializers.ModelSerializer):
    categories = CategorySimpleSerializer(many=True, read_only=True)
    created_by = UserSerialiazier(read_only=True)
    is_public = serializers.BooleanField(read_only=True)
    last_updated = serializers.DateTimeField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Event
        fields = [
            'poster_image', 'title', 'details',
            'is_online', 'is_public', 'city', 'location', 'meeting_link',
            'start_time', 'end_time', 'categories', "last_updated", "created_by",
            "created_at", 'is_public'
        ]

    def validate_details(self, value):
        plain_text = bleach.clean(value, tags=[], strip=True)
        if len(plain_text.strip()) < 100:
            raise serializers.ValidationError("Description must be at least 100 characters.")
        return value

    def validate_poster_image(self, image):
        CloudinaryExtensionandSizeValidator()(image)
        return image

class EventCreateSerializer(EventSerializer):
    categories = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='title',
        many=True,
    )