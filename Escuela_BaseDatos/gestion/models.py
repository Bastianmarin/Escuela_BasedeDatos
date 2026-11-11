from django.db import models

# Create your models here.
# TODO: Fill the choice field in diurno/vesp
# TODO  Revisar si el datetime funciona cuando se agrega un nuevo registro

class Campus(models.Model):
    nombre_campus = models.CharField(unique=True)
    direccion = models.CharField(unique=True)
    nombre_ciudad = models.CharField()
    nombre_Director = models.CharField()
    telefono_Director = models.CharField()
    def __str__(self):
        return self.nombre_campus

class Bloque(models.Model):
    HoraBloque = models.CharField(unique=True)
    Diurno_Vespertino = models.CharField(choices=[('Diurno', 'Diurno'), ('Vespertino', 'Vespertino')]) #made with AI need rev

class Docente(models.Model):
    nombre = models.CharField(unique=True)
    email = models.EmailField(unique=True)
    Especialidad = models.CharField()

class Sala(models.Model):
    numero_sala = models.CharField()

class Asignatura(models.Model):
    nombre_asignatura = models.CharField()
    IDDocente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    IDSala = models.ForeignKey(Sala, on_delete=models.CASCADE)

class Carrera(models.Model):
    nombre_carrera=models.CharField()
    IDJefe_Carrera=models.ForeignKey(Docente, on_delete=models.CASCADE)
    IDCampus=models.ForeignKey(Campus, on_delete=models.CASCADE)

class Estudiante(models.Model):
    nombre_completo = models.CharField(unique=True)
    edad = models.IntegerField()
    IDCarrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)

class DetalleEstudianteCarrera(models.Model):
    IDEstudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    IDCarrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    FechaHoraCreacion = models.DateTimeField(auto_now_add=True)

class DetalleCarreraAsignatura(models.Model):
    IDCarrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    IDAsignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    FechaHoraCreacion = models.DateTimeField(auto_now_add=True)

