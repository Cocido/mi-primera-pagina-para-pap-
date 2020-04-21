from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import personas, grupo, comision

# Create your views here.

def inicio(request):
    grp = grupo.objects.all()
    com = com.objects.all()
    return render(request, 'principal/inicio.html',{'grp': grp, 'com': com})

def retorno(request):
    nombregrp = request.POST['nombreTxt']
    nombreInt1 = request.POST['nombreIntegrante1']
    nombreInt2 = request.POST['nombreIntegrante2']
    nombreInt3 = request.POST['nombreIntegrante3']
    nombreInt4 = request.POST['nombreIntegrante4']
    nombreInt5 = request.POST['nombreIntegrante5']
    nombreInt6 = request.POST['nombreIntegrante6']
    appellidoInt1 = request.POST['apellidoIntegrante1']
    appellidoInt2 = request.POST['apellidoIntegrante2']
    appellidoInt3 = request.POST['apellidoIntegrante3']
    appellidoInt4 = request.POST['apellidoIntegrante4']
    appellidoInt5 = request.POST['apellidoIntegrante5']
    appellidoInt6 = request.POST['apellidoIntegrante6']
    dniInt1 = request.POST['dniIntegrante1']
    dniInt2 = request.POST['dniIntegrante2']
    dniInt3 = request.POST['dniIntegrante3']
    dniInt4 = request.POST['dniIntegrante4']
    dniInt5 = request.POST['dniIntegrante5']
    dniInt6 = request.POST['dniIntegrante6']
    grpS = request.POST['grpS']
    comS = request.POST['divS']
    guardar = personas(nombre= nombre,
        comision = comS,
        grupo_id = grpS
    )
    guardar.save()
    return render(request, 'principal/retorno.html',{})
