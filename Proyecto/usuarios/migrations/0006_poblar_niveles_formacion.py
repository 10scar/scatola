from django.db import migrations

def crear_niveles_formacion(apps, schema_editor):
    NivelFormacion = apps.get_model("usuarios", "NivelFormacion")

    niveles = [
        "Básica primaria",
        "Bachillerato",
        "Técnico",
        "Tecnólogo",
        "Pregrado"
    ]

    for n in niveles:
        NivelFormacion.objects.get_or_create(nombre=n)


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_alter_perfil_nivel_formacion'),  
    ]

    operations = [
        migrations.RunPython(crear_niveles_formacion),
    ]
