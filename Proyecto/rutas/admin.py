#from django.contrib import admin
# Register your models here.
from django.contrib import admin
from .models import Ruta, Leccion, RespuestaLeccion

admin.site.register(Ruta)
@admin.register(Leccion)
class LeccionAdmin(admin.ModelAdmin):
    list_display = ('id', 'ruta', 'numero', 'contenido', 'preguntas_list')

    def preguntas_list(self, obj):
        return ", ".join([p.titulo for p in obj.preguntas.all()])
admin.site.register(RespuestaLeccion)

