from pyexpat import model
from django.db import models
from django.utils.text import slugify
import uuid
from django.db.models.signals import pre_save

# Create your models here.
class Parking(models.Model):
    # crea tabla en la base de datos, los atributos son las columnas de las tablas.
    title = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    owner_name = models.CharField(max_length=50)
    owner_surname = models.CharField(max_length=50)
    address_p  = models.TextField()   
    # x_address # cordenadas para la imprementacion de la API de map
    # y_address
    price_hour = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)        
    price_day = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)        
    price_week = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)        
    price_month = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    phone_p = models.CharField(max_length=20)
    mail_p = models.EmailField()
    country_p = models.CharField(max_length=30)
    city_p = models.CharField(max_length=30)
    slots =  models.IntegerField()    
    url_map = models.CharField(max_length=500)
    avalaible = models.BooleanField(default=True)
    slug = models.SlugField(null=False, blank=False, unique=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.CharField(max_length=500)
    
    def __str__(self) -> str:
        return self.title

class Users(models.Model):
    user_name = models.CharField(max_length=50)
    user_surname = models.CharField(max_length=50)
    phone_u = models.CharField(max_length=20)
    mail_u = models.EmailField()
    country_u = models.CharField(max_length=30)
    city_u = models.CharField(max_length=30)
    car_plate = models.CharField(max_length=20, default="sin confirmar")
    # card = models.CharField(max_length=20)

class Reservations(models.Model):
    user_name = models.ForeignKey(Parking, on_delete=models.CASCADE)
    title = models.ForeignKey(Users, on_delete=models.CASCADE)

    """
        MODIFICADO POR SIGNALS
    def save(self, *args, **kwargs):
        # Guarda el slug
        self.slug = slugify(self.title)
        super(Parking, self).save(*args, **kwargs)"""

    def __str__(self) -> str:
        return self.title

def set_slug(sender, instance, *args, **kwargs): # Debe recibir 5 elementos
    if instance.title and not instance.slug:
        slug = slugify(instance.title)

        
        # si existe algun objeto con ese slug, genera uno nuevo
        while Parking.objects.filter(slug=slug).exists():
            # pone caracteres aleatorios con la libreria uuid
            slug = slugify(
                '{}-{}'.format(instance.title, str(uuid.uuid4())[:8]  )
            )
        # La instancia es nuestro objeto almacenado
        instance.slug = slug
    
# Antes de que un objeto parking se almacene se ejecutra el callback set_slug
pre_save.connect(set_slug, sender=Parking)