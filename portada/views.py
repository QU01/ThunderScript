from django.shortcuts import render
from .forms import cmsmap
from .forms import zero
from .forms import mack
# Create your views here.

import os

def inicio(request):

    return render(request, "inicio.html", {})

def plataforma(request):

    form = cmsmap(request.POST or None)
    
    if form.is_valid():

        form_data = form.cleaned_data

        website= form_data.get("website")

        print (" Data Recolected {0}".format(website))
        
        output = os.popen("python infoga.py --domain %s --source all --breach -v 2" %(website)).read()
        return render(request, "plataforma1.html", {"output":output,"cmsmap":form,})

   
    return render(request, "plataforma1.html", {"cmsmap":form})
    
def info(request):

    form = zero(request.POST or None)
    
    if form.is_valid():

        form_data = form.cleaned_data

        email= form_data.get("email")

        print (" Data Recolected {0}".format(email))
        
        output = os.popen("python infoga.py --info %s  --breach -v 3" %(email)).read()
        return render(request, "plataforma2.html", {"output":output,"zero":zero,})

   
    return render(request, "plataforma2.html", {"zero":zero})

def phoneinfo(request):

    form = mack(request.POST or None)
    
    if form.is_valid():

        form_data = form.cleaned_data

        phone= form_data.get("phone")

        print (" Data Recolected {0}".format(phone))
        
        output = os.popen("cd PhoneInfoga, python3 phoneinfoga.py -n %s -s footprints" %(phone)).read()
        return render(request, "plataforma3.html", {"output":output,"mack":mack,})

   
    return render(request, "plataforma3.html", {"mack":mack})