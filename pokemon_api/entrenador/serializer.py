from django.db.models import fields
from rest_framework import serializers
from .models import Entrenador

class EntrenadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrenador
        fields = (
            'id', 'nick', 'password', 'nombre', 'region', 'medallas',
            'batallas', 'fechaRegistro',
        )
