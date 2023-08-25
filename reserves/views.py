
from django.shortcuts import render
from .models import Reserve
from .utils import get_or_create_reserve
from parking.models import Parking
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .models import ReserveParkings
# Create your views here.
def reserve(request):    
    reserve = get_or_create_reserve(request)    
    
    return render(request, 'reserves/reserve.html', {
        'reserve': reserve
    })

def add(request):
    reserve = get_or_create_reserve(request)
    # obtiene el producto del formulario, con su name parking_id declarado en add.html
    parking = Parking.objects.get(pk=request.POST.get('parking_id'))    
    
    quantity = int(request.POST.get('quantity', 1))
    """
    # Se agrega el objeto de reserva a la relacion reserve-parking
    reserve.parkings.add(parking,through_defaults={
        'quantity': quantity
    } )    #reserve.parkings.add(parking)"""
    # 
    reserve_parking = ReserveParkings.objects.create_or_update_quantity(reserve=reserve, parking=parking, quantity=quantity)
   
    return render(request, 'reserves/add.html', {
        'quantity': quantity,
        'parking': parking
    })

def remove(request):
    reserve = get_or_create_reserve(request)
    parking = get_object_or_404(Parking, pk=request.POST.get('parking_id'))    

    reserve.parkings.remove(parking)

    return redirect('reserves:reserve')