from django.db import models
from usuarios.models import Usuario
from preguntas.models import TipoExamen, Pregunta, Opcion

class Simulacro(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_examen = models.ForeignKey(TipoExamen, on_delete=models.PROTECT)
    tiempo_minutos = models.IntegerField(default=0)
    preguntas = models.ManyToManyField(Pregunta) # De nuevo, ManyToMany es perfecto aquí.

class IntentoSimulacro(models.Model):
    simulacro = models.ForeignKey(Simulacro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    fecha_fin = models.DateTimeField(null=True, blank=True)
    puntaje_total = models.IntegerField(null=True, blank=True)

class RespuestaIntento(models.Model):
    intento = models.ForeignKey(IntentoSimulacro, on_delete=models.CASCADE, related_name='respuestas')
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    opcion_elegida = models.ForeignKey(Opcion, on_delete=models.CASCADE)
    tiempo_segundos = models.IntegerField(null=True, blank=True)