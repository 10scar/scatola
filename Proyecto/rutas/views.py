from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
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
from .services import sincronizar_lecciones, actualizar_estados_lecciones   


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
    """Lista las lecciones de la ruta del usuario actual, agrupadas por tema."""
    ruta = Ruta.objects.filter(usuario=request.user).first()

    if not ruta:
        messages.warning(request, "Primero debes configurar tu ruta de aprendizaje.")
        return redirect('usuarios:ver_rutas')

    actualizar_estados_lecciones(ruta)

    # Obtenemos todas las lecciones ordenadas por número
    # Asumimos que el orden 'numero' respeta el orden de los temas (lineal)
    lecciones = (
        Leccion.objects
        .filter(ruta=ruta)
        .select_related('contenido', 'contenido__tema')
        .prefetch_related('preguntas')
        .order_by('numero')
    )

    # Agrupar por Tema manualmente
    temas_list = []
    current_tema = None
    current_group = None

    for leccion in lecciones:
        tema = leccion.contenido.tema
        
        # Si cambia el tema, guardamos el grupo anterior e iniciamos uno nuevo
        if current_tema != tema:
            if current_group:
                temas_list.append(current_group)
            
            # Obtener el componente asociado al tema a través del Temario
            from preguntas.models import Temario
            temario = Temario.objects.filter(tema=tema).select_related('componente').first()
            componente = temario.componente if temario else None
            
            current_tema = tema
            current_group = {
                'tema': tema,
                'componente': componente,  # Agregamos el componente
                'lecciones': [],
                'estado_tema': 'bloqueado' # Se calculará abajo
            }
        
        current_group['lecciones'].append(leccion)

    # Añadir el último grupo
    if current_group:
        temas_list.append(current_group)

    # Calcular estado visual de cada tema
    for group in temas_list:
        lecciones_grupo = group['lecciones']
        if not lecciones_grupo:
            continue
            
        # Completado: todas aprobadas o saltadas
        all_done = all(l.estado in [Leccion.ESTADO_APROBADA, Leccion.ESTADO_SALTADA] for l in lecciones_grupo)
        # Activo: al menos una no está bloqueada
        any_active = any(l.estado != Leccion.ESTADO_BLOQUEADA for l in lecciones_grupo)
        
        if all_done:
            group['estado_tema'] = 'completado'
        elif any_active:
            group['estado_tema'] = 'activo'
        else:
            group['estado_tema'] = 'bloqueado'

    context = {
        'ruta': ruta,
        'temas_list': temas_list,
    }
    return render(request, 'rutas/listar_lecciones.html', context)

@login_required
def ver_leccion(request, leccion_id):
    """Muestra una lección específica y permite evaluarla o saltarla."""
    leccion = get_object_or_404(
        Leccion.objects.select_related('ruta', 'contenido').prefetch_related('preguntas__opciones'),
        id=leccion_id,
        ruta__usuario=request.user
    )

    # Recalcular estados por si cambió algo en la ruta
    actualizar_estados_lecciones(leccion.ruta)
    leccion.refresh_from_db()

    if leccion.estado == Leccion.ESTADO_BLOQUEADA:
        messages.warning(request, "Esta lección está bloqueada. Completa las anteriores para desbloquearla.")
        return redirect('rutas:listar_lecciones')

    preguntas = list(leccion.preguntas.all())
    total_preguntas = len(preguntas)

    # Saber si el formulario debe mostrarse bloqueado (después de reprobar)
    bloqueado = request.GET.get("bloqueado") == "1"

    # Calcular la siguiente lección de la ruta, si existe
    siguiente_leccion = (
        Leccion.objects
        .filter(ruta=leccion.ruta, numero__gt=leccion.numero)
        .order_by("numero")
        .first()
    )

    if request.method == "POST" and leccion.estado == Leccion.ESTADO_VIGENTE:
        accion = request.POST.get("accion")

        # 1) Saltar lección
        if accion == "saltar":
            leccion.estado = Leccion.ESTADO_SALTADA
            leccion.save()
            actualizar_estados_lecciones(leccion.ruta)
            messages.info(
                request,
                f"Has saltado la lección {leccion.numero}. "
                "Podrás volver a acceder a ella más adelante desde tu ruta de aprendizaje."
            )

            # Redirigir directamente a la siguiente lección vigente, si existe
            leccion_siguiente_vigente = (
                Leccion.objects
                .filter(ruta=leccion.ruta, estado=Leccion.ESTADO_VIGENTE)
                .order_by("numero")
                .first()
            )
            if leccion_siguiente_vigente:
                return redirect('rutas:ver_leccion', leccion_id=leccion_siguiente_vigente.id)

            return redirect('rutas:listar_lecciones')

        # 2) Evaluar lección
        if accion == "evaluar":
            # Si hay menos de 2 preguntas, no vale la pena evaluar
            if total_preguntas < 2:
                messages.warning(
                    request,
                    "Esta lección aún no tiene suficientes preguntas para ser evaluada. Inténtalo más tarde."
                )
                return redirect('rutas:listar_lecciones')

            respuestas_correctas = 0
            respondidas = 0

            for pregunta in preguntas:
                campo = f"opcion_{pregunta.id}"
                opcion_id = request.POST.get(campo)
                if not opcion_id:
                    # No respondió esta pregunta → cuenta como incorrecta
                    continue

                respondidas += 1
                try:
                    opcion = pregunta.opciones.get(id=opcion_id)
                except Opcion.DoesNotExist:
                    continue

                if (opcion.puntaje or 0) > 0:
                    respuestas_correctas += 1

            if respondidas == 0:
                messages.warning(request, "No respondiste ninguna pregunta. Inténtalo nuevamente.")
                return redirect('rutas:ver_leccion', leccion_id=leccion.id)

            porcentaje = (respuestas_correctas / total_preguntas) * 100

            if porcentaje >= 50:
                leccion.estado = Leccion.ESTADO_APROBADA
                leccion.puntaje = int(porcentaje)
                leccion.save()
                actualizar_estados_lecciones(leccion.ruta)
                messages.success(
                    request,
                    f"¡Felicitaciones! Aprobaste la lección con {respuestas_correctas} "
                    f"de {total_preguntas} preguntas correctas ({porcentaje:.0f}%)."
                )
            else:
                # No cambia el estado; puede reintentar, pero bloqueamos el formulario
                leccion.puntaje = int(porcentaje)
                leccion.save()
                messages.error(
                    request,
                    f"No alcanzaste el 50%. Obtuviste {respuestas_correctas} de "
                    f"{total_preguntas} preguntas correctas ({porcentaje:.0f}%). "
                    "Puedes volver a intentarlo cuando quieras."
                )

                # Redirigir con bandera de formulario bloqueado
                url = reverse('rutas:ver_leccion', args=[leccion.id])
                return redirect(f"{url}?bloqueado=1")

            return redirect('rutas:ver_leccion', leccion_id=leccion.id)

    context = {
        'leccion': leccion,
        'preguntas': preguntas,
        'estado': leccion.estado,
        'bloqueado': bloqueado,
        'siguiente_leccion': siguiente_leccion,
    }
    return render(request, 'rutas/leccion_detalle.html', context)