"""
Formularios de la aplicación preguntas
"""

from .dashboard_admin import (
    TemaForm,
    ContenidoForm,
    TemarioAddTemasForm,
    INPUT_CLASSES
)

from .dashboard_admin_preguntas import (
    TipoPreguntaForm,
    GrupoForm,
    GrupoAddPreguntasForm,
    PreguntaForm,
    OpcionForm,
    OpcionFormSet,
)

__all__ = [
    'TemaForm',
    'ContenidoForm',
    'TemarioAddTemasForm',
    'INPUT_CLASSES',
]