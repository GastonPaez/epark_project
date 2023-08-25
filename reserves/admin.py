from django.contrib import admin
from .models import Reserve
# Register your models here.

    
class ReserveAdmin(admin.ModelAdmin):
    list_display = ('user', 'reserve_id', 'created_at')

admin.site.register(Reserve, ReserveAdmin)
