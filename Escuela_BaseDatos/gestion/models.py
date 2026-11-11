from django.db import models

# Create your models here.
# TODO  Revisar si el datetime funciona cuando se agrega un nuevo registro

class Campus(models.Model):
    nombre_campus = models.CharField(max_length=100, unique=True)
    direccion = models.CharField(max_length=100,unique=True)
    nombre_ciudad = models.CharField(max_length=100)
    IDDirector = models.ForeignKey('Director', on_delete=models.CASCADE)
    IDUsuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_campus

class Director(models.Model):
    nombre_director = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    telefono = models.CharField(max_length=20)
    IDUsuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)

class Bloque(models.Model):
    HoraBloque = models.CharField(max_length=100,unique=True)
    Diurno_Vespertino = models.CharField(choices=[('Diurno', 'Diurno'), ('Vespertino', 'Vespertino')],max_length=30) #made with AI need rev
    IDUsuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)

class Docente(models.Model):
    nombre = models.CharField(unique=True,max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    Especialidad = models.CharField(max_length=100)
    IDUsuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)

class Sala(models.Model):
    numero_sala = models.CharField(max_length=100)
    IDUsuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)

class Asignatura(models.Model):
    nombre_asignatura = models.CharField(max_length=100)
    IDDocente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    IDSala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    IDUsuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)

class Carrera(models.Model):
    nombre_carrera=models.CharField(max_length=100)
    IDJefe_Carrera=models.ForeignKey(Docente, on_delete=models.CASCADE)
    IDCampus=models.ForeignKey(Campus, on_delete=models.CASCADE)
    IDUsuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)

class Estudiante(models.Model):
    nombre_completo = models.CharField(unique=True)
    edad = models.IntegerField()
    IDUsuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)

class DetalleEstudianteAsignatura(models.Model):
    IDEstudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    IDAsignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    FechaHoraCreacion = models.DateTimeField(auto_now_add=True)
    IDUsuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)

class DetalleEstudianteCarrera(models.Model):
    IDEstudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    IDCarrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    FechaHoraCreacion = models.DateTimeField(auto_now_add=True)
    IDUsuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)

class DetalleCarreraAsignatura(models.Model):
    IDCarrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    IDAsignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    FechaHoraCreacion = models.DateTimeField(auto_now_add=True)
    IDUsuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
