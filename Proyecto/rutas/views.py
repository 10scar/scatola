from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from preguntas.models import Pregunta, Opcion
from usuarios.models import Perfil
from .models import RespuestaDiaria
import random
import json
from django.utils import timezone
from django.contrib import messages
from .models import Ruta, Leccion




@login_required
def preguntas_diarias_view(request):
    """Muestra una pregunta diaria no respondida aún por el usuario en el día actual.

    En vez de depender de la sesión, consultamos la tabla `RespuestaDiaria` y
    mostramos la primera pregunta no respondida (aleatoria) para el usuario.
    Si el usuario ya completó 6 preguntas, devolvemos la pantalla de completado.
    """
    hoy = timezone.localdate()

    # Preguntas respondidas hoy (por pregunta id)
    respuestas_hoy_qs = RespuestaDiaria.objects.filter(usuario=request.user, fecha__date=hoy)
    id_respuestas_contestadas = list(respuestas_hoy_qs.values_list('opcion_elegida__pregunta', flat=True))
    id_respuestas_contestadas = [int(x) for x in set(id_respuestas_contestadas) if x is not None]
    conteo_respuestas_contestadas = len(id_respuestas_contestadas)

    if conteo_respuestas_contestadas >= 6:
        return render(request, 'preguntas_diarias.html', {
            'completado': True,
            'total': conteo_respuestas_contestadas,
        })

    # Preguntas disponibles sin ser contestadas hoy
    preguntas_faltantes = Pregunta.objects.exclude(id__in=id_respuestas_contestadas)
    if not preguntas_faltantes.exists():
        # No hay preguntas disponibles
        return render(request, 'preguntas_diarias.html', {
            'error': 'No hay suficientes preguntas en el banco'
        })

    # Elegir una pregunta para mostrar (random)
    pregunta = random.choice(list(preguntas_faltantes))

    context = {
        'pregunta': pregunta,
        'opciones': Opcion.objects.filter(pregunta=pregunta),
        'indice_actual': conteo_respuestas_contestadas + 1,
        'total_preguntas': 6,
    }

    return render(request, 'preguntas_diarias_item.html', context)


@login_required
@require_http_methods(["POST"])
def guardar_respuesta_diaria(request):
    """Guarda la respuesta actual y devuelve si ya se completó el set diario.
    Evita duplicados revisando si el usuario ya respondió la misma pregunta hoy.
    """
    try:
        data = json.loads(request.body)
        opcion_id = data.get('opcion_id')
        opcion = Opcion.objects.get(id=opcion_id)
        pregunta_id = opcion.pregunta_id

        hoy = timezone.localdate()
        # Evitar respuestas duplicadas para la misma pregunta hoy
        duplicate_exists = RespuestaDiaria.objects.filter(
            usuario=request.user,
            opcion_elegida__pregunta=pregunta_id,
            fecha__date=hoy
        ).exists()

        if duplicate_exists:
            # Si ya respondió, devolver info sobre si está completado
            conteo_respuestas_contestadas = RespuestaDiaria.objects.filter(usuario=request.user, fecha__date=hoy).count()
            completed = conteo_respuestas_contestadas >= 6
            return JsonResponse({
                'success': True,
                'duplicate': True,
                'completed': completed,
                'redirect_url': '/preguntas-diarias/'
            })

        respuesta = RespuestaDiaria.objects.create(
            usuario=request.user,
            opcion_elegida=opcion,
            puntaje=opcion.puntaje if opcion.puntaje else 0
        )

        # Actualizar perfil si la respuesta fue correcta
        try:
            if respuesta.puntaje and respuesta.puntaje > 0:
                perfil, _ = Perfil.objects.get_or_create(usuario=request.user)
                perfil.actualizar_racha(respuestas_correctas=1)
                perfil.ultima_respuesta_diaria = respuesta.id
                perfil.save()
        except Exception:
            pass

        # Contar cuántas respuestas tiene hoy
        conteo_respuestas_contestadas = RespuestaDiaria.objects.filter(usuario=request.user, fecha__date=hoy).count()
        completed = conteo_respuestas_contestadas >= 6
        return JsonResponse({
            'success': True,
            'puntaje': respuesta.puntaje,
            'es_correcta': respuesta.puntaje > 0,
            'completed': completed,
            'redirect_url': '/preguntas-diarias/'
        })
    except Opcion.DoesNotExist:
        return JsonResponse({'error': 'Opción no válida'}, status=400)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Datos inválidos'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@login_required
def listar_lecciones(request):
    """Lista las lecciones de la ruta del usuario actual."""
    ruta = Ruta.objects.filter(usuario=request.user).first()

    if not ruta:
        messages.warning(request, "Primero debes configurar tu ruta de aprendizaje.")
        return redirect('usuarios:ver_rutas')

    lecciones = (
        Leccion.objects
        .filter(ruta=ruta)
        .select_related('contenido', 'contenido__tema')
        .prefetch_related('preguntas')
        .order_by('numero')
    )

    context = {
        'ruta': ruta,
        'lecciones': lecciones,
    }
    return render(request, 'rutas/listar_lecciones.html', context)
