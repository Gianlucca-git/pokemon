from django.urls import path 
from . import views

urlpatterns = [
    path('login', views.login, name="login"),
    path('crear', views.crear, name="crear"),
    path('listar', views.listar, name="listar"),
    path('pokemones/<str:nick>', views.listarPokemones, name="listar_pokemones"),
    path('pokemonesAlterna/<int:id>', views.listarPokemonesAlterno, name="listar_pokemones_alterno"),
    path('post/<int:pk>', views.Entrenador_APIView.as_view()),
]