from django.db import models
from django.db.models.fields import BooleanField, CharField, DateField, IntegerField
from datetime import datetime
from django.utils import timezone
# Cada clase es una tabla :3 luego registrarlo en el admin

class Entrenador(models.Model):  
    nick   = CharField(max_length=100, unique=True)
    password = CharField (max_length=100)
    nombre = CharField (max_length=100, default='')
    region = CharField (max_length=100)
    medallas = IntegerField (default=0)
    batallas = IntegerField (default=0)
    fechaRegistro = DateField (default=timezone.now)

    def __str__(self):
        return self.nick + ' / ' +  self.nombre