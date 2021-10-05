from django import template

register = template.Library()


@register.filter
def index(indexable, i):
    b = str(indexable)
    return b[i]
