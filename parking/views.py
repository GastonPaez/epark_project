from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.
from .models import Parking

class ParkingListView(ListView):
    template_name = 'parking/parkings.html'
    queryset = Parking.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # toma los contextos
        context['parkings'] = context['object_list']
        return context

class ParkingDetailView(DetailView):
    # Obtiene un objeto o registro de nuestra base de datos
    # mediante un id unico
    # indicar con que modelo vamos a trabajar
    model = Parking
    template_name = 'parking/parking.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # toma los contextos
        
        return context


class ParkingSearchListView(ListView):
    template_name = 'parking/search.html'    

    def get_queryset(self):
        return Parking.objects.filter(title__icontains=self.query())

    def query(self):
        return self.request.GET.get('q')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # toma los contextos
        context['query'] = self.query()        
        context['count'] = context['object_list'].count()
        return context