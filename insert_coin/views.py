from django.shortcuts import render
from insert_coin_app.models import *
from django.http import HttpResponse

# Create your views here.

def agregar_ps5(request):
    str_nombre = "Fifa 23"
    ps5 = PS5(nombre="Fifa 23", genero="Deportes", online=False, precio="39.99")
    ps5.save()
    documento = f"Se agregó el juego {str_nombre}"
    return HttpResponse(documento)  #FInal clase 18
