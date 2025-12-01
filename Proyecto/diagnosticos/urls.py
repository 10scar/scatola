from django.urls import path
from . import views

app_name = 'diagnosticos'

urlpatterns = [
    path('', views.iniciar_prueba, name='iniciar'),
    path('<int:prueba_id>/pregunta/<int:pregunta_num>/', views.ver_pregunta, name='ver_pregunta'),
    path('<int:prueba_id>/responder/', views.guardar_respuesta, name='guardar_respuesta'),
    path('<int:prueba_id>/finalizar/', views.finalizar_prueba, name='finalizar'),
]