from django.urls import path 
from . import views


urlpatterns = [
    path('listar', views.listar, name="listar"),
    path('crear', views.crear, name="crear"),
    path('pokemones/<int:id>', views.listarPokemones, name="listar_pokemones"),
]