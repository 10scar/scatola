from django import template

register = template.Library()

@register.filter
def opciones_correctas(pregunta):
    """Filtro para contar las opciones correctas de una pregunta"""
    return pregunta.opciones.filter(puntaje__gt=0).count()
