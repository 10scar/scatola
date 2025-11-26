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
        preguntas = contenido.pregunta_set.all()  

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

    # desactivar lecciones que ya no pertenecen a los contenidos válidos
    for contenido_id, leccion in lecciones_actuales.items():
        if contenido_id not in contenidos_ids:
            leccion.activa = False
            leccion.save()

    return True