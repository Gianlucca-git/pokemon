from django.urls import path 
from . import views

urlpatterns = [
    path('listar', views.listar, name="listar"),
    path('crear', views.crear, name="crear"),
    path('pokemones/<str:nick>', views.listarPokemones, name="listar_pokemones"),
    path('pokemonesAlterna/<int:id>', views.listarPokemonesAlterno, name="listar_pokemones_alterno"),
    path('post/<int:pk>', views.Entrenador_APIView.as_view()),
]