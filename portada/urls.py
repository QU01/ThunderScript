"""Posts URLs."""

# Django
from django.urls import path

# Views
from portada.views import inicio
from portada.views import plataforma
from portada.views import info
from portada.views import geolocate

urlpatterns = [

    path('plataforma/', plataforma, name='email'),
    path('info/', info, name='info'),
    path('Scan/', geolocate, name='Scan'),
]
