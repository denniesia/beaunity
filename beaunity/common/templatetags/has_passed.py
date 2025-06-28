from django import template
from django.utils.timezone import now

register = template.Library()

@register.filter
def has_passd(obj_datetime):
    return obj_datetime < now()