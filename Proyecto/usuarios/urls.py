from django.urls import path
from . import views
from .views import LoginView
app_name = 'usuarios'

urlpatterns = [
    path('perfil/', views.profile_details, name='profile_details'),
    path('dashboard/', views.dashboard_estudiante, name='dashboard_estudiante'),
    path('perfil-actualizar/', views.editar_perfil, name='editar_perfil')
    
]
