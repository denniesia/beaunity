from django import template
from django.contrib.contenttypes.models import ContentType
from beaunity.interaction.models import Like, Favourite

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

@register.filter
def is_favourited_by_user(obj, user):
    content_type = ContentType.objects.get_for_model(obj)
    return Favourite.objects.filter(
        user=user,
        content_type=content_type,
        object_id=obj.id
    ).exists()

@register.simple_tag
def has_joined(user, model_name, obj_id):
    if model_name == 'event':
        return user.joined_events.filter(pk=obj_id).exists()
    elif model_name == 'challenge':
        return user.joined_challenges.filter(pk=obj_id).exists()
    return False