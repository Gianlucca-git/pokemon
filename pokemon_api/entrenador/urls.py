from django.urls import path 
from . import views

urlpatterns = [
    path('login', views.login, name="login"),
    path('crear', views.crear, name="crear"),
    path('listar', views.listar, name="listar"),
    path('listarArtificiales', views.listarArtificiales, name="listar_artificiales"),
    path('pokemones/<str:nick>', views.listarPokemones, name="listar_pokemones"),
    path('batalla/<str:nick>/<int:id>/<int:vida>', views.batalla, name="batalla"),
    path('pokemonesDefault/<int:id>', views.listarPokemonesDefault, name="listar_pokemones_default"),
    path('post/<int:pk>', views.Entrenador_APIView.as_view()),
]