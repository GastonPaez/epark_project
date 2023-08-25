from django import template

# Registrar funciones como filters
register = template.Library()

@register.filter()
def quantity_parking_format(quantity=1):
    return '{} {}'.format(quantity, 'horas' if quantity > 1 else 'hora')

@register.filter()
def quantity_add_format(quantity=1):
    return '{} {}'.format(
        quantity_parking_format(quantity),
        'agregadas' if quantity > 1 else 'agregada'
     )
