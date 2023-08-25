from .models import Order
from django.urls import reverse

def get_or_create_order(reserve, request):
    order = reserve.order

    if order is None and request.user.is_authenticated:
        order = Order.objects.create(reserve=reserve, user= request.user)
    
    if order:
        request.session['order_id']= order.order_id

    return order

def breadcrumb(parkings=True, payment=False, confirmation=False):
    return [ 
        {'title':'Parkings', 'active':parkings, 'url': reverse('orders:order')},
        {'title':'Pago', 'active':payment, 'url': reverse('orders:order')},
        {'title':'Confirmacion', 'active':confirmation, 'url': reverse('orders:order')}
    ]