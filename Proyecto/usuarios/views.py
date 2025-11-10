from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from formtools.wizard.views import SessionWizardView
from .models import Usuario, Perfil
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import Group
from .forms import (LoginForm, Paso1PersonalForm, Paso2AcademicoForm, Paso3SeguridadForm)


def get_redirect_url_by_role(user):
    if user.groups.filter(name='Administrador').exists():
        return 'dashboard_admin'
    
    return 'dashboard_estudiante'


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
        estudiante_group = Group.objects.get(name='Estudiante')
        user.groups.add(estudiante_group)
 
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
    template_name = 'login.html'
    form_class = LoginForm

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        
        if user is None:
            messages.error(self.request, 'Usuario o contraseña incorrectos.')
            return self.form_invalid(form)
        
        login(self.request, user)
        messages.success(self.request, f'¡Bienvenido de nuevo, {user.first_name}!')
            
        redirect_url = get_redirect_url_by_role(user)
        return redirect(redirect_url)
        
    
    def form_invalid(self, form):
        return super().form_invalid(form)


def logout_view(request):
    logout(request)
    messages.info(request, 'Has cerrado sesión exitosamente.')
    return redirect('login')


@login_required
def dashboard_estudiante(request):
    context = {
        'usuario': request.user,
    }
    return render(request, 'home_estudiante.html', context)

def landing_view(request):
    return render(request, 'landing/landing.html')

class DashboardAdminView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'admin/dashboard_admin.html'
    login_url = reverse_lazy('login')

    def test_func(self):
        return self.request.user.groups.filter(name='Administrador').exists()

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para acceder a esta página.')
        return redirect('dashboard_estudiante')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usuario'] = self.request.user
        return context


