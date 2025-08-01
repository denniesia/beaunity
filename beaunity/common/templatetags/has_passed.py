from django import template
from django.utils.timezone import now

register = template.Library()

@register.filter
def has_passed(obj_datetime):
    if obj_datetime:
        return obj_datetime < now()