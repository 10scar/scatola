from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import FormView
from django.urls import reverse_lazy
from formtools.wizard.views import SessionWizardView
from .models import Usuario, Rol, Perfil
from .forms import (
    LoginForm, 
    Paso1PersonalForm, Paso2AcademicoForm, Paso3SeguridadForm
)


def hola_mundo(request):
    """Vista de prueba inicial"""
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


class RegistroWizard(SessionWizardView):
    """Multi-step registration wizard con cache"""
    form_list = [Paso1PersonalForm, Paso2AcademicoForm, Paso3SeguridadForm]
    template_name = 'registro/wizard_form.html'
    
    def get_context_data(self, form, **kwargs):
        context = super().get_context_data(form=form, **kwargs)
        context.update({
            'step_num': self.steps.index + 1,
            'total_steps': len(self.form_list),
            'progress': ((self.steps.index + 1) / len(self.form_list)) * 100,
        })
        return context
    
    def done(self, form_list, **kwargs):
        data = {k: v for form in form_list for k, v in form.cleaned_data.items()}
        
        # Crear usuario
        user = Usuario.objects.create_user(
            username=data['username'], email=data['email'],
            first_name=data['first_name'], last_name=data['last_name'],
            password=data['password1']
        )
        
        # Asignar rol
        rol, _ = Rol.objects.get_or_create(nombre='Estudiante')
        user.rol = rol
        user.save()
        
        # Crear perfil
        Perfil.objects.update_or_create(
            usuario=user,
            defaults={'edad': data.get('edad'), 'nivel_formacion': data.get('nivel_formacion'),
                     'institucion': data.get('institucion')}
        )
        
        # Login automático
        login(self.request, authenticate(username=data['username'], password=data['password1']))
        messages.success(self.request, f'¡Bienvenido {user.first_name}!')
        return redirect('dashboard_estudiante')


class LoginView(FormView):
    """
    Vista basada en clase para el inicio de sesión de usuarios.
    Maneja la autenticación y redirección según el rol del usuario.
    """
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('dashboard_estudiante')
    
    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        
        if user is not None:
            login(self.request, user)
            messages.success(self.request, f'¡Bienvenido de nuevo, {user.first_name}!')
            
            # Redirigir según el rol del usuario
            if user.rol and user.rol.nombre == 'Estudiante':
                return redirect('dashboard_estudiante')
            else:
                return redirect('dashboard_estudiante')
        else:
            messages.error(self.request, 'Usuario o contraseña incorrectos.')
            return self.form_invalid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)


def logout_view(request):
    logout(request)
    messages.info(request, 'Has cerrado sesión exitosamente.')
    return redirect('login')


@login_required
def dashboard_estudiante(request):
    """Dashboard principal para estudiantes autenticados"""
    context = {
        'usuario': request.user,
    }
    return render(request, 'home_estudiante.html', context)

def landing_view(request):
    return render(request, 'landing/landing.html')
    
    
