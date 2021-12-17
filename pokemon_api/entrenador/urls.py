from django.urls import path 
from . import views


urlpatterns = [
    path('listar', views.listar, name="listar")
    ##path('crear', views.crearEstudiante, name="crear"),
    ##path('asignaturas/<int:id>', views.listarAsignaturas, name="listar_asignaturas"),
    ##path('asignaturas/crear', views.crearAsignaturas, name="crear_asignaturas")
]