from re import template
from unicodedata import name
from django.urls import path
from .views import index

urlpatterns = [
    path('', index)
]
