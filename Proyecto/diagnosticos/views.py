from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.utils import timezone
from preguntas.models import Pregunta, Opcion
from .models import PruebaDiagnostica, RespuestaDiagnostica
from .services import (
    seleccionar_preguntas_diagnostica,
    crear_prueba_diagnostica,
    guardar_respuesta_diagnostica,
    finalizar_prueba_diagnostica
)
import json


@login_required
def iniciar_prueba(request):
    """Inicia una nueva prueba diagnóstica para el usuario"""
    # Obtener la ruta del usuario para filtrar por sus componentes seleccionados
    from rutas.models import Ruta
    try:
        ruta = Ruta.objects.get(usuario=request.user)
        componentes_usuario = ruta.componentes.all()
        
        # Verificar que tenga componentes seleccionados
        if not componentes_usuario.exists():
            return render(request, 'diagnosticos/iniciar.html', {
                'error': 'Primero debes seleccionar tus componentes de estudio en tu perfil.'
            })
    except Ruta.DoesNotExist:
        return render(request, 'diagnosticos/iniciar.html', {
            'error': 'Primero debes configurar tu ruta de aprendizaje en tu perfil.'
        })
    
    # Verificar si ya tiene una prueba completada
    prueba_existente = PruebaDiagnostica.objects.filter(
        usuario=request.user,
        completada=True
    ).first()
    
    if prueba_existente:
        # Si ya completó una prueba, mostrar opción de hacer otra
        return render(request, 'diagnosticos/iniciar.html', {
            'tiene_prueba_anterior': True,
            'prueba_anterior': prueba_existente
        })
    
    # Seleccionar preguntas para la prueba SOLO de los componentes seleccionados
    preguntas = seleccionar_preguntas_diagnostica(
        num_preguntas=20, 
        componentes_usuario=componentes_usuario
    )
    
    if not preguntas:
        return render(request, 'diagnosticos/iniciar.html', {
            'error': 'No hay suficientes preguntas disponibles para la prueba diagnóstica en los componentes seleccionados.'
        })
    
    # Crear prueba diagnóstica
    prueba = crear_prueba_diagnostica(request.user, preguntas)
    
    # Guardar preguntas en la sesión o en la prueba (usaremos un campo ManyToMany si es necesario)
    # Por ahora, redirigir a la primera pregunta
    return redirect('diagnosticos:ver_pregunta', prueba_id=prueba.id, pregunta_num=1)


@login_required
def ver_pregunta(request, prueba_id, pregunta_num):
    """Muestra una pregunta específica de la prueba diagnóstica"""
    prueba = get_object_or_404(PruebaDiagnostica, id=prueba_id, usuario=request.user)

    # Preguntas que realmente pertenecen a esta prueba
    preguntas_prueba = list(prueba.preguntas.all().order_by('id'))
    total_preguntas = len(preguntas_prueba)

    if pregunta_num < 1 or pregunta_num > total_preguntas:
        # Si el número está fuera de rango, finalizar la prueba
        return redirect('diagnosticos:finalizar', prueba_id=prueba.id)

    pregunta_actual = preguntas_prueba[pregunta_num - 1]

    respuesta_existente = RespuestaDiagnostica.objects.filter(
        prueba=prueba,
        pregunta=pregunta_actual
    ).first()

    opciones = Opcion.objects.filter(pregunta=pregunta_actual)

    context = {
        'prueba': prueba,
        'pregunta': pregunta_actual,
        'opciones': opciones,
        'pregunta_num': pregunta_num,
        'total_preguntas': total_preguntas,
        'respuesta_existente': respuesta_existente,
    }

    return render(request, 'diagnosticos/pregunta.html', context)


@login_required
@require_http_methods(["POST"])
def guardar_respuesta(request, prueba_id):
    """Guarda la respuesta de una pregunta en la prueba diagnóstica"""
    try:
        prueba = get_object_or_404(PruebaDiagnostica, id=prueba_id, usuario=request.user)
        data = json.loads(request.body)
        pregunta_id = data.get('pregunta_id')
        opcion_id = data.get('opcion_id')
        pregunta_num = data.get('pregunta_num', 1)
        
        pregunta = get_object_or_404(Pregunta, id=pregunta_id)
        opcion = get_object_or_404(Opcion, id=opcion_id, pregunta=pregunta)
        
        # Guardar respuesta
        guardar_respuesta_diagnostica(prueba, pregunta, opcion)
        
        # Determinar siguiente pregunta
        siguiente_num = pregunta_num + 1
        
        if siguiente_num > prueba.total_preguntas:
            # Finalizar prueba
            return JsonResponse({
                'success': True,
                'completed': True,
                'redirect_url': f'/diagnosticos/{prueba.id}/finalizar/'
            })
        
        return JsonResponse({
            'success': True,
            'completed': False,
            'redirect_url': f'/diagnosticos/{prueba.id}/pregunta/{siguiente_num}/'
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@login_required
def finalizar_prueba(request, prueba_id):
    """Finaliza la prueba diagnóstica y muestra los resultados"""
    prueba = get_object_or_404(PruebaDiagnostica, id=prueba_id, usuario=request.user)
    
    if not prueba.completada:
        # Finalizar la prueba
        prueba, ruta = finalizar_prueba_diagnostica(prueba)
    
    # Obtener estadísticas
    respuestas = RespuestaDiagnostica.objects.filter(prueba=prueba)
    total_respuestas = respuestas.count()
    respuestas_correctas = respuestas.filter(puntaje_obtenido__gt=0).count()
    porcentaje = (respuestas_correctas / total_respuestas * 100) if total_respuestas > 0 else 0
    
    context = {
        'prueba': prueba,
        'total_respuestas': total_respuestas,
        'respuestas_correctas': respuestas_correctas,
        'porcentaje': round(porcentaje, 2),
        'ruta_generada': True,
    }
    
    return render(request, 'diagnosticos/resultados.html', context)