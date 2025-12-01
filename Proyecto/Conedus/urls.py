"""
URL configuration for Conedus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from usuarios import views
from rutas import views as rutas_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('usuarios/', include('usuarios.urls', namespace='usuarios')),
    path('', views.landing_view, name='landing'),

    # Registro
    path('registro/', views.RegistroWizard.as_view(), name='registro'),
    # Autenticación
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    # Dashboard
    path('dashboard/estudiante/', views.dashboard_estudiante, name='dashboard_estudiante'),
    path('dashboard/admin/', views.DashboardAdminView.as_view(), name='dashboard_admin'),
    # Prueba Diagnóstica
    path('diagnosticos/', include('diagnosticos.urls', namespace='diagnosticos')),
    # Gestión de Temas y Contenidos (Admin)
    path('dashboard/admin/', include('preguntas.urls_admin')),

    # Preguntas Diarias
    path('preguntas-diarias/', rutas_views.preguntas_diarias_view, name='preguntas_diarias'),
    path('preguntas-diarias/responder/', rutas_views.guardar_respuesta_diaria, name='guardar_respuesta_diaria'),
]
