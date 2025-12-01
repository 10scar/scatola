from django.urls import path
from . import views
from .views import LoginView
app_name = 'usuarios'

urlpatterns = [
    # path('perfil/', views.perfil_view, name='perfil'),
    path('api/reminder-racha/', views.recuerdo_racha, name='reminder_racha'),

    path('perfil/', views.profile_details, name='profile_details'),
    path('dashboard/', views.dashboard_estudiante, name='dashboard_estudiante'),
    path('perfil-actualizar/', views.editar_perfil, name='editar_perfil'),
    path('Perfil-rutas/', views.editar_ruta_usuario, name='ver_rutas'),
    path('preguntar-prueba-diagnostica/', views.preguntar_prueba_diagnostica, name='preguntar_prueba_diagnostica'),
]
