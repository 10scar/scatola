from django.contrib import admin
from .models import Rol, NivelFormacion, Usuario, Perfil

# Register your models here.
admin.site.register(Rol)
admin.site.register(NivelFormacion)
admin.site.register(Usuario)
admin.site.register(Perfil)
