from http.client import HTTPResponse
from django.shortcuts import render 
from django.contrib import messages
from django.shortcuts import redirect

from django.contrib.auth import logout
# cierra la sesion
from django.contrib.auth import login
# genera la sesion
from django.contrib.auth import authenticate

from .forms import RegisterForm
from .forms import RegisterFormOwner
# para autenticar usuarios


#from django.contrib.auth.models import User
# se deja de usar para utilizar la personalizada
# da de alta nuevos usuarios
from users.models import User
from parking.models import Parking
from django.http import HttpResponseRedirect

def index(request):
    parkings = Parking.objects.all()
    return render(request, 'index.html', {
        'parkings': parkings,
    })

def login_view(request):
    # request.method es POST cuando se toca el boton enviar en el login
    # si se presiono el boton, obtiene el input name username y password 

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')        
        
        # busca en la base de datos un usuario que tenga ese username y contranseña
        # si existe nos retorna un objeto User almacenable si no existe nos retorna NONE
        user = authenticate(username=username, password=password)
        
        if user: 
            # para generar una sesion necesita peticion (request) y el usuario (user)
            login(request, user)
            # Mensaje de login correcto 
            messages.success(request, "Bienvenido {}".format(username))
            # se debe colocar en el template si hay mensajes para visualizarlos
            
            # si la peticion tiene la palabra next en url redirecciona a ese lugar
            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET['next'])


            # concretada lo anterior redirije al string que se coloca dentro. 
            return redirect('index')
        # Si user retorna NONE
        else:
            messages.error(request, "Usuario o Contraseña Incorrectos.")
            # se debe colocar en el template si hay mensajes para visualizarlos
            
    return render(request, 'users/login.html', {
    })

def login_owner_view(request):
    # request.method es POST cuando se toca el boton enviar en el login
    # si se presiono el boton, obtiene el input name username y password 

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')        
        
        # busca en la base de datos un usuario que tenga ese username y contranseña
        # si existe nos retorna un objeto User almacenable si no existe nos retorna NONE
        userOwner = authenticate(username=username, password=password)
        
        if userOwner: 
            # para generar una sesion necesita peticion (request) y el usuario (user)
            login(request, userOwner)
            # Mensaje de login correcto 
            messages.success(request, "Bienvenido {}".format(username))
            # se debe colocar en el template si hay mensajes para visualizarlos
            
            # concretada lo anterior redirije al string que se coloca dentro. 
            return redirect('index')
        # Si user retorna NONE
        else:
            messages.error(request, "Usuario o Contraseña Incorrectos.")
            # se debe colocar en el template si hay mensajes para visualizarlos
            
    return render(request, 'users/login_owner.html', {
    })

def logout_view(request):
    logout(request)
    messages.success(request, "Sesion cerrada exitosamente.")
    return redirect('login')

def register_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    # Trae el formulario y se debe agregar al contexto
    form = RegisterForm(request.POST or None)    
    # Si el metodo es post se genera un formulario con los datos del usuario
    # Si la peticion no es POST es decir None el formulario es vacio

    # is_valid nos indica si el formulario es valido
    if request.method == 'POST' and form.is_valid():
        #si es valido se obtienen los datos
        
        """ SE OPTIMIZA ESTE CODIGO POR FORMS.SAVE
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        """
        # crear nuevo usuario 
        user = form.save() # retorna objeto user
        if user:
            login(request,user)
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('index')


    return render(request, 'users/register.html', {
        'form': form
    })

def register_owner_view(request):
    # Trae el formulario de administrador/dueño y se debe agregar al contexto
    formOwner = RegisterFormOwner(request.POST or None)    
    # Si el metodo es post se genera un formulario con los datos del usuario
    # Si la peticion no es POST es decir None el formulario es vacio

    # is_valid nos indica si el formulario es valido
    if request.method == 'POST' and formOwner.is_valid():
        #si es valido se obtienen los datos
        """ SE OPTIMIZA ESTE CODIGO POR FORMS.SAVE
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        """
        # crear nuevo usuario 
        userOwner = formOwner.save() # retorna objeto user
        if userOwner:
            login(request,userOwner)
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('index')


    return render(request, 'users/register_owner.html', {
        'formOwner': formOwner
    })

def parking_view(request):
    parkings = Parking.objects.all()

    return render(request, 'parking/parkings.html', {
        'parkings': parkings,
    })

def logout_view(request):
    logout(request)
    messages.success(request, 'La sesión ha sido cerrada')
    return redirect('index')

def contact_view(request):
    return render(request, 'snippets/contact.html', {
        
    })

