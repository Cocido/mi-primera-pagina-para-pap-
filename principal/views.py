from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import personas, grupo, division

# Create your views here.

def inicio(request):
    grp = grupo.objects.all()
    div = division.objects.all()
    return render(request, 'principal/inicio.html',{'grp': grp, 'div': div})

def retorno(request):
    return render(request, 'principal/retorno.html',{})
