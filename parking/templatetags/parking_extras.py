from django import template

register = template.Library()

@register.filter()
def price_format(value):
    # Solo muestra dos digitos
    return '${0:.2f}'.format(value)