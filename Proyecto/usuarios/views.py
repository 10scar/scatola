from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from formtools.wizard.views import SessionWizardView
from .models import Usuario, Perfil, NivelFormacion
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import Group
from .forms import (
    LoginForm, Paso1PersonalForm, Paso2AcademicoForm, Paso3SeguridadForm,
    UserUpdateForm, PerfilUpdateForm,
)

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta
from rutas.models import RespuestaDiaria


def get_redirect_url_by_role(user):
    if user.groups.filter(name='Administrador').exists():
        return 'dashboard_admin'
    
    return 'dashboard_estudiante'


@login_required
def profile_details(request):
    usuario = request.user
    perfil, created = Perfil.objects.get_or_create(usuario=usuario)

    context = {
        "usuario": usuario,
        "perfil": perfil,
    }
    return render(request, 'perfil_estudiante.html', context)

@login_required
def editar_perfil(request):
    usuario = request.user
    perfil, created = Perfil.objects.get_or_create(usuario=usuario)
    niveles = NivelFormacion.objects.all()

    if request.method == "POST":
        form_user = UserUpdateForm(request.POST, instance=usuario)
        form_perfil = PerfilUpdateForm(request.POST, instance=perfil)

        if form_user.is_valid() and form_perfil.is_valid():
            form_user.save()
            form_perfil.save()
            
            messages.success(request, "¡Datos actualizados correctamente!")
            return redirect("usuarios:profile_details")
        else:
            messages.error(request, "Por favor corrige los errores del formulario.")
    else:
        form_user = UserUpdateForm(instance=usuario)
        form_perfil = PerfilUpdateForm(instance=perfil)

    return render(request, "editar_perfil.html", {
        "form_user": form_user,
        "form_perfil": form_perfil,
    })
    

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
    usuario = request.user
    perfil, _ = Perfil.objects.get_or_create(usuario=usuario)
    preguntas_hoy = RespuestaDiaria.objects.filter(usuario=usuario, fecha__date=timezone.localdate()).count()
    context = {
        'usuario': usuario,
        'perfil': perfil,
        'preguntas_hoy': preguntas_hoy,
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


# ============================================
# MIXIN PARA VERIFICAR PERMISOS DE ADMINISTRADOR
# ============================================

class AdminRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """Mixin para verificar que el usuario sea administrador"""
    login_url = reverse_lazy('login')
    
    def test_func(self):
        return self.request.user.groups.filter(name='Administrador').exists()
    
    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            messages.error(self.request, 'Debes iniciar sesión para acceder a esta página.')
            return redirect(self.login_url)
        messages.error(self.request, 'No tienes permisos de administrador.')
        return redirect('dashboard_estudiante')



@login_required
def recuerdo_racha(request):
    """Endpoint JSON que indica si el usuario debe recibir un recordatorio para mantener su racha.

    Respuesta: { 'reminder': true|false, 'detail': 'texto opcional' }
    """
    try:
        perfil = request.user.perfil
    except Exception:
        # Si el usuario no tiene perfil, no hacemos nada
        return JsonResponse({'reminder': False, 'detail': 'Sin perfil'}, status=200)

    necesita = False
    try:
        # Lógica localizada aquí: recordatorio si no existe `ultima_respuesta_diaria`
        # o si su fecha es anterior al día actual.
        # Si el usuario ya respondió 6 (o más) preguntas hoy, no necesita recordatorio
        from django.apps import apps
        RespuestaDiaria = apps.get_model('rutas', 'RespuestaDiaria')
        respuestas_hoy_count = RespuestaDiaria.objects.filter(usuario=request.user, fecha__date=timezone.localdate()).count()
        if respuestas_hoy_count >= 6:
            necesita = False
        elif not perfil.ultima_respuesta_diaria:
            necesita = True
        else:
            from django.apps import apps
            RespuestaDiaria = apps.get_model('rutas', 'RespuestaDiaria')
            fecha_dt = (
                RespuestaDiaria.objects
                .filter(pk=perfil.ultima_respuesta_diaria)
                .values_list('fecha', flat=True)
                .first()
            )
            if not fecha_dt:
                necesita = True
            else:
                try:
                    # Convertir a hora local si es un datetime con tz
                    try:
                        if timezone.is_aware(fecha_dt):
                            fecha_local = timezone.localtime(fecha_dt)
                        else:
                            fecha_local = fecha_dt
                        ultima_fecha = fecha_local.date()
                    except Exception:
                        ultima_fecha = fecha_dt

                    hoy = timezone.localdate()
                    necesita = (ultima_fecha != hoy)
                except Exception:
                    necesita = True
    except Exception:
        # En caso de error defensivo, pedir recordatorio para mayor seguridad
        necesita = True

    detail = 'Se requiere recordatorio' if necesita else 'Racha al día'
    return JsonResponse({'reminder': necesita, 'detail': detail}, status=200)



