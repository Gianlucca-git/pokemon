from django.shortcuts import render
from .models import Entrenador , EntrenadorPokemones
from .forms import EntrenadorForm
from django.shortcuts import  render, redirect

def listar(r):
    context = {
        "entrenadores": Entrenador.objects.all()
    }
    return render(r, "entrenador/listar.html", context)

def listarPokemones(r, id):
    entrenador = Entrenador.objects.get(pk=id)
    pokemones = EntrenadorPokemones.objects.filter(entrenador=entrenador) ##regresa el join con la tabla asignatura
    
    context = {  
        "pokemones" : pokemones
      }
    return render(r, "entrenador/listar_pokemones.html", context)