#from django.shortcuts import render
# Create your views here.
from django.db import transaction
from preguntas.models import Contenido
from rutas.models import Ruta, Leccion

from django.db import transaction
from preguntas.models import Contenido
from rutas.models import Ruta, Leccion

@transaction.atomic
def sincronizar_lecciones(ruta_id):
    ruta = Ruta.objects.get(id=ruta_id)

    # obtener temas válidos
    temas_ids = ruta.componentes.values_list(
        "temarios__tema_id", flat=True
    ).distinct()

    # obtener contenidos con sus preguntas 
    contenidos_validos = (
        Contenido.objects
        .filter(tema_id__in=temas_ids)
        .prefetch_related("pregunta_set")  
        .order_by("tema__prioridad", "id")
    )

    contenidos_ids = [c.id for c in contenidos_validos]

    # lecciones existentes por contenido
    lecciones_actuales = {
        l.contenido_id: l  
        for l in Leccion.objects.filter(ruta=ruta)
    }

    orden = 1
    for contenido in contenidos_validos:
        preguntas = list(contenido.pregunta_set.all()[:12])

        if contenido.id in lecciones_actuales:
            # actualizar lección existente
            leccion = lecciones_actuales[contenido.id]
            leccion.numero = orden
            leccion.save()

            # actualizar preguntas
            leccion.preguntas.set(preguntas)

        else:
            # crear lección nueva + asignar preguntas
            leccion = Leccion.objects.create(
                ruta=ruta,
                contenido=contenido,
                numero=orden
            )
            leccion.preguntas.set(preguntas)

        orden += 1

    # Eliminar lecciones que ya no pertenecen a los contenidos válidos
    for contenido_id, leccion in lecciones_actuales.items():
        if contenido_id not in contenidos_ids:
            leccion.delete()
    return True

@transaction.atomic
def generar_ruta_sin_diagnostica(usuario, ruta):
    """
    Genera una ruta de aprendizaje con todos los temas de los componentes seleccionados,
    sin necesidad de prueba diagnóstica. Cada lección tendrá máximo 12 preguntas.
    
    Args:
        usuario: Usuario para quien generar las lecciones
        ruta: Instancia de Ruta con los componentes ya seleccionados
    
    Returns:
        Ruta: Ruta de aprendizaje generada
    """
    # La ruta ya tiene los componentes seleccionados
    # Solo necesitamos sincronizar las lecciones (ya limitadas a 12 preguntas)
    sincronizar_lecciones(ruta.id)
    
    return ruta

@transaction.atomic
def generar_lecciones_desde_diagnostica(usuario, prueba_diagnostica):
    """
    KAN-11/KAN-8: Genera lecciones de 12 preguntas basadas en los resultados 
    de la prueba diagnóstica, seleccionando módulos según las áreas débiles.
    
    Args:
        usuario: Usuario para quien generar las lecciones
        prueba_diagnostica: Instancia de PruebaDiagnostica con los resultados
    
    Returns:
        Ruta: Ruta de aprendizaje generada o actualizada
    """
    from preguntas.models import Componente, TipoExamen
    from diagnosticos.models import RespuestaDiagnostica
    
    # Obtener o crear ruta del usuario
    ruta, created = Ruta.objects.get_or_create(usuario=usuario)
    
    # Analizar resultados de la prueba diagnóstica
    # Obtener componentes donde el estudiante tuvo bajo rendimiento
    respuestas_incorrectas = RespuestaDiagnostica.objects.filter(
        prueba=prueba_diagnostica,
        puntaje_obtenido=0
    )
    
    # Obtener componentes relacionados con las preguntas fallidas
    componentes_necesarios = Componente.objects.filter(
        temarios__tema__contenidos__pregunta__in=[
            r.pregunta for r in respuestas_incorrectas
        ]
    ).distinct()
    
    # Si no hay suficientes componentes, usar todos los disponibles
    if not componentes_necesarios.exists():
        # Obtener todos los componentes de los tipos de examen seleccionados
        tipos_examen = TipoExamen.objects.all()
        componentes_necesarios = Componente.objects.filter(tipo_examen__in=tipos_examen)
    
    # Actualizar componentes de la ruta
    ruta.componentes.set(componentes_necesarios)
    
    # Actualizar tipos de examen basados en los componentes
    tipos_examen = componentes_necesarios.values_list('tipo_examen', flat=True).distinct()
    ruta.examenes.set(tipos_examen)
    
    # Sincronizar lecciones (ya limitadas a 12 preguntas)
    sincronizar_lecciones(ruta.id)
    
    return ruta