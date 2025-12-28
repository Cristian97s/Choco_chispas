from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):

    def create_user(self, nombre_usuario, email, password=None, **extra_fields):
        if not nombre_usuario:
            raise ValueError('nombre_usuario es obligatorio')
        if not email:
            raise ValueError('email es obligatorio')

        email = self.normalize_email(email)

        user = self.model(
            nombre_usuario=nombre_usuario,
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nombre_usuario, email, password=None, **extra_fields):
        extra_fields.setdefault('es_staff', True)
        extra_fields.setdefault('es_superusuario', True)
        extra_fields.setdefault('rol', 'ADMIN')

        return self.create_user(nombre_usuario, email, password, **extra_fields)
