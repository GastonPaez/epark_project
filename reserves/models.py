from django.db import models
from users.models import User
from parking.models import Parking
import uuid
from django.db.models.signals import pre_save
from django.db.models.signals import m2m_changed
from django.db.models.signals import post_save

class Reserve(models.Model):
    reserve_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    parkings = models.ManyToManyField(Parking, through='ReserveParkings')
    subtotal = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    total = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.parkings} con id:{self.reserve_id}' 
    
    def update_totals(self):
        self.update_subtotal()
        self.update_total()
        """
        # se intenta obtener la orden de la reserva
        order = self.order_set.first()
        # si la orden existe se actualiza su total (por si se modifico)
        if order:
            order.update_total()"""
        if self.order:
            self.order.update_total()
    
    def update_subtotal(self):
          # metodos para obtener obj parking y ReserveParking en la misma consulta
        self.subtotal = sum([cp.quantity * cp.parking.price_hour for cp in self.parkings_related()])                             
        self.save()
    
    def update_total(self):
        FEE = 0.05
        self.total = self.subtotal 
        self.save()

    def parkings_related(self):
        # Mejora el pedido de consulta relacionada a una sola consulta
        return self.reserveparkings_set.select_related('parking')

    @property
    def order(self):
        # order_set es la relacion uno a muchos
        return self.order_set.first()

class ReserveParkingsManager(models.Manager):
    
    def create_or_update_quantity(self, reserve, parking, quantity=1):
        # metodo que permite obtener un objeto, si no existe lo crea
        object, created = self.get_or_create(reserve=reserve, parking=parking)

        if not created:
            quantity = object.quantity + quantity 
            
        object.update_quantity(quantity)
        return object

class ReserveParkings(models.Model):
    reserve = models.ForeignKey(Reserve, on_delete=models.CASCADE)
    parking = models.ForeignKey(Parking, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = ReserveParkingsManager()

    def update_quantity(self, quantity=1):
        self.quantity = quantity 
        self.save()

def set_reserve_id(sender, instance, *args, **kwargs):
    if not instance.reserve_id:
        instance.reserve_id = str(uuid.uuid4())

def update_totals(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clean':
      instance.update_totals()

def post_save_update_totals(sender, instance, *args, **kwargs):
    instance.reserve.update_totals()

        
pre_save.connect(set_reserve_id, sender=Reserve)
# Cuando se cree un objeto ReserveParkings se ejecutra el signal post_save
post_save.connect(post_save_update_totals, sender=ReserveParkings)
# cuando se agregue una reserva, se elimine o se limpie se calculan los totales.
m2m_changed.connect(update_totals, sender=Reserve.parkings.through)
