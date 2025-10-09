from django.db import models

class TipoExamen(models.Model):
    nombre = models.CharField(max_length=45)

class Componente(models.Model):
    nombre = models.CharField(max_length=45)

class Tema(models.Model):
    nombre = models.CharField(max_length=45)
    componente = models.ForeignKey(Componente, on_delete=models.CASCADE)
    descripcion = models.TextField(null=True, blank=True)
    prioridad = models.IntegerField(null=True, blank=True)

class Grupo(models.Model):
    titulo = models.CharField(max_length=45)
    descripcion = models.TextField(null=True, blank=True)
    
class TipoPregunta(models.Model):
    nombre = models.CharField(max_length=45)

class Pregunta(models.Model):
    titulo = models.CharField(max_length=100) # Un poco más de 45 es usualmente mejor
    descripcion = models.TextField() # Usar TextField para textos largos
    imagen = models.ImageField(upload_to='preguntas_imgs/', null=True, blank=True)
    tipo_examen = models.ForeignKey(TipoExamen, on_delete=models.PROTECT)
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo, on_delete=models.SET_NULL, null=True)
    tipo_pregunta = models.ForeignKey(TipoPregunta, on_delete=models.PROTECT)

class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta, related_name='opciones', on_delete=models.CASCADE)
    contenido = models.CharField(max_length=255) # 50 puede ser poco
    imagen = models.ImageField(upload_to='opciones_imgs/', null=True, blank=True)
    puntaje = models.BooleanField(default=False) # Es mejor tener un booleano que un puntaje
    