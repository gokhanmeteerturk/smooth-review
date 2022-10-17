from django import template
from django.conf import settings

register = template.Library()

ALLOWED_SETTINGS = ('SITENAME_PRETTY', 'DEFAULT_FROM_EMAIL')

@register.simple_tag
def get_setting(name):
    if name not in ALLOWED_SETTINGS:
        return ""
    return getattr(settings, name, "")
