from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from simple_history.models import HistoricalRecords

from .managers import UserManager

# Create your models here.
class Usuario (AbstractBaseUser, PermissionsMixin):
    ROL_ADMIN = 'ADMIN'
    ROL_VENDEDOR = 'VENDEDOR'
    ROL_PRODUCCION = 'PRODUCCION'

    ROL_CHOICES = (
        (ROL_ADMIN, 'Administrador'),
        (ROL_VENDEDOR,'Vendedor'),
        (ROL_PRODUCCION, 'Produccion'),
    )

    nombre_usuario = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    rol = models.CharField(max_length=20, choices=ROL_CHOICES, default=ROL_VENDEDOR)
    esta_activo = models.BooleanField(default=True)
    es_staff = models.BooleanField(default=False)
    es_superusuario = models.BooleanField(default=False)
    ultimo_inicio_sesion = models.DateTimeField(null=True, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    history = HistoricalRecords()

    objects = UserManager()

    USERNAME_FIELD = 'nombre_usuario'
    REQUIRED_FIELDS = ['email']

    class Meta:
        db_table = 'usuario'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.nombre_usuario
    
    @property
    def is_staff(self):
        return self.es_staff

    @property
    def is_superuser(self):
        return self.es_superusuario

    @property
    def is_active(self):
        return self.esta_activo
