from rest_framework import serializers

from beaunity.category.models import Category
from beaunity.common.utils.validators import CloudinaryExtensionandSizeValidator
from .models import Event
import bleach

class EventSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Category.objects.all(),
        help_text='Please choose one or more categories.'
    )

    class Meta:
        model = Event
        fields = [
            'poster_image', 'title', 'details',
            'is_online', 'is_public', 'city', 'location', 'meeting_link',
            'start_time', 'end_time', 'categories',
        ]

    def validate_details(self, value):
        plain_text = bleach.clean(value, tags=[], strip=True)
        if len(plain_text.strip()) < 100:
            raise serializers.ValidationError("Description must be at least 100 characters.")
        return value

    def validate_poster_image(self, image):
        CloudinaryExtensionandSizeValidator()(image)
        return image