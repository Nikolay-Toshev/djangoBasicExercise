from django import template
from profiles.models import Profile

register = template.Library()

@register.simple_tag
def get_user():
    return Profile.objects.all().first()