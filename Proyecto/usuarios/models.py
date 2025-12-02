from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import timedelta
from django.utils import timezone
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
        # Usar la fecha local de Django para evitar desajustes por UTC
        hoy = timezone.localdate()
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
                    # si es datetime con timezone, convertir a hora local
                    try:
                        if timezone.is_aware(fecha_dt):
                            fecha_local = timezone.localtime(fecha_dt)
                        else:
                            fecha_local = fecha_dt
                        ultima_fecha = fecha_local.date()
                    except Exception:
                        ultima_fecha = fecha_dt
                except Exception:
                    ultima_fecha = None

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

    def reiniciar_racha_si_vieja(self, threshold_days=2):
        """Reinicia la racha a 0 si la última respuesta fue hace >= threshold_days.

        Este método solo cambia el campo `racha`; no modifica `ultima_respuesta_diaria`.
        """
        if not self.ultima_respuesta_diaria:
            return
        RespuestaDiaria = apps.get_model('rutas', 'RespuestaDiaria')
        fecha_dt = (
            RespuestaDiaria.objects
            .filter(pk=self.ultima_respuesta_diaria)
            .values_list('fecha', flat=True)
            .first()
        )
        if not fecha_dt:
            return
        try:
            if timezone.is_aware(fecha_dt):
                fecha_local = timezone.localtime(fecha_dt)
            else:
                fecha_local = fecha_dt
            ultima_fecha = fecha_local.date()
        except Exception:
            ultima_fecha = fecha_dt

        if not ultima_fecha:
            return
        hoy = timezone.localdate()
        try:
            dias = (hoy - ultima_fecha).days
        except Exception:
            return
        if dias >= threshold_days:
            self.racha = 0
            self.save()