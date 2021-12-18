from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.

class Pokemones(models.Model):  
    nombre = CharField (max_length=100,null= False, unique=True)
    tipo = CharField (max_length=100,null= False)
    icono = CharField (max_length=100,default='') ## sprites.front_default
    imagen = CharField (max_length=100,default='') ## sprites.other.dream_world.front_default

    moviminetoUno = CharField(max_length=200,default='Generico=25')
    moviminetoDos = CharField(max_length=200,default='Generico=25')
    moviminetoTres = CharField(max_length=200,default='Generico=25')
    moviminetoCuatro  = CharField(max_length=200,default='Generico=25')

    def __str__(self):
        return self.nombre