from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.db.models import Q

# Importar modelos
from preguntas.models import Tema, Contenido, Componente, TipoExamen, Temario

# Importar formularios
from preguntas.forms import TemaForm, ContenidoForm, TemarioAddTemasForm


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


# ============================================
# VISTAS PARA GESTIÓN DE TEMAS
# ============================================

class TemaListView(AdminRequiredMixin, ListView):
    """Vista para listar todos los temas"""
    model = Tema
    template_name = 'admin/temas/tema_list.html'
    context_object_name = 'temas'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Tema.objects.prefetch_related('temarios__componente').order_by('prioridad', 'nombre')
        
        # Filtro por búsqueda
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(nombre__icontains=search) | 
                Q(descripcion__icontains=search)
            )
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context

# ...existing code... (el resto de tus vistas)


class TemaListView(AdminRequiredMixin, ListView):
    """Vista para listar todos los temas"""
    model = Tema
    template_name = 'admin/temas/tema_list.html'
    context_object_name = 'temas'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Tema.objects.prefetch_related('temarios').order_by('prioridad', 'nombre')
        
        # Filtro por búsqueda
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(nombre__icontains=search)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context


class TemaCreateView(AdminRequiredMixin, CreateView):
    """Vista para crear un nuevo tema"""
    model = Tema
    form_class = TemaForm
    template_name = 'admin/temas/tema_form.html'
    success_url = reverse_lazy('usuarios:tema_list')
    
    def form_valid(self, form):
        messages.success(self.request, f'Tema "{form.instance.nombre}" creado exitosamente.')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Nuevo Tema'
        context['button_text'] = 'Crear Tema'
        return context


class TemaUpdateView(AdminRequiredMixin, UpdateView):
    """Vista para editar un tema existente"""
    model = Tema
    form_class = TemaForm
    template_name = 'admin/temas/tema_form.html'
    success_url = reverse_lazy('usuarios:tema_list')
    
    def form_valid(self, form):
        messages.success(self.request, f'Tema "{form.instance.nombre}" actualizado exitosamente.')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Tema'
        context['button_text'] = 'Guardar Cambios'
        return context


class TemaDeleteView(AdminRequiredMixin, DeleteView):
    """Vista para eliminar un tema"""
    model = Tema
    template_name = 'admin/temas/tema_confirm_delete.html'
    success_url = reverse_lazy('usuarios:tema_list')
    
    def delete(self, request, *args, **kwargs):
        tema = self.get_object()
        messages.success(request, f'Tema "{tema.nombre}" eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)


# ============================================
# VISTAS PARA GESTIÓN DE CONTENIDOS
# ============================================

class ContenidoListView(AdminRequiredMixin, ListView):
    """Vista para listar los contenidos de un tema específico"""
    model = Contenido
    template_name = 'admin/temas/contenido_list.html'
    context_object_name = 'contenidos'
    paginate_by = 15
    
    def get_queryset(self):
        self.tema = get_object_or_404(Tema, pk=self.kwargs['tema_id'])
        return Contenido.objects.filter(tema=self.tema).select_related('padre_id').order_by('titulo')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tema'] = self.tema
        return context


class ContenidoCreateView(AdminRequiredMixin, CreateView):
    """Vista para crear un nuevo contenido dentro de un tema"""
    model = Contenido
    form_class = ContenidoForm
    template_name = 'admin/temas/contenido_form.html'
    
    def dispatch(self, request, *args, **kwargs):
        self.tema = get_object_or_404(Tema, pk=self.kwargs['tema_id'])
        return super().dispatch(request, *args, **kwargs)
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['tema'] = self.tema
        return kwargs
    
    def form_valid(self, form):
        form.instance.tema = self.tema
        messages.success(self.request, f'Contenido "{form.instance.titulo}" creado exitosamente.')
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('usuarios:contenido_list', kwargs={'tema_id': self.tema.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tema'] = self.tema
        context['title'] = 'Crear Nuevo Contenido'
        context['button_text'] = 'Crear Contenido'
        return context


class ContenidoUpdateView(AdminRequiredMixin, UpdateView):
    """Vista para editar un contenido existente"""
    model = Contenido
    form_class = ContenidoForm
    template_name = 'admin/temas/contenido_form.html'
    pk_url_kwarg = 'contenido_id'
    
    def dispatch(self, request, *args, **kwargs):
        self.tema = get_object_or_404(Tema, pk=self.kwargs['tema_id'])
        return super().dispatch(request, *args, **kwargs)
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['tema'] = self.tema
        return kwargs
    
    def form_valid(self, form):
        messages.success(self.request, f'Contenido "{form.instance.titulo}" actualizado exitosamente.')
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('usuarios:contenido_list', kwargs={'tema_id': self.tema.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tema'] = self.tema
        context['title'] = 'Editar Contenido'
        context['button_text'] = 'Guardar Cambios'
        return context


class ContenidoDeleteView(AdminRequiredMixin, DeleteView):
    """Vista para eliminar un contenido"""
    model = Contenido
    template_name = 'admin/temas/contenido_confirm_delete.html'
    pk_url_kwarg = 'contenido_id'
    
    def dispatch(self, request, *args, **kwargs):
        self.tema = get_object_or_404(Tema, pk=self.kwargs['tema_id'])
        return super().dispatch(request, *args, **kwargs)
    
    def get_success_url(self):
        return reverse_lazy('usuarios:contenido_list', kwargs={'tema_id': self.tema.pk})
    
    def delete(self, request, *args, **kwargs):
        contenido = self.get_object()
        messages.success(request, f'Contenido "{contenido.titulo}" eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tema'] = self.tema
        return context


# ============================================
# VISTAS PARA GESTIÓN DE TEMARIOS
# ============================================

class TemarioIndexView(AdminRequiredMixin, ListView):
    """Vista principal: Lista de Tipos de Examen"""
    model = TipoExamen
    template_name = 'admin/temarios/temario_index.html'
    context_object_name = 'tipos_examen'
    
    def get_queryset(self):
        return TipoExamen.objects.prefetch_related('componente_set').order_by('nombre')


class ComponenteListView(AdminRequiredMixin, ListView):
    """Vista: Lista de componentes de un Tipo de Examen"""
    model = Componente
    template_name = 'admin/temarios/componente_list.html'
    context_object_name = 'componentes'
    
    def dispatch(self, request, *args, **kwargs):
        self.tipo_examen = get_object_or_404(TipoExamen, pk=self.kwargs['tipo_id'])
        return super().dispatch(request, *args, **kwargs)
    
    def get_queryset(self):
        return Componente.objects.filter(tipo_examen=self.tipo_examen).prefetch_related('temarios').order_by('prioridad', 'nombre')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tipo_examen'] = self.tipo_examen
        return context


class TemarioDetailView(AdminRequiredMixin, ListView):
    """Vista: Temas asociados a un componente específico"""
    model = Temario
    template_name = 'admin/temarios/temario_detail.html'
    context_object_name = 'temarios'
    paginate_by = 15
    
    def dispatch(self, request, *args, **kwargs):
        self.componente = get_object_or_404(Componente, pk=self.kwargs['comp_id'])
        return super().dispatch(request, *args, **kwargs)
    
    def get_queryset(self):
        return Temario.objects.filter(componente=self.componente).select_related('tema').order_by('tema__prioridad', 'tema__nombre')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['componente'] = self.componente
        context['tipo_examen'] = self.componente.tipo_examen
        return context


class TemarioAddTemasView(AdminRequiredMixin, FormView):
    """Vista: Agregar múltiples temas a un componente"""
    form_class = TemarioAddTemasForm
    template_name = 'admin/temarios/temario_add_temas.html'
    
    def dispatch(self, request, *args, **kwargs):
        self.componente = get_object_or_404(Componente, pk=self.kwargs['comp_id'])
        return super().dispatch(request, *args, **kwargs)
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['componente'] = self.componente
        kwargs['busqueda'] = self.request.GET.get('buscar', '')
        return kwargs
    
    def form_valid(self, form):
        temas_seleccionados = form.cleaned_data.get('temas')
        
        if temas_seleccionados:
            # Crear las asociaciones en Temario
            temarios_nuevos = [
                Temario(tema=tema, componente=self.componente)
                for tema in temas_seleccionados
            ]
            Temario.objects.bulk_create(temarios_nuevos, ignore_conflicts=True)
            
            messages.success(
                self.request, 
                f'{len(temas_seleccionados)} tema(s) agregado(s) a {self.componente.nombre}.'
            )
        else:
            messages.warning(self.request, 'No se seleccionó ningún tema.')
        
        return redirect('usuarios:temario_detail', comp_id=self.componente.pk)
    
    def get_success_url(self):
        return reverse_lazy('usuarios:temario_detail', kwargs={'comp_id': self.componente.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['componente'] = self.componente
        context['tipo_examen'] = self.componente.tipo_examen
        context['busqueda'] = self.request.GET.get('buscar', '')
        return context


class TemarioRemoveTemaView(AdminRequiredMixin, DeleteView):
    """Vista: Eliminar la asociación de un tema con un componente"""
    model = Temario
    template_name = 'admin/temarios/temario_confirm_remove.html'
    
    def dispatch(self, request, *args, **kwargs):
        self.componente = get_object_or_404(Componente, pk=self.kwargs['comp_id'])
        return super().dispatch(request, *args, **kwargs)
    
    def get_object(self):
        return get_object_or_404(
            Temario, 
            componente=self.componente, 
            tema_id=self.kwargs['tema_id']
        )
    
    def get_success_url(self):
        return reverse_lazy('usuarios:temario_detail', kwargs={'comp_id': self.componente.pk})
    
    def delete(self, request, *args, **kwargs):
        temario = self.get_object()
        messages.success(
            request, 
            f'Tema "{temario.tema.nombre}" eliminado de {self.componente.nombre}.'
        )
        return super().delete(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['componente'] = self.componente
        context['tipo_examen'] = self.componente.tipo_examen
        return context
