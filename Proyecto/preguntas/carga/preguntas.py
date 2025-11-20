from preguntas.models import TipoPregunta, Contenido, Grupo, Pregunta, Opcion
import preguntas.carga.preguntas_data as preguntas_data_module


def poblar_preguntas_desde_temario():
    tipo_om, _ = TipoPregunta.objects.get_or_create(nombre="Opción múltiple")

    # 1. Crear/obtener grupos
    grupos = {}
    for g in preguntas_data_module.GRUPOS_DATA:
        grupo_obj, _ = Grupo.objects.get_or_create(
            titulo=g["titulo"],
            defaults={"descripcion": g.get("descripcion", "")},
        )
        grupos[g["codigo"]] = grupo_obj

    # 2. Aplanar la lista de preguntas (puede contener listas anidadas)
    preguntas_flat = []
    for item in preguntas_data_module.PREGUNTAS_DATA:
        if isinstance(item, list):
            preguntas_flat.extend(item)
        else:
            preguntas_flat.append(item)

    # 3. Crear preguntas y opciones
    
    for q in preguntas_flat:
        contenido = Contenido.objects.get(titulo=q["contenido_titulo"])
        grupo_obj = grupos.get(q.get("grupo_codigo")) if q.get("grupo_codigo") else None

        pregunta = Pregunta.objects.create(
            titulo=q["titulo"],
            descripcion=q["descripcion"],
            contenido=contenido,
            grupo=grupo_obj,
            tipo_pregunta=tipo_om,
            tipo_examen=None,  
        )

        for op in q["opciones"]:
            Opcion.objects.create(
                pregunta=pregunta,
                contenido=op["texto"],
                puntaje=op.get("puntaje", 0),
            )
        
        print(f"✓ Pregunta creada: {pregunta.titulo}")

    print(f"\n{'='*60}")
    print(f"Resumen:")
    print(f"  - Grupos creados: {len(grupos)}")
    print(f"  - Preguntas creadas: 100")
    print(f"{'='*60}")
