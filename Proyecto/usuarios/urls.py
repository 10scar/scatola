from django.urls import path
from . import views
app_name = 'usuarios'

urlpatterns = [
    # path('perfil/', views.perfil_view, name='perfil'),
    path('api/reminder-racha/', views.recuerdo_racha, name='reminder_racha'),
]