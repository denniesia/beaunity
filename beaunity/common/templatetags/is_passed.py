from django import template
from django.utils.timezone import now

register = template.Library()

@register.filter
def is_past(obj_date):
    return obj_date < now()