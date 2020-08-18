#Utilities

from django.contrib import admin
from django.urls import path, include

#views


from login import views as login_in
from portada.views import inicio
from portada.views import plataforma
from portada.views import info
from portada.views import geolocate

#urls

urlpatterns = [

    path('', login_in.login_view, name='login'),
    path('main/', include (('portada.urls', 'portada'), namespace='scanners')),
    path('elpotroloco/', admin.site.urls, name='admin'),

]
