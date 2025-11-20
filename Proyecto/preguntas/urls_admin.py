from django.urls import path
from preguntas.views import dashboard_admin, dashboard_admin_preguntas

app_name = 'dashboard_admin'

urlpatterns = [
    # Gestión de Temas
    path('temas/', dashboard_admin.TemaListView.as_view(), name='tema_list'),
    path('temas/crear/', dashboard_admin.TemaCreateView.as_view(), name='tema_create'),
    path('temas/<int:pk>/editar/', dashboard_admin.TemaUpdateView.as_view(), name='tema_update'),
    path('temas/<int:pk>/eliminar/', dashboard_admin.TemaDeleteView.as_view(), name='tema_delete'),
    
    # Gestión de Contenidos
    path('temas/<int:tema_id>/contenidos/', dashboard_admin.ContenidoListView.as_view(), name='contenido_list'),
    path('temas/<int:tema_id>/contenidos/crear/', dashboard_admin.ContenidoCreateView.as_view(), name='contenido_create'),
    path('temas/<int:tema_id>/contenidos/<int:contenido_id>/editar/', dashboard_admin.ContenidoUpdateView.as_view(), name='contenido_update'),
    path('temas/<int:tema_id>/contenidos/<int:contenido_id>/eliminar/', dashboard_admin.ContenidoDeleteView.as_view(), name='contenido_delete'),
    path('contenidos/<int:contenido_id>/preguntas/', dashboard_admin_preguntas.ContenidoPreguntasView.as_view(), name='contenido_preguntas'),
    
    # Gestión de Temarios (Asociación Tema-Componente)
    path('temarios/', dashboard_admin.TemarioIndexView.as_view(), name='temario_index'),
    path('temarios/tipo-examen/<int:tipo_id>/', dashboard_admin.ComponenteListView.as_view(), name='componente_list'),
    path('temarios/componente/<int:comp_id>/', dashboard_admin.TemarioDetailView.as_view(), name='temario_detail'),
    path('temarios/componente/<int:comp_id>/agregar/', dashboard_admin.TemarioAddTemasView.as_view(), name='temario_add_temas'),
    path('temarios/componente/<int:comp_id>/eliminar/<int:tema_id>/', dashboard_admin.TemarioRemoveTemaView.as_view(), name='temario_remove_tema'),
    
    # Gestión de Tipos de Pregunta
    path('tipos-pregunta/', dashboard_admin_preguntas.TipoPreguntaListView.as_view(), name='tipo_pregunta_list'),
    path('tipos-pregunta/crear/', dashboard_admin_preguntas.TipoPreguntaCreateView.as_view(), name='tipo_pregunta_create'),
    path('tipos-pregunta/<int:pk>/editar/', dashboard_admin_preguntas.TipoPreguntaUpdateView.as_view(), name='tipo_pregunta_update'),
    path('tipos-pregunta/<int:pk>/eliminar/', dashboard_admin_preguntas.TipoPreguntaDeleteView.as_view(), name='tipo_pregunta_delete'),
    
    # Gestión de Grupos
    path('grupos/', dashboard_admin_preguntas.GrupoListView.as_view(), name='grupo_list'),
    path('grupos/crear/', dashboard_admin_preguntas.GrupoCreateView.as_view(), name='grupo_create'),
    path('grupos/<int:pk>/', dashboard_admin_preguntas.GrupoDetailView.as_view(), name='grupo_detail'),
    path('grupos/<int:pk>/editar/', dashboard_admin_preguntas.GrupoUpdateView.as_view(), name='grupo_update'),
    path('grupos/<int:pk>/eliminar/', dashboard_admin_preguntas.GrupoDeleteView.as_view(), name='grupo_delete'),
    path('grupos/<int:pk>/agregar-preguntas/', dashboard_admin_preguntas.GrupoAddPreguntasView.as_view(), name='grupo_add_preguntas'),
    
    # Gestión de Preguntas
    path('preguntas/', dashboard_admin_preguntas.PreguntaListView.as_view(), name='pregunta_list'),
    path('preguntas/crear/', dashboard_admin_preguntas.PreguntaCreateView.as_view(), name='pregunta_create'),
    path('preguntas/<int:pk>/', dashboard_admin_preguntas.PreguntaDetailView.as_view(), name='pregunta_detail'),
    path('preguntas/<int:pk>/editar/', dashboard_admin_preguntas.PreguntaUpdateView.as_view(), name='pregunta_update'),
    path('preguntas/<int:pk>/eliminar/', dashboard_admin_preguntas.PreguntaDeleteView.as_view(), name='pregunta_delete'),
]
