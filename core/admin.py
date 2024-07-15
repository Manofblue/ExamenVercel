from django.contrib import admin
from .models import *
from django.contrib.admin import ModelAdmin
from admin_confirm import AdminConfirmMixin


# Register your models here.

class ProductoObra(AdminConfirmMixin,admin.ModelAdmin):
    list_display=["id_obra","nombre", "precio","tipo","artista"]
    list_editable=["precio"]
    search_fields=["nombre"]
    list_filter=["tipo"]
    confirm_change = True
    confirmation_fields = ['nombre', 'precio','descripcion','historia','tecnica_usada','tipo','artista']

class DetalleEmpleado(AdminConfirmMixin,admin.ModelAdmin):
    list_display=["rut","nombre","apellido","tipo"]
    confirm_change = True
    confirmation_fields = ['rut', 'nombre','apellido','edad','direccion','telefono','genero','tipo']
    
class DetalleContacto(admin.ModelAdmin):
    list_display=["nombre","correo","tipo_consulta"]


admin.site.register(Obra,ProductoObra)
admin.site.register(TipoObra)
admin.site.register(Empleado,DetalleEmpleado)
admin.site.register(TipoEmpleado)
admin.site.register(TipoGenero)
admin.site.register(Contacto,DetalleContacto)

