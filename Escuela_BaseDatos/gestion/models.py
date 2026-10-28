from django.db import models

# Create your models here.

class Docente(models.Model):
    nombre = models.CharField()
    email = models.EmailField(unique=True)
    Especialidad = models.CharField()