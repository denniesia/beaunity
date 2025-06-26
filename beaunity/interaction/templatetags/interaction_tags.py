from django import template
from django.contrib.contenttypes.models import ContentType
from beaunity.interaction.models import Like

register = template.Library()

@register.filter
def is_liked_by_user(obj, user):
    content_type = ContentType.objects.get_for_model(obj)
    return Like.objects.filter(
        user=user,
        content_type=content_type,
        object_id=obj.id
    ).exists()

@register.filter
def total_likes(obj):
    content_type = ContentType.objects.get_for_model(obj)
    return Like.objects.filter(
        content_type=content_type,
        object_id=obj.id
    ).count()