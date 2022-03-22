from django import forms

class formulario_videojuego(forms.Form):
    nombre = forms.CharField(max_length=40)
    genero = forms.CharField(max_length=20)
    puntaje = forms.IntegerField()
    
class formulario_pelicula(forms.Form):
    nombre = forms.CharField(max_length=50)
    genero = forms.CharField(max_length=20)
    lanzamiento = forms.DateField
    
class formulario_futbol(forms.Form):
    equipo = forms.CharField(max_length=40)
    liga = forms.CharField(max_length=20)