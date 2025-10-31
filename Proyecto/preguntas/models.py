from django.db import models

class TipoExamen(models.Model):
    nombre = models.CharField(max_length=45)
    def __str__(self):
        return self.nombre

class Componente(models.Model):
    nombre = models.CharField(max_length=45)
    tipo_examen = models.ManyToManyField(TipoExamen) 

class Tema(models.Model):
    nombre = models.CharField(max_length=100)
    componente = models.ForeignKey(Componente, on_delete=models.CASCADE)
    descripcion = models.TextField(null=True, blank=True)
    prioridad = models.IntegerField(null=True, blank=True)
    tema_padre = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='subtemas')
    def __str__(self):
        return self.nombre

class Grupo(models.Model):
    titulo = models.CharField(max_length=45)
    descripcion = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.titulo

class TipoPregunta(models.Model):
    nombre = models.CharField(max_length=45)

class Pregunta(models.Model):
    titulo = models.CharField(max_length=100) 
    descripcion = models.TextField() 
    imagen = models.ImageField(upload_to='preguntas_img/', null=True, blank=True)
    tema = models.ForeignKey(Tema, on_delete=models.SET_NULL, null=True)
    grupo = models.ForeignKey(Grupo, on_delete=models.SET_NULL, null=True, blank=True)
    tipo_pregunta = models.ForeignKey(TipoPregunta, on_delete=models.PROTECT)

class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta, related_name='opciones', on_delete=models.CASCADE)
    contenido = models.CharField(max_length=255) 
    imagen = models.ImageField(upload_to='opciones_imgs/', null=True, blank=True)
    puntaje = models.IntegerField(null=True, blank=True)
