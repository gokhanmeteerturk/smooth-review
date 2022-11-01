from django import template
from django.conf import settings
import random
from smoothapp import cssClassNames

register = template.Library()

ALLOWED_SETTINGS = ('SITENAME_PRETTY', 'DEFAULT_FROM_EMAIL')


@register.simple_tag
def get_setting(name):
    if name not in ALLOWED_SETTINGS:
        return ""
    return getattr(settings, name, "")


@register.simple_tag
def get_class_name(css_group_name, attribute_name):
    css_group = getattr(cssClassNames, css_group_name, None)
    if css_group:
        return getattr(css_group, attribute_name, "")
    return ""


@register.simple_tag
def get_random_category():
    return random.choice(['game', 'shoes', 'burger', 'drink', 'game', 'car', 'game'])
