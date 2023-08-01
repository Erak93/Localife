from django import template

register = template.Library()

@register.filter
def get_star_emoji(rating):
    return "⭐️" * rating

@register.filter
def extract_id(name):
    from user_app.models import Experience
    experience = Experience.objects.get(title=name)
    return experience.id

@register.filter
def extract_host(host_name):
    from user_app.models import Experience
    experience = Experience.objects.get(host__user__username=host_name)
    return experience.id