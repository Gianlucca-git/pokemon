from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from django import forms
from .models import Entrenador 


class EntrenadorForm(ModelForm):

    class Meta:
        model = Entrenador
        fields = '__all__'
        labels = {
    'nick' : 'Entrenador',
    'nombreCompleto' : 'Nombre',
    'region' : 'Region' ,
    'medallas' : 'Medallas' ,
    'batallas' : 'Batallas' ,
    'fechaRegistro' : 'Fecha de Inicio' 
        }