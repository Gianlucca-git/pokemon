from django.shortcuts import render

from entrenador.service import *
from .models import Entrenador , EntrenadorPokemones
from .forms import EntrenadorForm
from django.shortcuts import  render, redirect
from random import randrange
from pokemones.models import Pokemones


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
            
            data = get_pokemon_data(nombrePokemon) 
            if len(data) == 0: ## por si pasa un error es por que el pókemon no esta en el api externa.
                return crear(r) ## entonces se vuelve a mandar la peticion
            moviminetosSeleccionados.append(data)
        
        i=0
        while i<len(moviminetosSeleccionados):

            j=0
            while j<4:

                moviminetosSeleccionados[i][j] = get_moves_data( moviminetosSeleccionados[i][j] )
                j+=1
            
            print(moviminetosSeleccionados)
            poke = Pokemones(
                nombre = pokemonesSeleccionados[i],
                tipo = 'f' ,
                icono = 'f', 
                imagen = 'f',
                moviminetoUno = 'f',
                moviminetoDos = 'f',
                moviminetoTres = 'f',
                moviminetoCuatro  = 'f')
            poke.save()

            i+=1

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

