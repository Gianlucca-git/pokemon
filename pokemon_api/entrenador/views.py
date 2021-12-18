from django.shortcuts import render
from entrenador.service import *
from preguntas.models import Preguntas
from .models import *
from .forms import *
from django.shortcuts import  render, redirect
from random import randrange
from pokemones.models import Pokemones
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import EntrenadorSerializer
from rest_framework import status
from django.http import Http404

def login(r):
    formulario =  LoginForm(r.POST)
    context = {
         "formulario" :formulario,
    }
    if r.POST:
        formulario = LoginForm(r.POST)
        try:
            miEntrenador=Entrenador.objects.get(nick=formulario['nick'].value()) 
            try:
                pokemones = Pokemones.objects.filter(entrenador=formulario['nick'].value())
                context = {  
                    "pokemones" : pokemones
                }
                if miEntrenador.password == formulario['password'].value():
                    return render(r, "entrenador/listar_pokemones.html", context)
            except:
                return render(r, "entrenador/login.html", context)
        except:
            return render(r, "entrenador/login.html", context)
    return render(r, "entrenador/login.html", context)

def listar(r):
    context = {
        "entrenadores": Entrenador.objects.all()
    }
    return render(r, "entrenador/listar.html", context)

def listarArtificiales(r):
    context = {
        "user": "gian-1", 
        "entrenadores": Artificial.objects.all()
    }
    return render(r, "entrenador/listar_artificiales.html", context)

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

        return redirect ("login")

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

def listarPokemonesDefault(r, id):
    entrenador = Artificial.objects.get(pk=id)
    pokemones = EntrenadorArticialPokemones.objects.filter(entrenador=entrenador) ##regresa el join con la tabla asignatura
    
    context = {  
        "pokemones" : pokemones
      }
    return render(r, "entrenador/listar_pokemones_alterno.html", context)

def batalla(r, nick, id, vida):

    if int(vida) < 0 :
        return redirect(listar)

    preguntas = Preguntas.objects.all()
    artificial = Artificial.objects.get(pk=id) 
    formulario= BatallaForm()
    
    ## Revolver las Respuestas -----------------
    i=0  
    preguntasLimitadas=[]
    while i< 10:
        numberRamdon = randrange(1)
        if numberRamdon == 0:
            preguntasRamdon = Preguntas( pregunta=preguntas[i].pregunta,
                                         respuestaCorrecta=preguntas[i].respuestaIncorrecta1, 
                                         respuestaIncorrecta1=preguntas[i].respuestaCorrecta, 
                                         respuestaIncorrecta2= preguntas[i].respuestaIncorrecta2)
        elif numberRamdon == 1:
            preguntasRamdon = Preguntas( pregunta=preguntas[i].pregunta,
                                         respuestaCorrecta=preguntas[i].respuestaIncorrecta1, 
                                         respuestaIncorrecta1=preguntas[i].respuestaIncorrecta2, 
                                         respuestaIncorrecta2= preguntas[i].respuestaCorrecta)     
        else:
            preguntasRamdon= preguntas[i]

        preguntasLimitadas.append(preguntasRamdon)
        i+=1     

    ## Fin Revolver las Respuestas -----------------
    context = {  
        "user": nick,
        "artificial": artificial,
        "vida" : vida,
        "preguntasLimitadas": preguntasLimitadas,
        "formulario" : formulario
      }

    if r.POST: ## No funciona :(
        print("ENTRE VIDA")
        resp = r.POST['respuesta']
        print(resp)

        vida = int(vida)
        vida = vida-10
        

        return batalla(r, nick, id, str(vida))

    return render(r, "entrenador/batalla.html", context)


class Entrenador_APIView(APIView):
    def get_object(self, pk):
        try:
            return Entrenador.objects.get(pk=pk)
        except Entrenador.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        entrenador = self.get_object(pk)
        serializer = EntrenadorSerializer(entrenador)  
        return Response(serializer.data) 