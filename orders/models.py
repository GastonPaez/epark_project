from django.db import models
from users.models import User
from reserves.models import Reserve
from enum import Enum
from django.db.models.signals import pre_save
import uuid
# Create your models here.

class OrderStatus(Enum):
    CREATED = 'CREATED'
    PAYED = 'PAYED'
    COMPLETED = 'COMPLETED'
    CANCELED = 'CANCELED'

choices = [ (tag, tag.value) for tag in OrderStatus ]

class Order(models.Model):
    order_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reserve = models.ForeignKey(Reserve, on_delete=models.CASCADE)
    status = models.CharField(max_length=40, choices=choices, default=OrderStatus.CREATED) 
    total = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_id
    
    def update_total(self):
        self.total = self.get_total()
        self.save()
    
    def get_total(self):
        return self.reserve.total



def set_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = str(uuid.uuid4())

def set_total(sender, instance, *args, **kwargs):
    instance.total = instance.get_total()

# Antes que se almacenen los objetos order, se ejecutan los callbacks
pre_save.connect(set_order_id, sender=Order)
pre_save.connect(set_total, sender=Order)

