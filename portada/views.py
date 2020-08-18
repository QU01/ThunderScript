#Django
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

#Libraries
from .forms import cmsmap
from .forms import zero
from .forms import mack
import nmap
import geoip2.database

# Create your views here.

import os

#Methods

user = User

#Views



def inicio(request,*args,**kwargs):

    return render(request, "inicio.html", {})


def plataforma(request):

    form = cmsmap(request.POST or None)

    if user.is_authenticated:


        if form.is_valid():

            form_data = form.cleaned_data

            website= form_data.get("website")

            print (" Data Recolected {0}".format(website))

            output = os.popen("python infoga.py --domain %s --source all --breach -v 2" %(website)).read()
            return render(request, "plataforma1.html", {"output":output,"cmsmap":form,})


        return render(request, "plataforma1.html", {"cmsmap":form})

    else:

        return redirect('http://127.0.0.1:8000/')


def info(request):

    form = zero(request.POST or None)

    if user.is_authenticated:

        if form.is_valid():

            form_data = form.cleaned_data

            email= form_data.get("email")

            print (" Data Recolected {0}".format(email))

            output = os.popen("python infoga.py --info %s  --breach -v 3" %(email)).read()
            return render(request, "plataforma2.html", {"output":output,"zero":zero,})


        return render(request, "plataforma2.html", {"zero":zero})

    else:

        return redirect('http://127.0.0.1:8000/')



def geolocate(request):

    form = mack(request.POST or None)

    if user.is_authenticated:

        if form.is_valid():

            form_data = form.cleaned_data

            ip= form_data.get("IP")
            reader = geoip2.database.Reader('GeoLite2-City.mmdb')
            response = reader.city(ip)

            print (" Data Recolected {0}".format(ip))



            output = response.city.name
            return render(request, "plataforma3.html", {"output":output,"mack":mack,})


        return render(request, "plataforma3.html", {"mack":mack})
