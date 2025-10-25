from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
def hola_mundo(request):
    usuario, created = Usuario.objects.get_or_create(
    email='hola@mundo.com',
    defaults={
        'last_name': 'Guti',
        'first_name': "Oscar",
    }
    )
    # Pasar datos al template
    context = {
    'usuario': usuario,
    'mensaje': '¡Aplicación funcionando correctamente!' if created else
    '¡Usuario ya existía en la BD!',
    'es_nuevo': created
    }
    return render(request, 'hola_mundo.html', context)
