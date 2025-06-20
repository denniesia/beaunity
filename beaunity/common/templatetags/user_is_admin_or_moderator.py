from django import template
from beaunity.common.utils import user_is_admin_or_moderator

register = template.Library()

@register.simple_tag(name='user_is_admin_or_moderator')
def is_admin_or_moderator(user):
    return user_is_admin_or_moderator(user)