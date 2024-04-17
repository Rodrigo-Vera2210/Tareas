from rest_framework import serializers
from .models import *

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = (
            'id',
            'nombre',
            'estado'
        )

class EscribirTareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        exclude = ('id')