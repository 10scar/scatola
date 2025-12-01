from django.db import models
from usuarios.models import Usuario
from preguntas.models import Pregunta, Opcion

class PruebaDiagnostica(models.Model):
    """Creamos una nueva tabla, que se encargara de almacenar los resultados de la prueba diagnóstica del
     estudiante, y se relacionara con el usuario que la realizo. tambien se pretende que se utilice para
     construir la ruta de aprendizaje del estudiante."""
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='pruebas_diagnosticas')
    fecha = models.DateTimeField(auto_now_add=True)
    puntaje_total = models.IntegerField(default=0)
    completada = models.BooleanField(default=False)
    total_preguntas = models.IntegerField(default=0)
    preguntas = models.ManyToManyField(Pregunta, related_name='pruebas_diagnosticas')
    
    class Meta:
        ordering = ['-fecha']
        verbose_name = 'Prueba Diagnóstica'
        verbose_name_plural = 'Pruebas Diagnósticas'
    
    def __str__(self):
        return f"Prueba Diagnóstica de {self.usuario.username} - {self.fecha.date()}"


class RespuestaDiagnostica(models.Model):
    """Almacena las respuestas individuales de la prueba diagnostica, esto permitira que la ruta a crear
    se enfoque en los componentes que el estudiante tiene mas debil"""
    prueba = models.ForeignKey(PruebaDiagnostica, on_delete=models.CASCADE, related_name='respuestas')
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    opcion_elegida = models.ForeignKey(Opcion, on_delete=models.CASCADE, null=True, blank=True)
    puntaje_obtenido = models.IntegerField(default=0)
    tiempo_segundos = models.IntegerField(null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['fecha']
        unique_together = ('prueba', 'pregunta')
    
    def __str__(self):
        return f"Respuesta de {self.prueba.usuario.username} - Pregunta {self.pregunta.id}"