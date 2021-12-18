from django.shortcuts import render

from entrenador.service import *
from .models import Entrenador , EntrenadorPokemones
from .forms import *
from django.shortcuts import  render, redirect
from random import randrange
from pokemones.models import Pokemones
from django.utils import timezone

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
        nickUser = formulario['nick'].value()

        informacionEntrenador = Entrenador(nick= nickUser,
        password= formulario['password'].value(),
        nombre= formulario['nombre'].value(),
        region=formulario['region'].value(),
        medallas=0,
        batallas=0,
        fechaRegistro= str(timezone.now())[:19]
        )

        listaIdsPokemones =  crearAuxiliar(r, nickUser) ## deberia ser una excepcion
        informacionEntrenador.save()

        '''for value in listaIdsPokemones: ## PREGUNTAR

            print (" LOG 1 ->>> ")
            #formulario = EntrenadorPokemonesForm()

            #entrenador = EntrenadorPokemones.entrenador(entrenador = int(informacionEntrenador) )
            #pokemon = EntrenadorPokemones.pokemones(entrenador = int(value) )

            entrenadorPokemones = EntrenadorPokemones(entrenador = 20, pokemones= 160 )

            entrenadorPokemones.save()'''

        return render(r, "entrenador/crear.html", context)

    return render(r, "entrenador/register.html", context)

def crearAuxiliar(r,nickUser):

        listaIdsPokemones=[]

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
                return crearAuxiliar(r,nickUser) ## entonces se vuelve a mandar la peticion
            moviminetosSeleccionados.append(data)
        
        i=0

        while i<len(moviminetosSeleccionados):

            j=0
            while j<4:

                moviminetosSeleccionados[i][j] = get_moves_data( moviminetosSeleccionados[i][j] )
                
                j+=1
            
            dicc = get_tipo_e_imagenes(pokemonesSeleccionados[i])

            poke = Pokemones(
                nombre = pokemonesSeleccionados[i] + " / " + nickUser ,
                tipo = dicc['tipo'],
                icono = dicc['icono'],
                imagen = dicc['imagen'],
                moviminetoUno = moviminetosSeleccionados[i][0],
                moviminetoDos = moviminetosSeleccionados[i][1],
                moviminetoTres = moviminetosSeleccionados[i][2],
                moviminetoCuatro  = moviminetosSeleccionados[i][3],
                entrenador = nickUser)
            poke.save()
            listaIdsPokemones.append(poke.id)

            i+=1

        return listaIdsPokemones

def listarPokemones(r, nick):
    pokemones = Pokemones.objects.filter(entrenador=nick)
    print( pokemones )
    context = {  
        "pokemones" : pokemones
      }
    return render(r, "entrenador/listar_pokemones.html", context)

def listarPokemonesAlterno(r, id):
    entrenador = Entrenador.objects.get(pk=id)
    pokemones = EntrenadorPokemones.objects.filter(entrenador=entrenador) ##regresa el join con la tabla asignatura
    
    context = {  
        "pokemones" : pokemones
      }
    return render(r, "entrenador/listar_pokemones_alterno.html", context)
