from django.shortcuts import render

from entrenador.service import *
from .models import Entrenador , EntrenadorPokemones
from .forms import EntrenadorForm
from django.shortcuts import  render, redirect
from random import randrange

def listar(r):
    context = {
        "entrenadores": Entrenador.objects.all()
    }
    return render(r, "entrenador/listar.html", context)

def crear(r):

    formulario =  EntrenadorForm()
    context = {
        "formulario" :formulario,
    }

    if r.POST:
        formulario = EntrenadorForm(r.POST)

        print("ENTRE")
        pokemonesExistentes= get_pokemon_list()
        pokemonesSeleccionados = ['pikachu']
        i=0
        listRamdons=[]
        while i<5:
            
            intRamdon= randrange(len(pokemonesExistentes)-1)
            if intRamdon in listRamdons:
                continue
            
            listRamdons.append(intRamdon)
            pokemonesSeleccionados.append(pokemonesExistentes[listRamdons[i]])
            
            i+=1 
        
        moviminetosSeleccionados = []
        for nombrePokemon in pokemonesSeleccionados:
            moviminetosSeleccionados.append(get_pokemon_data(nombrePokemon)[0:])

        i=0
        while i<len(moviminetosSeleccionados):
            print("Log 0 ----------------")

            j=0
            while j<4:

                moviminetosSeleccionados[i][j] = get_moves_data( moviminetosSeleccionados[i][j] )
                j+=1
            
            i+=1

        print("Log 1 ----------------")
        print(moviminetosSeleccionados)
        ##formulario.save()

        ##return redirect("listar")

    return render(r, "entrenador/register.html", context)



def listarPokemones(r, id):
    entrenador = Entrenador.objects.get(pk=id)
    pokemones = EntrenadorPokemones.objects.filter(entrenador=entrenador) ##regresa el join con la tabla asignatura
    
    context = {  
        "pokemones" : pokemones
      }
    return render(r, "entrenador/listar_pokemones.html", context)

