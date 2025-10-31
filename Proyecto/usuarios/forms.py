from django import forms
from .models import Usuario, Perfil, NivelFormacion

# Estilos comunes de Tailwind
INPUT_CLASSES = 'mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500'


class LoginForm(forms.Form):
    """
    Formulario de inicio de sesión con estilos de Tailwind CSS.
    """
    username = forms.CharField(
        label='Nombre de usuario o correo',
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500',
            'placeholder': 'tu_usuario',
            'id': 'username'
        })
    )
    
    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500',
            'placeholder': '••••••••',
            'id': 'password'
        })
    )


class Paso1PersonalForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario', max_length=150, 
        widget=forms.TextInput(attrs={'class': INPUT_CLASSES, 'placeholder': 'tu_usuario'}))
    email = forms.EmailField(label='Correo electrónico',
        widget=forms.EmailInput(attrs={'class': INPUT_CLASSES, 'placeholder': 'correo@ejemplo.com'}))
    first_name = forms.CharField(label='Nombre', max_length=150,
        widget=forms.TextInput(attrs={'class': INPUT_CLASSES, 'placeholder': 'Juan'}))
    last_name = forms.CharField(label='Apellidos', max_length=150,
        widget=forms.TextInput(attrs={'class': INPUT_CLASSES, 'placeholder': 'Pérez'}))
    
    def clean_username(self):
        """Valida que el username no exista"""
        username = self.cleaned_data.get('username')
        if Usuario.objects.filter(username=username).exists():
            raise forms.ValidationError('Este nombre de usuario ya está en uso.')
        return username
    
    def clean_email(self):
        """Valida que el email no exista"""
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo electrónico ya está registrado.')
        return email


class Paso2AcademicoForm(forms.Form):
    edad = forms.IntegerField(label='Edad', required=False, min_value=5, max_value=100,
        widget=forms.NumberInput(attrs={'class': INPUT_CLASSES, 'placeholder': '18'}))
    nivel_formacion = forms.ModelChoiceField(label='Nivel de Formación', 
        queryset=NivelFormacion.objects.all(), required=False,
        widget=forms.Select(attrs={'class': INPUT_CLASSES}))
    institucion = forms.CharField(label='Institución Educativa', max_length=45, required=False,
        widget=forms.TextInput(attrs={'class': INPUT_CLASSES, 'placeholder': 'Colegio'}))


class Paso3SeguridadForm(forms.Form):
    password1 = forms.CharField(label='Contraseña', min_length=8,
        widget=forms.PasswordInput(attrs={'class': INPUT_CLASSES}),
        help_text='Mínimo 8 caracteres.')
    password2 = forms.CharField(label='Confirmar contraseña',
        widget=forms.PasswordInput(attrs={'class': INPUT_CLASSES}))
    
    def clean_password1(self):
        """Valida la longitud mínima de la contraseña"""
        password = self.cleaned_data.get('password1')
        if len(password) < 8:
            raise forms.ValidationError('La contraseña debe tener al menos 8 caracteres.')
        return password
    
    def clean(self):
        cleaned_data = super().clean()
        pwd1 = cleaned_data.get('password1')
        pwd2 = cleaned_data.get('password2')
        if pwd1 and pwd2 and pwd1 != pwd2:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return cleaned_data
