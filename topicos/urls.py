from django.urls import path
from .views import juego,pelicula,futbol

urlpatterns = [
    path('videojuego/',juego , name='videojuego'),
    path('peliculas/',pelicula,name='pelicula'),
    path('futbol/',futbol,name='futbol')
]

