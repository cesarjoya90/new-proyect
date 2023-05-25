from rest_framework import serializers
from project01.models import Persona

class AdminPersonasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ("id", "nombres", "apellidos", "correo")
        read_only = ("id", )