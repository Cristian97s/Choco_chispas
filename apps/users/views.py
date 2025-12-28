from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Usuario
from .serializers import UsuarioSerializer, UsuarioCreateSerializer
from .permissions import IsAdmin

# Create your views here.

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin]

    def get_serializer_class(self):
        if self.action == 'create':
            return UsuarioCreateSerializer
        return UsuarioSerializer
