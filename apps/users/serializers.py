from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = (
            'id',
            'nombre_usuario',
            'email',
            'rol',
            'esta_activo',
            'fecha_registro',
        )
        read_only_fields = ('id', 'fecha_registro')

class UsuarioCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = (
            'nombre_usuario',
            'email',
            'password',
            'rol',
        )

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Usuario(**validated_data)
        user.set_password(password)
        user.save()
        return user
