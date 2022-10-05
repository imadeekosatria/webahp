from django import template

register = template.Library()

@register.simple_tag
def kategories(list):
    for l in list:
        return l
    