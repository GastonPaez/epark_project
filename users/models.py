
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# Create your models here.

# AbstractBaseUser nos permite utilizar los atributos ID, password y lastlogin
#AbstractUser Nos permite utilizar muchos mas atributos
class User(AbstractUser):

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)
        

class Customer(User):
# Customer hereda de User (no genera otra tabla en la BBDD)
    # con el proxy true se pueden definir metodos a la clase padre.
    class Meta:
        proxy = True 

    def get_parking(self):
        return []

class Profile(models.Model):
    # se relaciona con el modelo usuario, y tambien de elimina  el registro profile si deja de existir
    user = models.OneToOneField(User, on_delete=models.CASCADE)




