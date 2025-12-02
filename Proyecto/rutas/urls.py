from django.urls import path
from . import views

app_name = 'rutas'

urlpatterns = [
    path('mi-ruta/', views.listar_lecciones, name='listar_lecciones'),
    path('leccion/<int:leccion_id>/', views.ver_leccion, name='ver_leccion'),
    path('continuar/', views.continuar_leccion_vigente, name='continuar_leccion'),
]