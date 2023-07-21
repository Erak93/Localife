from django import template

register = template.Library()

@register.filter
def get_star_emoji(rating):
    return "⭐️" * rating