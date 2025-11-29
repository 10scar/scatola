from django.db import models
from usuarios.models import Usuario
from preguntas.models import Pregunta, Opcion
from preguntas.models import Componente, TipoExamen, Contenido

class Ruta(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    examenes = models.ManyToManyField(TipoExamen)          
    componentes = models.ManyToManyField(Componente)       

    def __str__(self):
        return f"Ruta de {self.usuario.username}"
    
class Leccion(models.Model):
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE)
    puntaje = models.IntegerField(null=True, blank=True)
    contenido = models.ForeignKey(Contenido, on_delete=models.CASCADE, null = True)
    numero = models.PositiveIntegerField(default=1) 
    # Usa ManyToManyField para relacionar lecciones y preguntas.
    # Django creará la tabla intermedia 'lecciones_preguntas' automáticamente.
    preguntas = models.ManyToManyField(Pregunta) 

    def __str__(self):
        return f"Ruta #{self.numero} de {self.ruta.usuario.username}"

class RespuestaLeccion(models.Model):
    leccion = models.ForeignKey(Leccion, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    opcion_elegida = models.ForeignKey(Opcion, on_delete=models.CASCADE)
    puntaje_obtenido = models.IntegerField(default=0)
    fecha = models.DateTimeField(auto_now_add=True)
    tiempo_segundos = models.IntegerField(null=True, blank=True)

class RespuestaDiaria(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    opcion_elegida = models.ForeignKey(Opcion, on_delete=models.CASCADE)
    puntaje = models.IntegerField(default=0)
    fecha = models.DateTimeField(auto_now_add=True)
    tiempo_segundos = models.IntegerField(null=True, blank=True)