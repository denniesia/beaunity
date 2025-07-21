from rest_framework import serializers
from .models import Challenge
from beaunity.category.models import Category
import bleach
from drf_spectacular.utils import extend_schema_field
from beaunity.common.validators import CloudinaryExtensionandSizeValidator
from beaunity.accounts.serializers import UserSerializer
from beaunity.category.serializers import CategorySimpleSerializer


class ChallengeSerializer(serializers.ModelSerializer):
    categories = CategorySimpleSerializer(many=True, read_only=True)
    created_by = UserSerializer(read_only=True)
    last_updated = serializers.DateTimeField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Challenge
        fields = [
            'poster_image', 'title', 'details',
            'is_online', 'city', 'location', 'meeting_link',
            'start_time', 'end_time', 'categories',
            'difficulty', "last_updated", "created_by", "created_at"
        ]

    def validate_details(self, value):
        plain_text = bleach.clean(value, tags=[], strip=True)
        if len(plain_text.strip()) < 100:
            raise serializers.ValidationError("Description must be at least 100 characters.")
        return cleaned_value

    def validate_poster_image(self, image):
        try:
            CloudinaryExtensionandSizeValidator()(image)
        except serializers.ValidationError as e:
            raise serializers.ValidationError(str(e))
        return image

    def validate(self, data):
        start_time = data.get('start_time')
        end_time = data.get('end_time')

        if start_time and end_time and end_time <= start_time:
            raise serializers.ValidationError(
                {
                    "end_time": "End time must be after start time."
                }
            )
        return data

class ChallengeCreateSerializer(ChallengeSerializer):
    categories = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='title',
        many=True,
    )