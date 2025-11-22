from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date, timedelta
from django.apps import apps


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
    racha = models.IntegerField(default=0)
    puntos = models.IntegerField(default=0)    
    ultima_respuesta_diaria = models.IntegerField(null=True, blank=True) # Guarda el id (pk) de la última RespuestaDiaria correcta del usuario
                                                                        #en la implementación de preguntas necesita almacenar este id.
    def __str__(self):
        return f"Perfil de {self.usuario.username}"
    
    def actualizar_racha(self, respuestas_correctas):
        """
        Actualiza la racha y los puntaje del usuario.
        """
        hoy = date.today()
        ayer = hoy - timedelta(days=1)

        # Obtener la fecha de la última respuesta diaria (si existe)
        ultima_fecha = None
        if self.ultima_respuesta_diaria:
            RespuestaDiaria = apps.get_model('rutas', 'RespuestaDiaria')
            # obtener la fecha (datetime) y convertir a date para comparar
            fecha_dt = (
                RespuestaDiaria.objects
                .filter(pk=self.ultima_respuesta_diaria)
                .values_list('fecha', flat=True)
                .first()
            )
            if fecha_dt:
                try:
                    ultima_fecha = fecha_dt.date()
                except Exception:
                    # si por alguna razón no tiene método date(), intentar comparar directamente
                    ultima_fecha = fecha_dt

        # Si ya hubo actividad hoy, no hacer nada.
        if ultima_fecha == hoy:
            return

        # Si la última actividad fue ayer, continuar la racha.
        if ultima_fecha == ayer:
            self.racha += 1
            self.puntos += 5 + (respuestas_correctas * 2)
        else:
            # Si no, iniciar la racha en 1.
            self.racha = 1
            self.puntos += 5 + (respuestas_correctas * 2)

        # No modificamos `ultima_respuesta_diaria` aquí: debe ser actualizado
        # por quien crea la RespuestaDiaria (por ejemplo la vista que procesa la respuesta).
        self.save()
    # La lógica de recordatorio se gestiona en la vista `recuerdo_racha`.