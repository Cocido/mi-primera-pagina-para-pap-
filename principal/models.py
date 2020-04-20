from django.db import models

# Create your models here.

class grupo(models.Model):
    id_grp = models.AutoField(primary_key = True, null = False)
    numero_grp = models.IntegerField()

class division(models.Model):
    id_div = models.AutoField(primary_key = True, blank = False, null = False)
    descripcion = models.CharField(max_length = 4)

class personas(models.Model):
    id_personas = models.AutoField(primary_key = True, blank = False, null = False)
    nombre = models.CharField(max_length = 50)
    grupo = models.ForeignKey(grupo, on_delete = models.CASCADE)
    division = models.ForeignKey(division, on_delete = models.CASCADE)
