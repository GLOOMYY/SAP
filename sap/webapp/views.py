from django.http import HttpResponse
from django.shortcuts import render
from personas.models import Persona

# Create your views here.

def bienvenido(request):
  numPersonas = Persona.objects.count()
  #personas= Persona .objects.all()
  personas = Persona.objects.order_by('id')
  return render(request, 'prueba.html', {'personas':personas, 'numPersonas':numPersonas})

def contacto(request):
  return HttpResponse("Nombre: Sebastian Mesa \nTelefono: 3053438319 \nEmail: sebas.mesa.montoya@gmail.com")
