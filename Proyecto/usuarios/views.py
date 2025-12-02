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
from rutas.models import Ruta
from preguntas.models import TipoExamen, Componente
from rutas.forms import RutaUsuarioForm
from rutas.services import sincronizar_lecciones

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
    
@login_required
def editar_ruta_usuario(request):
    ruta_obj, _ = Ruta.objects.get_or_create(usuario=request.user)

    icfes = TipoExamen.objects.filter(nombre__icontains="ICFES")
    unal = TipoExamen.objects.filter(nombre__icontains="UNAL")
    try:
        icfes_exam = TipoExamen.objects.get(nombre="ICFES Saber 11")
    except TipoExamen.DoesNotExist:
        icfes_exam = None

    try:
        unal_exam = TipoExamen.objects.get(nombre="Admisión UNAL")
    except TipoExamen.DoesNotExist:
        unal_exam = None

    componentes_icfes = Componente.objects.filter(tipo_examen=icfes_exam) if icfes_exam else Componente.objects.none()
    componentes_unal = Componente.objects.filter(tipo_examen=unal_exam) if unal_exam else Componente.objects.none()
    componentes_icfes_ids = list(componentes_icfes.values_list('id', flat=True))
    componentes_unal_ids = list(componentes_unal.values_list('id', flat=True))

    if request.method == "POST":
        form = RutaUsuarioForm(request.POST, instance=ruta_obj)
        if form.is_valid():
            ruta = form.save(commit=False)
            ruta.usuario = request.user
            ruta.save()
            form.save_m2m()
            sincronizar_lecciones(ruta.id)
            messages.success(request, "Ruta y componentes guardados correctamente.")
            # Redirigir a la página de pregunta sobre prueba diagnóstica
            return redirect("usuarios:preguntar_prueba_diagnostica")
        else:
            messages.error(request, "Corrige los errores del formulario.")
    else:
        form = RutaUsuarioForm(instance=ruta_obj)

    context = {
        "form": form,
        "componentes_icfes": componentes_icfes,
        "componentes_unal": componentes_unal,
        "icfes_exam": icfes_exam,
        "unal_exam": unal_exam,
        "componentes_icfes_ids": componentes_icfes_ids,
        "componentes_unal_ids": componentes_unal_ids,
        "usuario_examenes": list(ruta_obj.examenes.values_list("id", flat=True)),
        "usuario_componentes": list(ruta_obj.componentes.values_list("id", flat=True)),
    }

    return render(request, "modificar_rutas.html", context)



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
        messages.success(self.request, f'¡{user.first_name}!, por favor selecciona tu ruta de aprendizaje')
        return redirect('usuarios:ver_rutas')


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
        # Reiniciar racha visual si la última respuesta fue hace >= 2 días
        try:
            perfil, _ = Perfil.objects.get_or_create(usuario=user)
            perfil.reiniciar_racha_si_vieja(threshold_days=2)
        except Exception:
            # No bloquear el login ante errores
            pass
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
    template_name = 'admin/home.html'
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


@login_required
def preguntar_prueba_diagnostica(request):
    """Página intermedia que pregunta si el usuario desea realizar la prueba diagnóstica"""
    ruta = get_object_or_404(Ruta, usuario=request.user)
    
    # Verificar que tenga componentes seleccionados
    if not ruta.componentes.exists():
        messages.warning(request, "Primero debes seleccionar tus componentes de estudio.")
        return redirect("usuarios:ver_rutas")
    
    if request.method == "POST":
        realizar_prueba = request.POST.get('realizar_prueba') == 'si'
        
        if realizar_prueba:
            # Redirigir a la prueba diagnóstica
            return redirect('diagnosticos:iniciar')
        else:
            # Generar ruta sin prueba diagnóstica (con todos los temas)
            from rutas.services import generar_ruta_sin_diagnostica
            generar_ruta_sin_diagnostica(request.user, ruta)
            messages.success(request, "¡Tu ruta de aprendizaje ha sido creada! Puedes comenzar con tus lecciones.")
            return redirect('dashboard_estudiante')
    
    context = {
        'ruta': ruta,
        'componentes': ruta.componentes.all(),
    }
    
    return render(request, 'usuarios/preguntar_prueba_diagnostica.html', context)

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



