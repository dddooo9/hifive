from django import template

register = template.Library()


@register.filter
def sub(before, after):
    return before - after

