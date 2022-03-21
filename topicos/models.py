from django.db import models

# Create your models here.
class Videojuego(models.Model):
    nombre = models.CharField(max_length=40)
    genero = models.CharField(max_length=20)
    puntaje = models.IntegerField(max_length=2)
    
class Pelicula(models.Model):
    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=20)
    lanzamiento = models.DateField

class Futbol(models.Model):
    equipo = models.CharField(max_length=40)
    liga = models.CharField(max_length=20)