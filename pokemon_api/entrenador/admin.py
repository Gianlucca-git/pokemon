from django.contrib import admin
from .models import Artificial, Entrenador, EntrenadorArticialPokemones

admin.site.register(Entrenador)
admin.site.register(EntrenadorArticialPokemones)
admin.site.register(Artificial)