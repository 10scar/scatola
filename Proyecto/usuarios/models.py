from django.contrib.auth.models import AbstractUser
from django.db import models


class NivelFormacion(models.Model):
    nombre = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre

# Extiende el usuario de Django para añadir los campos
class Usuario(AbstractUser):
    def __str__(self):
        return self.username

# El perfil se relaciona 1 a 1 con el usuario.
class Perfil(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    nivel_formacion = models.ForeignKey(NivelFormacion, on_delete=models.SET_NULL, blank = True, null=True)
    institucion = models.CharField(max_length=45, null=True, blank=True)
    edad = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Perfil de {self.usuario.username}"