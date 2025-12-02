from django.db import transaction
from preguntas.models import Pregunta, Componente, TipoExamen
from .models import PruebaDiagnostica, RespuestaDiagnostica
import random


def seleccionar_preguntas_diagnostica(num_preguntas=20, componentes_usuario=None):
    """
    Selecciona preguntas para la prueba diagnóstica distribuyendo equitativamente
    entre diferentes componentes y temas.
    
    Args:
        num_preguntas: Número de preguntas a seleccionar (default: 20)
        componentes_usuario: QuerySet o lista de Componente del usuario. 
                            Si es None, usa todos los componentes del sistema.
    """
    # Si se proporcionan componentes del usuario, usar esos; si no, usar todos
    if componentes_usuario is not None:
        componentes = list(componentes_usuario)
        componentes_ids = [c.id for c in componentes]
    else:
        componentes = list(Componente.objects.all())
        componentes_ids = [c.id for c in componentes]
    
    if not componentes:
        # Si no hay componentes, retornar preguntas aleatorias
        return list(Pregunta.objects.all()[:num_preguntas])
    
    # Obtener los IDs de los temas que están relacionados con los componentes seleccionados
    # a través de Temario. Esto asegura que solo obtenemos temas que pertenecen a estos componentes.
    from preguntas.models import Temario
    temas_ids = Temario.objects.filter(
        componente_id__in=componentes_ids
    ).values_list('tema_id', flat=True).distinct()
    
    if not temas_ids:
        # Si no hay temas, retornar lista vacía
        return []
    
    # Obtener todas las preguntas cuyos contenidos pertenezcan a los temas seleccionados
    # y que no tengan contenido nulo
    preguntas_base = Pregunta.objects.filter(
        contenido__tema_id__in=temas_ids,
        contenido__isnull=False
    ).distinct()
    
    if not preguntas_base.exists():
        return []
    
    preguntas_seleccionadas = []
    preguntas_ids_seleccionadas = set()
    
    # Convertir a lista para poder usar random.sample
    preguntas_disponibles_lista = list(preguntas_base)
    
    # Estrategia: distribuir equitativamente entre componentes
    # Primero, intentar obtener al menos 1-2 preguntas por componente
    preguntas_minimas_por_componente = max(1, num_preguntas // len(componentes))
    preguntas_restantes = num_preguntas
    
    # Fase 1: Obtener preguntas mínimas de cada componente
    for componente in componentes:
        if preguntas_restantes <= 0:
            break
        
        # Obtener temas específicos de este componente
        temas_componente_ids = Temario.objects.filter(
            componente=componente
        ).values_list('tema_id', flat=True).distinct()
        
        if not temas_componente_ids:
            continue
        
        # Obtener preguntas disponibles de este componente específico
        preguntas_disponibles = [
            p for p in preguntas_disponibles_lista
            if p.id not in preguntas_ids_seleccionadas
            and p.contenido
            and p.contenido.tema_id in temas_componente_ids
        ]
        
        if preguntas_disponibles:
            # Seleccionar aleatoriamente hasta el mínimo requerido
            cantidad_a_tomar = min(preguntas_minimas_por_componente, len(preguntas_disponibles), preguntas_restantes)
            preguntas_seleccionadas_componente = random.sample(preguntas_disponibles, cantidad_a_tomar)
            
            preguntas_seleccionadas.extend(preguntas_seleccionadas_componente)
            preguntas_ids_seleccionadas.update(p.id for p in preguntas_seleccionadas_componente)
            preguntas_restantes -= cantidad_a_tomar
    
    # Fase 2: Si aún faltan preguntas, distribuirlas equitativamente entre componentes con preguntas disponibles
    if preguntas_restantes > 0:
        # Mezclar componentes para dar variedad
        random.shuffle(componentes)
        
        while preguntas_restantes > 0:
            preguntas_agregadas_en_esta_iteracion = 0
            
            for componente in componentes:
                if preguntas_restantes <= 0:
                    break
                
                # Obtener temas específicos de este componente
                temas_componente_ids = Temario.objects.filter(
                    componente=componente
                ).values_list('tema_id', flat=True).distinct()
                
                if not temas_componente_ids:
                    continue
                
                # Obtener una pregunta más de este componente específico
                preguntas_disponibles = [
                    p for p in preguntas_disponibles_lista
                    if p.id not in preguntas_ids_seleccionadas
                    and p.contenido
                    and p.contenido.tema_id in temas_componente_ids
                ]
                
                if preguntas_disponibles:
                    pregunta_seleccionada = random.choice(preguntas_disponibles)
                    preguntas_seleccionadas.append(pregunta_seleccionada)
                    preguntas_ids_seleccionadas.add(pregunta_seleccionada.id)
                    preguntas_restantes -= 1
                    preguntas_agregadas_en_esta_iteracion += 1
            
            # Si no se agregó ninguna pregunta en esta iteración, salir
            if preguntas_agregadas_en_esta_iteracion == 0:
                break
    
    # Fase 3: Si aún faltan preguntas, completar con preguntas aleatorias de los componentes seleccionados
    if preguntas_restantes > 0:
        # Obtener preguntas adicionales solo de los temas relacionados con los componentes seleccionados
        preguntas_adicionales = [
            p for p in preguntas_disponibles_lista
            if p.id not in preguntas_ids_seleccionadas
        ][:preguntas_restantes]
        preguntas_seleccionadas.extend(preguntas_adicionales)
    
    # Mezclar las preguntas seleccionadas para que no estén agrupadas por componente
    random.shuffle(preguntas_seleccionadas)
    
    return preguntas_seleccionadas[:num_preguntas]


@transaction.atomic
def crear_prueba_diagnostica(usuario, preguntas):
    """Crea una nueva prueba diagnóstica para el usuario"""
    prueba = PruebaDiagnostica.objects.create(
        usuario=usuario,
        total_preguntas=len(preguntas)
    )
    prueba.preguntas.set(preguntas)
    return prueba


@transaction.atomic
def guardar_respuesta_diagnostica(prueba, pregunta, opcion_elegida):
    """Guarda una respuesta de la prueba diagnóstica"""
    puntaje = opcion_elegida.puntaje if opcion_elegida and opcion_elegida.puntaje else 0
    
    respuesta, created = RespuestaDiagnostica.objects.update_or_create(
        prueba=prueba,
        pregunta=pregunta,
        defaults={
            'opcion_elegida': opcion_elegida,
            'puntaje_obtenido': puntaje
        }
    )
    
    return respuesta


@transaction.atomic
def finalizar_prueba_diagnostica(prueba):
    """Finaliza la prueba diagnóstica, calcula el puntaje total y actualiza la ruta."""
    respuestas = RespuestaDiagnostica.objects.filter(prueba=prueba)
    puntaje_total = sum(r.puntaje_obtenido for r in respuestas)

    prueba.puntaje_total = puntaje_total
    prueba.completada = True
    prueba.save()

    # Generar o actualizar la ruta a partir de la diagnóstica
    from rutas.services import generar_lecciones_desde_diagnostica, actualizar_estados_lecciones
    from rutas.models import Leccion

    ruta = generar_lecciones_desde_diagnostica(prueba.usuario, prueba)

    # --- NUEVO: marcar como aprobadas las lecciones cuyos contenidos
    # hayan sido respondidos correctamente en la diagnóstica ---

    # Respuestas correctas (puntaje_obtenido > 0) con su contenido asociado
    respuestas_correctas = respuestas.select_related('pregunta__contenido').filter(
        puntaje_obtenido__gt=0,
        pregunta__contenido__isnull=False,
    )

    contenidos_aprobados_ids = {
        r.pregunta.contenido_id
        for r in respuestas_correctas
        if r.pregunta.contenido_id is not None
    }

    if contenidos_aprobados_ids:
        Leccion.objects.filter(
            ruta=ruta,
            contenido_id__in=contenidos_aprobados_ids,
        ).update(estado=Leccion.ESTADO_APROBADA)
        actualizar_estados_lecciones(ruta)

    return prueba, ruta