from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    # Vista de prueba
    path('hola/', views.hola_mundo, name='hola_mundo'),
]
