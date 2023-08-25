"""epark URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views
from parking.views import ParkingListView
from django.urls import include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/login", views.login_view, name="login"),
    path("user/logout", views.logout_view, name="logout"),
    path("user/register", views.register_view, name="register"),
    path("parking/parkings", ParkingListView.as_view(), name="parking"),
    path("", views.index, name='index'),
    path("parking/", include('parking.urls')),
    path("reserves/", include('reserves.urls')),
    path('order/', include('orders.urls')),
    path("owner/register", views.register_owner_view, name="register_owner"),
    path("owner/login", views.login_owner_view, name="login_owner"),
    path("contact", views.contact_view, name="contact"),
    #path("owner/logout", views.logout_owner_view, name="logout_owner"),
    
]

urlpatterns += staticfiles_urlpatterns()