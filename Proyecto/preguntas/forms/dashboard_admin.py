# ============================================
# FORMULARIOS PARA GESTIÓN DE TEMAS Y CONTENIDOS
# ============================================
from django import forms 
from preguntas.models import Tema, Contenido, Componente, Temario
# Clases CSS reutilizables para inputs
INPUT_CLASSES = 'mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500'

class TemaForm(forms.ModelForm):
    """Formulario para crear y editar Temas"""
    class Meta:
        model = Tema
        fields = ['nombre', 'prioridad', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Ej: Pensamiento Numérico y Aritmética'
            }),
            'prioridad': forms.NumberInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': '1',
                'min': '1'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
                'rows': '4',
                'placeholder': 'Descripción detallada del tema...'
            }),
        }
        labels = {
            'nombre': 'Nombre del Tema',
            'prioridad': 'Prioridad',
            'descripcion': 'Descripción'
        }

class ContenidoForm(forms.ModelForm):
    """Formulario para crear y editar Contenidos de un Tema"""
    class Meta:
        model = Contenido
        fields = ['titulo', 'descripcion', 'icono', 'padre_id']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Ej: Conjuntos Numéricos y Operaciones'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
                'rows': '5',
                'placeholder': 'Descripción detallada del contenido...'
            }),
            'icono': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Ej: 📊 (opcional)'
            }),
            'padre_id': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
        }
        labels = {
            'titulo': 'Título del Contenido',
            'descripcion': 'Descripción',
            'icono': 'Icono (opcional)',
            'padre_id': 'Contenido Padre (opcional)'
        }

    def __init__(self, *args, **kwargs):
        tema = kwargs.pop('tema', None)
        super().__init__(*args, **kwargs)
        
        # Filtrar contenidos padre solo del mismo tema
        if tema:
            self.fields['padre_id'].queryset = Contenido.objects.filter(tema=tema)
            self.fields['padre_id'].required = False


# ============================================
# FORMULARIOS PARA GESTIÓN DE TEMARIOS
# ============================================

class TemarioAddTemasForm(forms.Form):
    """Formulario para agregar múltiples temas a un componente"""
    buscar = forms.CharField(
        label='Buscar tema',
        required=False,
        widget=forms.TextInput(attrs={
            'class': INPUT_CLASSES,
            'placeholder': 'Buscar por nombre...',
            'id': 'buscar-tema'
        })
    )
    
    temas = forms.ModelMultipleChoiceField(
        label='Selecciona los temas',
        queryset=Tema.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'form-checkbox h-4 w-4 text-blue-600'
        }),
        required=False
    )
    
    def __init__(self, *args, **kwargs):
        componente = kwargs.pop('componente', None)
        busqueda = kwargs.pop('busqueda', None)
        super().__init__(*args, **kwargs)
        
        # Filtrar temas que NO están ya asociados al componente
        if componente:
            temas_ya_asociados = Temario.objects.filter(componente=componente).values_list('tema_id', flat=True)
            queryset = Tema.objects.exclude(id__in=temas_ya_asociados).order_by('prioridad', 'nombre')
            
            # Aplicar búsqueda si existe
            if busqueda:
                queryset = queryset.filter(nombre__icontains=busqueda)
            
            self.fields['temas'].queryset = queryset
