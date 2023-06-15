from django.http import HttpResponse
from django.shortcuts import render
from personas.models import Persona

# Create your views here.

def bienvenido(request):
  numPersonas = Persona.objects.count()
  return render(request, 'prueba.html', {'numPersonas':numPersonas})

def contacto(request):
  return HttpResponse("Nombre: Sebastian Mesa \nTelefono: 3053438319 \nEmail: sebas.mesa.montoya@gmail.com")