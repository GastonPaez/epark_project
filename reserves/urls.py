from django.urls import path 
from . import views

app_name = 'reserves'
urlpatterns = [
    path('', views.reserve, name='reserve'),
    path('add', views.add, name='add'),
    path('remove', views.remove, name='remove'),
    
]