from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from django import forms
from .models import Entrenador, EntrenadorPokemones 


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

class EntrenadorPokemonesForm(ModelForm):

    class Meta:
        model = EntrenadorPokemones
        fields = '__all__'
        labels = {
            'entrenador':'Entrenador',
            'pokemones':'Pokemon'
        }

class LoginForm(ModelForm):

    class Meta:
        model = Entrenador
        exclude = ['medallas','batallas','fechaRegistro', 'nombre', 'region', 'numeroPokemones']
        labels = {
    'nick' : 'Entrenador',
    'password' : 'Contraseña'
        }