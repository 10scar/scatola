# ============================================
# VISTAS PARA GESTIÓN DE PREGUNTAS, GRUPOS Y TIPOS
# ============================================
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, FormView
from django.urls import reverse_lazy
from django.db.models import Q, Count
from django.db import transaction

# Importar modelos
from preguntas.models import (
    Pregunta, TipoPregunta, Grupo, 
    Contenido, TipoExamen
)

# Importar formularios
from preguntas.forms import (
    TipoPreguntaForm, GrupoForm, GrupoAddPreguntasForm,
    PreguntaForm, OpcionFormSet
)

# Importar mixin de permisos
from preguntas.views.dashboard_admin import AdminRequiredMixin


# ============================================
# VISTAS PARA GESTIÓN DE TIPOS DE PREGUNTA
# ============================================

class TipoPreguntaListView(AdminRequiredMixin, ListView):
    """Vista para listar todos los tipos de pregunta"""
    model = TipoPregunta
    template_name = 'admin/tipos_pregunta/tipo_pregunta_list.html'
    context_object_name = 'tipos_pregunta'
    paginate_by = 15
    
    def get_queryset(self):
        queryset = TipoPregunta.objects.annotate(
            num_preguntas=Count('pregunta')
        ).order_by('nombre')
        
        # Filtro por búsqueda
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(nombre__icontains=search)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context


class TipoPreguntaCreateView(AdminRequiredMixin, CreateView):
    """Vista para crear un nuevo tipo de pregunta"""
    model = TipoPregunta
    form_class = TipoPreguntaForm
    template_name = 'admin/tipos_pregunta/tipo_pregunta_form.html'
    success_url = reverse_lazy('dashboard_admin:tipo_pregunta_list')
    
    def form_valid(self, form):
        messages.success(self.request, f'Tipo de pregunta "{form.instance.nombre}" creado exitosamente.')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Nuevo Tipo de Pregunta'
        context['button_text'] = 'Crear Tipo'
        return context


class TipoPreguntaUpdateView(AdminRequiredMixin, UpdateView):
    """Vista para editar un tipo de pregunta existente"""
    model = TipoPregunta
    form_class = TipoPreguntaForm
    template_name = 'admin/tipos_pregunta/tipo_pregunta_form.html'
    success_url = reverse_lazy('dashboard_admin:tipo_pregunta_list')
    
    def form_valid(self, form):
        messages.success(self.request, f'Tipo de pregunta "{form.instance.nombre}" actualizado exitosamente.')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Tipo de Pregunta'
        context['button_text'] = 'Guardar Cambios'
        return context


class TipoPreguntaDeleteView(AdminRequiredMixin, DeleteView):
    """Vista para eliminar un tipo de pregunta"""
    model = TipoPregunta
    template_name = 'admin/tipos_pregunta/tipo_pregunta_confirm_delete.html'
    success_url = reverse_lazy('dashboard_admin:tipo_pregunta_list')
    
    def delete(self, request, *args, **kwargs):
        tipo = self.get_object()
        try:
            messages.success(request, f'Tipo de pregunta "{tipo.nombre}" eliminado exitosamente.')
            return super().delete(request, *args, **kwargs)
        except Exception:
            messages.error(request, 'No se puede eliminar el tipo de pregunta porque tiene preguntas asociadas.')
            return redirect('dashboard_admin:tipo_pregunta_list')


# ============================================
# VISTAS PARA GESTIÓN DE GRUPOS
# ============================================

class GrupoListView(AdminRequiredMixin, ListView):
    """Vista para listar todos los grupos de preguntas"""
    model = Grupo
    template_name = 'admin/grupos/grupo_list.html'
    context_object_name = 'grupos'
    paginate_by = 15
    
    def get_queryset(self):
        queryset = Grupo.objects.annotate(
            num_preguntas=Count('pregunta')
        ).order_by('titulo')
        
        # Filtro por búsqueda
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(titulo__icontains=search) |
                Q(descripcion__icontains=search)
            )
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context


class GrupoCreateView(AdminRequiredMixin, CreateView):
    """Vista para crear un nuevo grupo"""
    model = Grupo
    form_class = GrupoForm
    template_name = 'admin/grupos/grupo_form.html'
    success_url = reverse_lazy('dashboard_admin:grupo_list')
    
    def form_valid(self, form):
        messages.success(self.request, f'Grupo "{form.instance.titulo}" creado exitosamente.')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Nuevo Grupo'
        context['button_text'] = 'Crear Grupo'
        return context


class GrupoUpdateView(AdminRequiredMixin, UpdateView):
    """Vista para editar un grupo existente"""
    model = Grupo
    form_class = GrupoForm
    template_name = 'admin/grupos/grupo_form.html'
    success_url = reverse_lazy('dashboard_admin:grupo_list')
    
    def form_valid(self, form):
        messages.success(self.request, f'Grupo "{form.instance.titulo}" actualizado exitosamente.')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Grupo'
        context['button_text'] = 'Guardar Cambios'
        return context


class GrupoDeleteView(AdminRequiredMixin, DeleteView):
    """Vista para eliminar un grupo"""
    model = Grupo
    template_name = 'admin/grupos/grupo_confirm_delete.html'
    success_url = reverse_lazy('dashboard_admin:grupo_list')
    
    def delete(self, request, *args, **kwargs):
        grupo = self.get_object()
        messages.success(request, f'Grupo "{grupo.titulo}" eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)


class GrupoDetailView(AdminRequiredMixin, DetailView):
    """Vista para ver los detalles y preguntas de un grupo"""
    model = Grupo
    template_name = 'admin/grupos/grupo_detail.html'
    context_object_name = 'grupo'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['preguntas'] = Pregunta.objects.filter(
            grupo=self.object
        ).select_related('tipo_pregunta', 'contenido', 'tipo_examen').prefetch_related('opciones')
        return context


class GrupoAddPreguntasView(AdminRequiredMixin, FormView):
    """Vista para agregar preguntas existentes a un grupo"""
    form_class = GrupoAddPreguntasForm
    template_name = 'admin/grupos/grupo_add_preguntas.html'
    
    def dispatch(self, request, *args, **kwargs):
        self.grupo = get_object_or_404(Grupo, pk=self.kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['grupo'] = self.grupo
        kwargs['busqueda'] = self.request.GET.get('buscar', '')
        return kwargs
    
    def form_valid(self, form):
        preguntas_seleccionadas = form.cleaned_data.get('preguntas')
        
        if preguntas_seleccionadas:
            # Asignar las preguntas al grupo
            preguntas_seleccionadas.update(grupo=self.grupo)
            
            messages.success(
                self.request, 
                f'{preguntas_seleccionadas.count()} pregunta(s) agregada(s) a "{self.grupo.titulo}".'
            )
        else:
            messages.warning(self.request, 'No se seleccionó ninguna pregunta.')
        
        return redirect('dashboard_admin:grupo_detail', pk=self.grupo.pk)
    
    def get_success_url(self):
        return reverse_lazy('dashboard_admin:grupo_detail', kwargs={'pk': self.grupo.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grupo'] = self.grupo
        context['busqueda'] = self.request.GET.get('buscar', '')
        return context


# ============================================
# VISTAS PARA GESTIÓN DE PREGUNTAS
# ============================================

class PreguntaListView(AdminRequiredMixin, ListView):
    """Vista para listar todas las preguntas con filtros"""
    model = Pregunta
    template_name = 'admin/preguntas/pregunta_list.html'
    context_object_name = 'preguntas'
    paginate_by = 20
    
    def get_queryset(self):
        queryset = Pregunta.objects.select_related(
            'tipo_pregunta', 'contenido', 'tipo_examen', 'grupo'
        ).prefetch_related('opciones').order_by('-id')
        
        # Filtros
        search = self.request.GET.get('search')
        tipo_pregunta_id = self.request.GET.get('tipo_pregunta')
        tipo_examen_id = self.request.GET.get('tipo_examen')
        contenido_id = self.request.GET.get('contenido')
        grupo_id = self.request.GET.get('grupo')
        
        if search:
            queryset = queryset.filter(
                Q(titulo__icontains=search) |
                Q(descripcion__icontains=search)
            )
        
        if tipo_pregunta_id:
            queryset = queryset.filter(tipo_pregunta_id=tipo_pregunta_id)
        
        if tipo_examen_id:
            queryset = queryset.filter(tipo_examen_id=tipo_examen_id)
        
        if contenido_id:
            queryset = queryset.filter(contenido_id=contenido_id)
        
        if grupo_id:
            queryset = queryset.filter(grupo_id=grupo_id)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        context['tipos_pregunta'] = TipoPregunta.objects.all()
        context['tipos_examen'] = TipoExamen.objects.all()
        context['grupos'] = Grupo.objects.all()
        context['filtros'] = {
            'tipo_pregunta': self.request.GET.get('tipo_pregunta', ''),
            'tipo_examen': self.request.GET.get('tipo_examen', ''),
            'contenido': self.request.GET.get('contenido', ''),
            'grupo': self.request.GET.get('grupo', ''),
        }
        return context


class PreguntaCreateView(AdminRequiredMixin, CreateView):
    """Vista para crear una nueva pregunta con sus opciones"""
    model = Pregunta
    form_class = PreguntaForm
    template_name = 'admin/preguntas/pregunta_form.html'
    success_url = reverse_lazy('dashboard_admin:pregunta_list')
    
    def get_initial(self):
        initial = super().get_initial()
        contenido_id = self.request.GET.get('contenido')
        if contenido_id:
            initial['contenido'] = contenido_id
        return initial
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = OpcionFormSet(self.request.POST, self.request.FILES)
        else:
            context['formset'] = OpcionFormSet()
        context['title'] = 'Crear Nueva Pregunta'
        context['button_text'] = 'Crear Pregunta'
        return context
    
    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        
        with transaction.atomic():
            self.object = form.save()
            
            if formset.is_valid():
                formset.instance = self.object
                opciones = formset.save(commit=False)
                
                # Validar que solo haya una opción correcta
                opciones_correctas = 0
                for opcion_form in formset:
                    if opcion_form.cleaned_data.get('es_correcta'):
                        opciones_correctas += 1
                
                if opciones_correctas != 1:
                    messages.error(self.request, 'Debe haber exactamente una opción correcta.')
                    return self.form_invalid(form)
                
                # Guardar opciones con puntaje correcto
                for i, opcion_form in enumerate(formset):
                    if opcion_form.cleaned_data and not opcion_form.cleaned_data.get('DELETE'):
                        opcion = opciones[i] if i < len(opciones) else None
                        if opcion:
                            opcion.puntaje = 1 if opcion_form.cleaned_data.get('es_correcta') else 0
                            opcion.save()
                
                # Eliminar opciones marcadas para borrar
                for opcion in formset.deleted_objects:
                    opcion.delete()
                
                messages.success(self.request, f'Pregunta "{self.object.titulo}" creada exitosamente.')
                return redirect(self.success_url)
            else:
                return self.form_invalid(form)


class PreguntaUpdateView(AdminRequiredMixin, UpdateView):
    """Vista para editar una pregunta existente"""
    model = Pregunta
    form_class = PreguntaForm
    template_name = 'admin/preguntas/pregunta_form.html'
    success_url = reverse_lazy('dashboard_admin:pregunta_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = OpcionFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['formset'] = OpcionFormSet(instance=self.object)
        context['title'] = 'Editar Pregunta'
        context['button_text'] = 'Guardar Cambios'
        return context
    
    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        
        with transaction.atomic():
            self.object = form.save()
            
            if formset.is_valid():
                opciones = formset.save(commit=False)
                
                # Validar que solo haya una opción correcta
                opciones_correctas = 0
                for opcion_form in formset:
                    if opcion_form.cleaned_data and not opcion_form.cleaned_data.get('DELETE'):
                        if opcion_form.cleaned_data.get('es_correcta'):
                            opciones_correctas += 1
                
                if opciones_correctas != 1:
                    messages.error(self.request, 'Debe haber exactamente una opción correcta.')
                    return self.form_invalid(form)
                
                # Guardar opciones con puntaje correcto
                for i, opcion_form in enumerate(formset):
                    if opcion_form.cleaned_data and not opcion_form.cleaned_data.get('DELETE'):
                        opcion = opciones[i] if i < len(opciones) else opcion_form.instance
                        opcion.puntaje = 1 if opcion_form.cleaned_data.get('es_correcta') else 0
                        opcion.save()
                
                # Eliminar opciones marcadas para borrar
                for opcion in formset.deleted_objects:
                    opcion.delete()
                
                messages.success(self.request, f'Pregunta "{self.object.titulo}" actualizada exitosamente.')
                return redirect(self.success_url)
            else:
                return self.form_invalid(form)


class PreguntaDetailView(AdminRequiredMixin, DetailView):
    """Vista para ver los detalles completos de una pregunta"""
    model = Pregunta
    template_name = 'admin/preguntas/pregunta_detail.html'
    context_object_name = 'pregunta'
    
    def get_queryset(self):
        return Pregunta.objects.select_related(
            'tipo_pregunta', 'contenido', 'tipo_examen', 'grupo'
        ).prefetch_related('opciones')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Contar opciones correctas
        context['opciones_correctas'] = self.object.opciones.filter(puntaje__gt=0).count()
        return context


class PreguntaDeleteView(AdminRequiredMixin, DeleteView):
    """Vista para eliminar una pregunta"""
    model = Pregunta
    template_name = 'admin/preguntas/pregunta_confirm_delete.html'
    success_url = reverse_lazy('dashboard_admin:pregunta_list')
    
    def delete(self, request, *args, **kwargs):
        pregunta = self.get_object()
        messages.success(request, f'Pregunta "{pregunta.titulo}" eliminada exitosamente.')
        return super().delete(request, *args, **kwargs)


# ============================================
# VISTAS CONTEXTUALES (DESDE CONTENIDOS)
# ============================================

class ContenidoPreguntasView(AdminRequiredMixin, ListView):
    """Vista para ver y gestionar preguntas desde un contenido específico"""
    model = Pregunta
    template_name = 'admin/contenidos/contenido_preguntas.html'
    context_object_name = 'preguntas'
    paginate_by = 15
    
    def dispatch(self, request, *args, **kwargs):
        self.contenido = get_object_or_404(Contenido, pk=self.kwargs['contenido_id'])
        return super().dispatch(request, *args, **kwargs)
    
    def get_queryset(self):
        return Pregunta.objects.filter(
            contenido=self.contenido
        ).select_related('tipo_pregunta', 'tipo_examen', 'grupo').prefetch_related('opciones').order_by('-id')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contenido'] = self.contenido
        context['tema'] = self.contenido.tema
        return context
