"""
Generated migration to remove the historic `ultima_actividad_racha` field from Perfil.
This migration is intended to be applied as a no-op on the database because the
column was already dropped manually; after creating it we'll mark it as applied
with `--fake`.
"""
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("usuarios", "0005_perfil_puntos_perfil_racha_and_more"),
    ]

    # Este migration se creó para eliminar la columna que ya fue removida manualmente en la BD.
    # Para evitar conflictos de estado al recargar las migraciones, dejamos la operación vacía.
    # La migración fue marcada como aplicada con --fake en la base de datos.
    operations = []
