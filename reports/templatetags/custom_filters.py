# custom_filters.py
from django import template

register = template.Library()

@register.filter
def model_name(obj):
    return obj.__class__._meta.model_name
