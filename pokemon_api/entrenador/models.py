from django.db import models
from django.db.models.fields import BooleanField, CharField, DateField, IntegerField, PositiveSmallIntegerField
from datetime import datetime
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

from pokemones.models import Pokemones

# Cada clase es una tabla :3 luego registrarlo en el admin

class Entrenador(models.Model):  
    nick   = CharField(max_length=100, unique=True)
    password = CharField (max_length=100)
    nombre = CharField (max_length=100, default='')
    region = CharField (max_length=100)
    medallas = PositiveSmallIntegerField (default=0)
    batallas = PositiveSmallIntegerField (default=0)
    fechaRegistro = CharField(max_length=100, default='') ##DateField (default=timezone.now)

    def __str__(self):
        return self.nick

class EntrenadorPokemones (models.Model): ## PREGUNTAR

    class Meta:
        unique_together = (('entrenador', 'pokemones'),)

    entrenador = models.ForeignKey(Entrenador, on_delete=models.CASCADE)
    pokemones = models.ForeignKey(Pokemones, on_delete=models.CASCADE)

    def __str__(self):
        return self.entrenador.nick + " / " + self.pokemones.nombre