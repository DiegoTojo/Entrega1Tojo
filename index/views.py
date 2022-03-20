from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
# Create your views here.

def index(request):
    return HttpResponse('<h1>Bienvenido a mi pagina de Django</h1>')

def plantilla(request):
    
    template = loader.get_template('plantilla.html')
    
    plantilla_generada = template.render({})
    
    return HttpResponse (plantilla_generada)