from django.shortcuts import render

def index(request):
    return render (request,"index/index.html",{})

def sobrenosotros(request):
    return render (request,"index/sobrenosotros.html", {})

