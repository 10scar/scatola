from django.test import TestCase, RequestFactory
from django.contrib.auth.models import Group
from django.contrib.messages import get_messages
from django.shortcuts import reverse


from usuarios.models import Usuario
from preguntas.models import Tema, Componente, TipoExamen, Temario
from preguntas.views.dashboard_admin import AdminRequiredMixin, TemarioAddTemasView


class TestAdminRequiredMixin(TestCase):
    """
    Tests para AdminRequiredMixin.
    Valida que el mixin verifique correctamente los permisos de administrador
    y redirija apropiadamente según el estado de autenticación del usuario.
    """
    
    def setUp(self):
        """
        Configura el entorno de prueba antes de cada test.
        Crea usuarios con y sin permisos de administrador.
        """
        self.factory = RequestFactory()
        
        # Obtener o crear grupo de Administrador
        self.grupo_admin, _ = Group.objects.get_or_create(name='Administrador')
        
        # Crear usuario administrador
        self.usuario_admin = Usuario.objects.create_user(
            username='admin_user',
            email='admin@test.com',
            password='AdminPass123',
            first_name='Admin',
            last_name='User'
        )
        self.usuario_admin.groups.add(self.grupo_admin)
        
        # Crear usuario normal (sin permisos de admin)
        self.usuario_normal = Usuario.objects.create_user(
            username='normal_user',
            email='normal@test.com',
            password='NormalPass123',
            first_name='Normal',
            last_name='User'
        )
        
        # Crear una vista de prueba que use el mixin
        class TestView(AdminRequiredMixin):
            def get(self, request):
                return "OK"
        
        self.test_view = TestView()
    
    def test_verificar_permisos_administrador(self):
        
        from django.contrib.auth.models import AnonymousUser
        
        casos_permisos = [
            {
                'descripcion': 'Usuario autenticado con permisos de administrador',
                'usuario': self.usuario_admin,
                'expected_result': True
            },
            {
                'descripcion': 'Usuario autenticado sin permisos de administrador',
                'usuario': self.usuario_normal,
                'expected_result': False
            },
            {
                'descripcion': 'Usuario no autenticado (anónimo)',
                'usuario': AnonymousUser(),
                'expected_result': False
            }
        ]
        
        for caso in casos_permisos:
            with self.subTest(caso=caso['descripcion']):
                request = self.factory.get('/admin/')
                request.user = caso['usuario']
                self.test_view.request = request
                
                resultado = self.test_view.test_func()
                
                self.assertEqual(
                    resultado,
                    caso['expected_result'],
                    f"Fallo en: {caso['descripcion']}"
                )


class TestTemarioAddTemasView(TestCase):
    """
    Tests para TemarioAddTemasView.
    Valida la funcionalidad de agregar múltiples temas a un componente,
    incluyendo bulk_create y manejo de duplicados.
    """
    
    def setUp(self):
        """
        Configura el entorno de prueba antes de cada test.
        Crea tipos de examen, componentes y temas necesarios.
        """
        # Obtener o crear grupo de Administrador
        self.grupo_admin, _ = Group.objects.get_or_create(name='Administrador')
        
        # Crear usuario administrador
        self.usuario_admin = Usuario.objects.create_user(
            username='admin_user',
            email='admin@test.com',
            password='AdminPass123',
            first_name='Admin',
            last_name='User'
        )
        self.usuario_admin.groups.add(self.grupo_admin)
        
        # Crear tipo de examen
        self.tipo_examen = TipoExamen.objects.create(
            nombre='Saber 11'
        )
        
        # Crear componente
        self.componente = Componente.objects.create(
            tipo_examen=self.tipo_examen,
            nombre='Matemáticas',
            prioridad=1
        )
        
        # Crear temas
        self.tema1 = Tema.objects.create(
            nombre='Álgebra',
            descripcion='Tema de álgebra',
            prioridad=1
        )
        
        self.tema2 = Tema.objects.create(
            nombre='Geometría',
            descripcion='Tema de geometría',
            prioridad=2
        )
        
        self.tema3 = Tema.objects.create(
            nombre='Trigonometría',
            descripcion='Tema de trigonometría',
            prioridad=3
        )
    
    def test_agregar_temas_a_componente(self):
        casos_agregar_temas = [
            {
                'descripcion': 'Agregar un solo tema al componente',
                'temas': lambda: [self.tema1],
                'setup': lambda: Temario.objects.filter(componente=self.componente).delete(),
                'expected_count': 1,
                'expected_message': '1 tema(s) agregado(s)',
                'verify_message': True
            },
            {
                'descripcion': 'Agregar múltiples temas al componente',
                'temas': lambda: [self.tema2, self.tema3],
                'setup': lambda: Temario.objects.filter(componente=self.componente).delete(),
                'expected_count': 2,
                'expected_message': '2 tema(s) agregado(s)',
                'verify_message': True
            },
            {
                'descripcion': 'Agregar tema que ya existe (bulk_create con ignore_conflicts)',
                'temas': lambda: [self.tema2],  # tema2 ya estará asociado por el setup
                'setup': lambda: (
                    Temario.objects.filter(componente=self.componente).delete(),
                    Temario.objects.create(tema=self.tema2, componente=self.componente)
                ),
                'expected_count': 1,  # No se duplica
                'expected_message': '1 tema(s) agregado(s)',
                'verify_message': True,
                'verify_no_duplicates': True  # Verificar que no se duplicó el tema2
            },
            {
                'descripcion': 'No seleccionar ningún tema (formulario vacío)',
                'temas': lambda: [],
                'setup': lambda: Temario.objects.filter(componente=self.componente).delete(),
                'expected_count': 0,
                'expected_message': 'No se seleccionó ningún tema',
                'verify_message': True
            }
        ]
        
        for caso in casos_agregar_temas:
            with self.subTest(caso=caso['descripcion']):
                # Ejecutar setup específico del caso
                if 'setup' in caso:
                    caso['setup']()
                
                # Login como administrador
                self.client.login(username='admin_user', password='AdminPass123')
                
                # Obtener los temas a agregar
                temas = caso['temas']()
                
                if caso.get('verify_no_duplicates'):
                    data = {'temas': [self.tema1.id]}
                    expected_final_count = 2  # tema1 + tema2 (ya existente)
                elif temas:
                    data = {'temas': [tema.id for tema in temas]}
                    expected_final_count = caso['expected_count']
                else:
                    data = {}
                    expected_final_count = caso['expected_count']
                
                # Hacer POST a la vista
                url = reverse('dashboard_admin:temario_add_temas', kwargs={'comp_id': self.componente.pk})
                response = self.client.post(url, data)
                
                # Verificar redirección exitosa
                self.assertEqual(
                    response.status_code,
                    302,
                    f"La vista debería redirigir en: {caso['descripcion']}"
                )
                
                # Verificar el conteo de temas
                count = Temario.objects.filter(componente=self.componente).count()
                self.assertEqual(
                    count,
                    expected_final_count,
                    f"Número de temas incorrecto en: {caso['descripcion']}"
                )
                
                # Verificar mensaje esperado
                if caso.get('verify_message'):
                    messages = list(get_messages(response.wsgi_request))
                    self.assertTrue(
                        any(caso['expected_message'] in str(m) for m in messages),
                        f"Mensaje '{caso['expected_message']}' no encontrado en: {caso['descripcion']}"
                    )


