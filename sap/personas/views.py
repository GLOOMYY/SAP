from django.shortcuts import render, get_object_or_404  , redirect
from personas.models import Persona
from personas.forms import PersonaForm



# Create your views here.

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
