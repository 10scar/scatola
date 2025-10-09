from django.db import models
from usuarios.models import Usuario
from preguntas.models import Pregunta, Opcion

class Ruta(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    

class Leccion(models.Model):
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE)
    puntaje = models.IntegerField(null=True, blank=True)
    # Usa ManyToManyField para relacionar lecciones y preguntas.
    # Django creará la tabla intermedia 'lecciones_preguntas' automáticamente.
    preguntas = models.ManyToManyField(Pregunta) 

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