from django.shortcuts import render, get_object_or_404  , redirect
from personas.models import Persona, Domicilio
from personas.forms import PersonaForm

# Vistas Persona

def detallePersona(request, id):
  #persona = Persona.objects.get(pk=id)
  persona = get_object_or_404(Persona, pk=id)
  return render(request, 'personas/detalle.html', {'persona': persona})

def formaPersona(request):
  if request.method == 'POST': # Si vieien datos por post significa que vamos a editar los datos existentes, esta info la trae el request
    formaPersona = PersonaForm(request.POST)
    if formaPersona.is_valid(): #Si es valido enviamos a la db con save()
      formaPersona.save() 
      return redirect('index')
  else: # Si no, vamos a crear una persona nueva
    formaPersona= PersonaForm()
    
  return render(request, 'personas/nuevo.html', {'formaPersona': formaPersona})

def editarPersona(request, id):
  persona = get_object_or_404(Persona, pk=id)
  if request.method == 'POST': # Si vieien datos por post significa que vamos a editar los datos existentes, esta info la trae el request
    formaPersona = PersonaForm(request.POST, instance=persona) #Al indicar la instancia pasa de ser un save a un update en la DB
    if formaPersona.is_valid(): #Si es valido enviamos a la db con save()
      formaPersona.save() 
      return redirect('index')
  else: # Si no, vamos a crear una persona nueva
    formaPersona= PersonaForm(instance=persona) #Instance para indicar que vamos a enviar una instancia de persona
    
  return render(request, 'personas/nuevo.html', {'formaPersona': formaPersona})

def eliminarPersona(request, id):
  persona = get_object_or_404(Persona, pk=id)
  if persona:
    persona.delete()
  return redirect('index')

# Vistas Domicilios
def mostrarDomicilios(request):
  domicilios = Domicilio.objects.all()
  return render(request, 'domicilios/base.html', {'domicilios':domicilios})

def detalleDomicilio(request, id):
  domicilio = get_object_or_404(Domicilio, pk=id)
  return render(request, 'domicilios/detalle.html', {'domicilio':domicilio})

def nuevoDomicilio(request):
  return redirect('index')

def editarDomicilio(request, id):
  return redirect('index')

def eliminarDomicilio(request, id):
  domicilio = get_object_or_404(Domicilio, pk=id)
  if domicilio:
    domicilio.delete()
  return redirect('/domicilios')

