from .models import Reserve

def get_or_create_reserve(request):
    # Crear sesion
    # obtenemos el usuario authenticado
    user = request.user if request.user.is_authenticated else None
    reserve_id = request.session.get('reserve_id') # Si existe nos retorna el reserve sino retorna None
    reserve = Reserve.objects.filter(reserve_id=reserve_id).first() # Retorna elemento sino None
    
    # si el reserve no existe
    if reserve is None:
        # se crea un reserve
        reserve = Reserve.objects.create(user=user)

    if user and reserve.user is None: #Si el usuario existe y el reserve no posee usuario
        # Se asigna el reserve al usuario logeado.
        reserve.user = user 
        reserve.save()

    request.session['reserve_id'] = reserve.reserve_id

    return reserve