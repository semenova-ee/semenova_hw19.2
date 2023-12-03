from django import template

register = template.Library()

@register.simple_tag
def mediapath(image_url):
    return f"/media/{image_url}"
