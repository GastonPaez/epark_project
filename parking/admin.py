from django.contrib import admin
from .models import Parking
# Register your models here.

class ParkingAdmin(admin.ModelAdmin):
    fields = ('title', 'address_p', 'city', 'price_hour','price_day','price_week','price_month','slots', 'url_map', 'image')
    list_display = ('__str__', 'slug', 'created_at')


admin.site.register(Parking, ParkingAdmin)

