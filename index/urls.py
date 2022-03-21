from re import template
from unicodedata import name
from django.urls import path
from .views import index, sobrenosotros

urlpatterns = [
    path('', index, name='index'),
    path('sobrenosotros/',sobrenosotros,name='sobrenosotros')
]
