from django.db import models

class TipoExamen(models.Model):
    nombre = models.CharField(max_length=45)
    def __str__(self):
        return self.nombre

class Componente(models.Model):
    prioridad = models.IntegerField(null=True, blank=True)
    nombre = models.CharField(max_length=45)
    tipo_examen = models.ForeignKey(TipoExamen,on_delete=models.CASCADE,null=True, blank=True)
    def __str__(self):
        return self.nombre

class Tema(models.Model):
    nombre = models.CharField(max_length=100)
    componente = models.ForeignKey(Componente, on_delete=models.CASCADE)
    descripcion = models.TextField(null=True, blank=True)
    prioridad = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.nombre
class Temario(models.Model):
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)
    componente = models.ForeignKey(Componente, on_delete=models.CASCADE)

class Contenido(models.Model):
    tema = models.ForeignKey(Tema, related_name='contenidos', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField(help_text="Contenido explicativo detallado.")
    icono = models.CharField(max_length=50, null=True, blank=True)
    padre_id = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='hijos')

    def __str__(self):
        return f"{self.titulo} (Tema: {self.tema.nombre})"

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
    contenido = models.ForeignKey(Contenido, on_delete=models.SET_NULL, null=True)
    grupo = models.ForeignKey(Grupo, on_delete=models.SET_NULL, null=True, blank=True)
    tipo_pregunta = models.ForeignKey(TipoPregunta, on_delete=models.PROTECT)
    tipo_examen = models.ForeignKey(TipoExamen, on_delete=models.CASCADE, null=True, blank=True)

class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta, related_name='opciones', on_delete=models.CASCADE)
    contenido = models.CharField(max_length=255) 
    imagen = models.ImageField(upload_to='opciones_imgs/', null=True, blank=True)
    puntaje = models.IntegerField(null=True, blank=True)
