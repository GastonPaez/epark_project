from unicodedata import name
from django.shortcuts import render
from reserves.utils import get_or_create_reserve
from .models import Order
from .utils import get_or_create_order
from django.contrib.auth.decorators import login_required
from .utils import breadcrumb

# Create your views here.

@login_required(login_url='login')
def order(request):
    reserve = get_or_create_reserve(request)
    order = get_or_create_order(reserve, request)

    return render(request, 'orders/order.html', {
        'reserve':reserve,
        'order':order,
        'breadcrumb': breadcrumb()
        
    } )

@login_required(login_url='login')
def credit_card(request):
    return render(request, 'orders/credit_card.html')

@login_required(login_url='confirm')
def confirm(request):
    reserve = get_or_create_reserve(request)
    order = get_or_create_order(reserve, request)
    
    return render(request, 'orders/confirm.html', {
        'reserve':reserve,
        'order':order,
        'breadcrumb': breadcrumb()
        
    } )