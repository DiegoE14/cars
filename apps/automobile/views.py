from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Bienvenidos a mi tienda de autos")

def portfolio(request):
    return HttpResponse("Bienvenidos a nuestro portafolio")

def info(request, id):
    return HttpResponse("ID de búsqueda %s" % id)
