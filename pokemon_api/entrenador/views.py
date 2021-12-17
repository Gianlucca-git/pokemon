from django.shortcuts import render
from .models import Entrenador
from .forms import EntrenadorForm
from django.shortcuts import  render, redirect

def listar(r):
    context = {
        "entrenadores": Entrenador.objects.all()
    }
    return render(r, "entrenador/listar.html", context)