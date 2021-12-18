from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from django import forms

from preguntas.models import Preguntas
from .models import Entrenador, EntrenadorArticialPokemones 


class EntrenadorForm(ModelForm):

    class Meta:
        model = Entrenador
        exclude = ['medallas','batallas','fechaRegistro']
        labels = {
    'nick' : 'Entrenador',
    'nombre' : 'Nombre',
    'region' : 'Region' ,
    'password' : 'Contraseña'
        }

class EntrenadorArticialPokemonesForm(ModelForm):

    class Meta:
        model = EntrenadorArticialPokemones
        fields = '__all__'
        labels = {
            'entrenador':'Entrenador',
            'pokemon':'Pokemon'
        }

class LoginForm(ModelForm):

    class Meta:
        model = Entrenador
        exclude = ['medallas','batallas','fechaRegistro', 'nombre', 'region', 'numeroPokemones']
        labels = {
    'nick' : 'Entrenador',
    'password' : 'Contraseña'
        }

class BatallaForm(ModelForm):

    class Meta:
        model = Preguntas
        exclude = ['pregunta','respuestaIncorrecta1','respuestaIncorrecta2']
        labels = {
    'respuestaCorrecta' : 'Contestar'
        }