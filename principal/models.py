from django.db import models

# Create your models here.

class grupo(models.Model):
    id_grp = models.AutoField(primary_key = True, null = False)
    nombre_grp = models.CharField(max_length = 30)
    numero_integrantes = models.IntegerField()

class comision(models.Model):
    id_com = models.AutoField(primary_key = True, blank = False, null = False)
    descripcion = models.CharField(max_length = 4)

class personas(models.Model):
    id_personas = models.AutoField(primary_key = True, blank = False, null = False)
    nombre = models.CharField(max_length = 20)
    apellido = models.CharField(max_length = 20)
    grupo = models.ForeignKey(grupo, on_delete = models.CASCADE)
    comision = models.ForeignKey(comision, on_delete = models.CASCADE)
