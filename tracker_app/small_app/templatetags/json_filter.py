from django.utils.safestring import mark_safe
import json
from django import template
register = template.Library()

@register.filter(is_safe=True)
def SafeArray(value):
    return mark_safe(json.dumps(value))