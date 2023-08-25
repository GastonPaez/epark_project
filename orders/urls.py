from django.urls import path

from . import views

app_name = 'orders'
urlpatterns = [
    path('', views.order, name='order'),
    path('credit-card', views.credit_card, name='credit-card'),
    path('confirm', views.confirm, name='confirm')
    
]