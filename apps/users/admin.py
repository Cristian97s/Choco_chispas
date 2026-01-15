from django.contrib import admin
from .models import Usuario
from simple_history.admin import SimpleHistoryAdmin

@admin.register(Usuario)
class UsuarioAdmin(SimpleHistoryAdmin):
    # Columnas que se verán en el listado de usuarios
    list_display = ('nombre_usuario', 'email', 'rol', 'esta_activo', 'es_staff', 'fecha_registro')
    
    # Filtros laterales para facilitar la búsqueda
    list_filter = ('rol', 'esta_activo', 'es_staff')
    
    # Campos por los que se puede buscar
    search_fields = ('nombre_usuario', 'email')
    
    # Orden predeterminado (por fecha de registro, el más reciente primero)
    ordering = ('-fecha_registro',)

    # Organización del formulario de edición en secciones (Fieldsets)
    fieldsets = (
        ('Información de Cuenta', {
            'fields': ('nombre_usuario', 'password', 'email', 'rol')
        }),
        ('Permisos y Estado', {
            'fields': ('esta_activo', 'es_staff', 'es_superusuario', 'groups', 'user_permissions')
        }),
        ('Fechas Importantes', {
            'fields': ('ultimo_inicio_sesion', 'fecha_registro')
        }),
    )

    # Campos que solo son de lectura (para evitar errores)
    readonly_fields = ('fecha_registro', 'ultimo_inicio_sesion')

    # Configuración para que el historial sea visible en el admin
    history_list_display = ['rol', 'esta_activo']