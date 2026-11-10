from django.db import models

# Create your models here.

class Campus(models.Model):
    nombre_campus = models.CharField(unique=True)
    direccion = models.CharField()
    nombre_ciudad = models.CharField()
    nombre_Director = models.CharField(unique=True)
    telefono_Director = models.CharField(unique=True)

    def __str__(self):
        return self.nombre_campus

class Jornada(models.Model):
    id_campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    Vespertino_Diurno = models.CharField()

class Horario(models.Model):
    Bloques = models.CharField()
    id_jornada = models.ForeignKey(Jornada, on_delete=models.CASCADE)

class Jefe_de_Carrera(models.Model):

class 


class Docente(models.Model):
    nombre = models.CharField()
    email = models.EmailField(unique=True)
    Especialidad = models.CharField()