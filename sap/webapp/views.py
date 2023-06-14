from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def bienvenido(request):
  return HttpResponse('Bienvenidos a la pagina SAP')

def despedirse(request):
  return HttpResponse('Chaito')

def contacto(request):
  return HttpResponse("Nombre: Sebastian Mesa \nTelefono: 3053438319 \nEmail: sebas.mesa.montoya@gmail.com")