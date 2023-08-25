
from django import forms

#from django.contrib.auth.models import User
# se deja de usar para utilizar la personalizada

from users.models import User 

class RegisterForm(forms.Form):
    name = forms.CharField(label='Nombre',required=True,max_length=255, widget=forms.TextInput(attrs={'class': "form-control", 'placeholder':'Nombre de Usuario'}))    
    lastname = forms.CharField(label='Apellido', required=True,max_length=255, widget=forms.TextInput(attrs={'class': "form-control", 'placeholder':'Apellido'}))
    email = forms.EmailField(label='Escriba su E-mail', required=True,widget=forms.EmailInput(attrs={'class': "form-control", 'placeholder':'E-mail'}))    
    phone = forms.CharField(label='telefono',required=True,widget=forms.TextInput(attrs={'class': "form-control", 'placeholder':'Numero de Telefono'}))
    country = forms.CharField(label='Pais',required=True,max_length=255, widget=forms.TextInput(attrs={'class': "form-control", 'placeholder':'Su nacionalidad'}))
    city = forms.CharField(label='Ciudad',required=True,max_length=255, widget=forms.TextInput(attrs={'class': "form-control", 'placeholder':'Su Ciudad'}))
    password = forms.CharField(label='Contraseña',required=True, widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder':'Escriba su contraseña'}))
    password2 = forms.CharField(label='Repetir contraseña', required=True, widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder':'Repita su contraseña'}))
     
    def clean_email(self):
        # obtiene la informacion del input 
        email = self.cleaned_data.get('email')
        # exister el name o no 
        if User.objects.filter(email=email).exists():
             # si existe un usuario con ese name
            raise forms.ValidationError('El email ya existe')
        return email

    def clean(self):
        # obtiene todos los campos dle formulario
        cleaned_data = super().clean()

        # si las contraseñas son diferentes
        if cleaned_data.get('password2') != cleaned_data.get('password'):
            self.add_error('password2', 'Las contraseñas no coinciden')

    def save(self):
        return User.objects.create_user(
            self.cleaned_data.get('name'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password'),
        )


class RegisterFormOwner(forms.Form):
    nameOwner = forms.CharField(label='Nombre',required=True,max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nombre'}))    
    lastnameOwner = forms.CharField(label='Apellido', required=True,max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Apellido'}))
    emailOwner = forms.EmailField(label='Email',required=True,widget=forms.EmailInput(attrs={'class': "form-control", 'placeholder':'Email'}))    
    phoneOwner = forms.CharField(label='telefono',required=True,widget=forms.TextInput(attrs={'class': "form-control", 'placeholder':'telefono'}))
    countryOwner = forms.CharField(label='Pais',required=True,max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Su nacionalidad'}))
    cityOwner = forms.CharField(label='Ciudad',required=True,max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Su Ciudad'}))
    parkingName = forms.CharField(label='Nombre del Parqueadero', required=True, max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nombre del Parqueadero'}))
    parkingSpace = forms.IntegerField(label= 'Espacios dentro de Parqueadero', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Número de espacios dentro del parqueadero'}))
    passwordOwner = forms.CharField(label='Contraseña',required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Escriba su contraseña'}))
    password2Owner = forms.CharField(label='Repetir contraseña', required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Repita su contraseña'}))
    
    def clean_email(self):
        # obtiene la informacion del input 
        emailOwner = self.cleaned_data.get('emailOwner')
        # exister el name o no 
        if User.objects.filter(emailOwner=emailOwner).exists():
             # si existe un usuario con ese name
            raise forms.ValidationError('El email ya existe')
        return emailOwner

    def clean(self):
        # obtiene todos los campos dle formulario
        cleaned_data = super().clean()

        # si las contraseñas son diferentes
        if cleaned_data.get('password2') != cleaned_data.get('password'):
            self.add_error('password2', 'Las contraseñas no coinciden')

    def save(self):
        return User.objects.create_user(
            self.cleaned_data.get('nameOwner'),
            self.cleaned_data.get('emailOwner'),
            self.cleaned_data.get('passwordOwner'),
        )