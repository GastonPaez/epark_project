from django.urls import path
from . import views

app_name = 'parking'
urlpatterns = [
    path('search', views.ParkingSearchListView.as_view(), name='search'),
    path('<slug:slug>', views.ParkingDetailView.as_view(), name='parking'),

]