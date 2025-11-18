
app_name = 'usuarios'

urlpatterns = [
    # Vista de prueba
    path('hola/', views.hola_mundo, name='hola_mundo'),
    path('perfil/', views.profile_details, name='profile_details'),
    path('dashboard/', views.dashboard_estudiante, name='dashboard_estudiante'),
    path('perfil-actualizar/', views.editar_perfil, name='editar_perfil')
    
]
