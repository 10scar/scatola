from django.urls import path
from preguntas.views import dashboard_admin

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
    
    # Gestión de Temarios (Asociación Tema-Componente)
    path('temarios/', dashboard_admin.TemarioIndexView.as_view(), name='temario_index'),
    path('temarios/tipo-examen/<int:tipo_id>/', dashboard_admin.ComponenteListView.as_view(), name='componente_list'),
    path('temarios/componente/<int:comp_id>/', dashboard_admin.TemarioDetailView.as_view(), name='temario_detail'),
    path('temarios/componente/<int:comp_id>/agregar/', dashboard_admin.TemarioAddTemasView.as_view(), name='temario_add_temas'),
    path('temarios/componente/<int:comp_id>/eliminar/<int:tema_id>/', dashboard_admin.TemarioRemoveTemaView.as_view(), name='temario_remove_tema'),
]
