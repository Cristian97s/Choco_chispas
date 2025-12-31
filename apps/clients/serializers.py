from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"

    def validate_telefono(self, value):
        if not value.isdigit():
            raise serializers.ValidationError(
                "El telefono solo debe contener numericos"
            )
        return value