# ============================================
# FORMULARIOS PARA GESTIÓN DE PREGUNTAS, GRUPOS Y TIPOS
# ============================================
from django import forms
from django.forms import inlineformset_factory
from django.db import models
from preguntas.models import Pregunta, Opcion, TipoPregunta, Grupo, Contenido, TipoExamen

# Clases CSS reutilizables para inputs
INPUT_CLASSES = 'mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500'
TEXTAREA_CLASSES = 'mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500'
SELECT_CLASSES = 'mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500'


# ============================================
# FORMULARIOS PARA TIPO DE PREGUNTA
# ============================================

class TipoPreguntaForm(forms.ModelForm):
    """Formulario para crear y editar Tipos de Pregunta"""
    class Meta:
        model = TipoPregunta
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Ej: Selección Múltiple, Verdadero/Falso, etc.'
            }),
        }
        labels = {
            'nombre': 'Nombre del Tipo de Pregunta',
        }


# ============================================
# FORMULARIOS PARA GRUPOS
# ============================================

class GrupoForm(forms.ModelForm):
    """Formulario para crear y editar Grupos de Preguntas"""
    class Meta:
        model = Grupo
        fields = ['titulo', 'descripcion']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Ej: Comprensión de Lectura - Texto 1'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': TEXTAREA_CLASSES,
                'rows': '5',
                'placeholder': 'Descripción del grupo, texto base, contexto, etc...'
            }),
        }
        labels = {
            'titulo': 'Título del Grupo',
            'descripcion': 'Descripción / Texto Base',
        }


class GrupoAddPreguntasForm(forms.Form):
    """Formulario para agregar múltiples preguntas existentes a un grupo"""
    buscar = forms.CharField(
        label='Buscar pregunta',
        required=False,
        widget=forms.TextInput(attrs={
            'class': INPUT_CLASSES,
            'placeholder': 'Buscar por título o descripción...',
            'id': 'buscar-pregunta'
        })
    )
    
    preguntas = forms.ModelMultipleChoiceField(
        label='Selecciona las preguntas',
        queryset=Pregunta.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'form-checkbox h-4 w-4 text-blue-600'
        }),
        required=False
    )
    
    def __init__(self, *args, **kwargs):
        grupo = kwargs.pop('grupo', None)
        busqueda = kwargs.pop('busqueda', '')
        super().__init__(*args, **kwargs)
        
        # Excluir preguntas que ya están en el grupo
        queryset = Pregunta.objects.select_related('tipo_pregunta', 'contenido', 'tipo_examen')
        
        if grupo:
            queryset = queryset.exclude(grupo=grupo)
        
        # Filtrar por búsqueda
        if busqueda:
            queryset = queryset.filter(
                models.Q(titulo__icontains=busqueda) |
                models.Q(descripcion__icontains=busqueda)
            )
        
        self.fields['preguntas'].queryset = queryset.order_by('-id')


# ============================================
# FORMULARIOS PARA PREGUNTAS Y OPCIONES
# ============================================

class PreguntaForm(forms.ModelForm):
    """Formulario para crear y editar Preguntas"""
    class Meta:
        model = Pregunta
        fields = ['titulo', 'descripcion', 'imagen', 'tipo_pregunta', 'tipo_examen', 'contenido', 'grupo']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Título breve de la pregunta'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': TEXTAREA_CLASSES,
                'rows': '4',
                'placeholder': 'Enunciado completo de la pregunta...'
            }),
            'imagen': forms.FileInput(attrs={
                'class': 'file-input file-input-bordered w-full',
                'accept': 'image/*'
            }),
            'tipo_pregunta': forms.Select(attrs={
                'class': SELECT_CLASSES,
            }),
            'tipo_examen': forms.Select(attrs={
                'class': SELECT_CLASSES,
            }),
            'contenido': forms.Select(attrs={
                'class': SELECT_CLASSES,
            }),
            'grupo': forms.Select(attrs={
                'class': SELECT_CLASSES,
            }),
        }
        labels = {
            'titulo': 'Título de la Pregunta',
            'descripcion': 'Enunciado',
            'imagen': 'Imagen (opcional)',
            'tipo_pregunta': 'Tipo de Pregunta',
            'tipo_examen': 'Tipo de Examen (opcional)',
            'contenido': 'Contenido Asociado (opcional)',
            'grupo': 'Grupo (opcional)',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Hacer campos opcionales según el modelo
        self.fields['tipo_examen'].required = False
        self.fields['contenido'].required = False
        self.fields['grupo'].required = False
        self.fields['imagen'].required = False
        
        # Ordenar los querysets
        self.fields['contenido'].queryset = Contenido.objects.select_related('tema').order_by('tema__nombre', 'titulo')
        self.fields['grupo'].queryset = Grupo.objects.order_by('titulo')


class OpcionForm(forms.ModelForm):
    """Formulario para crear y editar Opciones de una Pregunta"""
    es_correcta = forms.BooleanField(
        required=False,
        label='¿Es la opción correcta?',
        widget=forms.CheckboxInput(attrs={
            'class': 'checkbox checkbox-primary'
        })
    )
    
    class Meta:
        model = Opcion
        fields = ['contenido', 'imagen', 'puntaje']
        widgets = {
            'contenido': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Texto de la opción'
            }),
            'imagen': forms.FileInput(attrs={
                'class': 'file-input file-input-bordered file-input-sm w-full',
                'accept': 'image/*'
            }),
            'puntaje': forms.HiddenInput(),
        }
        labels = {
            'contenido': 'Texto de la Opción',
            'imagen': 'Imagen (opcional)',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['imagen'].required = False
        
        # Si la opción existe y tiene puntaje 1, marcar como correcta
        if self.instance.pk and self.instance.puntaje == 1:
            self.fields['es_correcta'].initial = True


# Formset para gestionar múltiples opciones inline
OpcionFormSet = inlineformset_factory(
    Pregunta,
    Opcion,
    form=OpcionForm,
    extra=4,  # Mostrar 4 opciones vacías por defecto
    min_num=2,  # Mínimo 2 opciones
    max_num=6,  # Máximo 6 opciones
    validate_min=True,
    can_delete=True,
    widgets={
        'DELETE': forms.CheckboxInput(attrs={
            'class': 'checkbox checkbox-error'
        })
    }
)
