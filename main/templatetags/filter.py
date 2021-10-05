from django import template

register = template.Library()


@register.filter
def sub(a, b):
    return b-a
