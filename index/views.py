from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import personas, grupo, division

# Create your views here.

def inicio(request):
    grp = grupo.objects.all()
    return render(request, 'index/inicio.html',{})
