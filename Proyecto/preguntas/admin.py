from django.contrib import admin
from .models import TipoExamen,Componente,TipoPregunta, Pregunta, Tema,Opcion,Grupo

admin.site.register(TipoExamen)
admin.site.register(Componente)
admin.site.register(TipoPregunta)
admin.site.register(Tema)
admin.site.register(Grupo)
admin.site.register(Pregunta)
admin.site.register(Opcion)

# Register your models here.
