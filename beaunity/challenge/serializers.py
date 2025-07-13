from rest_framework import serializers
from .models import Challenge
from beaunity.category.models import Category
import bleach
from drf_spectacular.utils import extend_schema_field


class ChallengeSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    categories = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Category.objects.all(),
        help_text='Please choose one or more categories.'
    )
    attendees  = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
    )
    progress = serializers.ReadOnlyField()
    duration_in_weeks = serializers.SerializerMethodField()
    is_approved = serializers.ReadOnlyField()

    class Meta:
        model = Challenge
        fields = '__all__'

    def validate_details(self, value):
        plain_text = bleach.clean(value, tags=[], strip=True)
        if len(plain_text.strip()) < 100:
            raise serializers.ValidationError("Description must be at least 100 characters (excluding formatting).")
        return value

    @extend_schema_field(int)
    def get_duration_in_weeks(self, obj):
        return obj.duration_in_weeks