from django.shortcuts import render
from django.urls import is_valid_path
from topicos.models import Futbol, Videojuego,Pelicula,Futbol
from topicos.forms import formulario_futbol, formulario_pelicula, formulario_videojuego
# Create your views here.

def juego(request):
    formulario = formulario_videojuego(request.POST)
    if formulario.is_valid():
            data = formulario.cleaned_data 
            nuevo_videojuego =Videojuego(nombre=data['nombre'],genero=data['genero'],puntaje=data['puntaje'])
            nuevo_videojuego.save()
            return render(request,"index/index.html",{'nuevo_videojuego':nuevo_videojuego})    
    formulario = formulario_videojuego()
    return render(request,"videojuego/videojuego.html",{'formulario':formulario})


def pelicula(request):
    if request.method == 'POST':
        formulario = formulario_pelicula(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data 
            nueva_pelicula =Pelicula(nombre=data['nombre'],genero=data['genero'],lanzamiento=data['lanzamiento'])
            nueva_pelicula.save()
            return render(request,"index/index.html",{'nueva_pelicula':nueva_pelicula})    
    formulario = formulario_pelicula()
    return render(request,"videojuego/videojuego.html",{'formulario':formulario})


def futbol(request):
    if request.method == 'POST':
        formulario = formulario_futbol(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data 
            nuevo_futbol =Futbol(equipo=data['equipo'],liga=data['liga'])
            nuevo_futbol.save()
            return render(request,"index/index.html",{'nueva_pelicula':nueva_pelicula})    
    formulario = formulario_futbol()
    return render(request,"videojuego/videojuego.html",{'formulario':formulario})