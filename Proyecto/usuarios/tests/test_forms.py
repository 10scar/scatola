from django.test import TestCase
from ..forms import Paso3SeguridadForm, Paso1PersonalForm
from ..models import Usuario


class TestsContraseña(TestCase):

    def _verificar_caso_test(self, caso):
        """
        Función auxiliar para verificar un caso de test.
        Crea el formulario, valida y verifica errores.
        """
        form = Paso3SeguridadForm(data=caso['data'])
        
        # Verifica que el resultado sea el esperado
        self.assertEqual(
            form.is_valid(), 
            caso['valid'], 
            f"Fallo en: {caso['descripcion']}"
        )
        
        # Verifica que el error esperado esté presente si no es válido
        if not caso['valid'] and caso.get('error'):
            self.assertIn(
                caso['error'], 
                str(form.errors), 
                f"El error '{caso['error']}' no se encontró en: {caso['descripcion']}"
            )
    
    def test_contrasenas_diferentes(self):
        casos_contrasenas_diferentes = [
            {
                'data': {'password1': 'MiContraseña123', 'password2': 'MiContraseña123'},
                'descripcion': 'Contraseñas válidas e iguales',
                'valid': True,
                'error': None
            },
            {
                'data': {'password1': 'MiContraseña123', 'password2': 'OtraContraseña456'},
                'descripcion': 'Contraseñas completamente diferentes',
                'valid': False,
                'error': 'Las contraseñas no coinciden.'
            },
            {
                'data': {'password1': 'Password123', 'password2': 'password123'},
                'descripcion': 'Diferencia en mayúsculas/minúsculas',
                'valid': False,
                'error': 'Las contraseñas no coinciden.'
            },
            {
                'data': {'password1': 'AbCdEfGh12', 'password2': 'AbCdEfGh21'},
                'descripcion': 'Solo difieren en últimos caracteres',
                'valid': False,
                'error': 'Las contraseñas no coinciden.'
            }
        ]
        
        for caso in casos_contrasenas_diferentes:
            with self.subTest(caso=caso['descripcion']):
                self._verificar_caso_test(caso)
    
    def test_contrasena_tamano_minimo(self):
        casos_tamano_invalido = [
            {
                'data': {'password1': '1234567', 'password2': '1234567'},
                'descripcion': 'Contraseña de 7 caracteres (justo debajo del mínimo)',
                'longitud': 7,
                'valid': False,
                'error': 'Ensure this value has at least 8 characters'
            },
            {
                'data': {'password1': 'abc', 'password2': 'abc'},
                'descripcion': 'Contraseña de 3 caracteres',
                'longitud': 3,
                'valid': False,
                'error': 'Ensure this value has at least 8 characters'
            },
            {
                'data': {'password1': 'A1', 'password2': 'A1'},
                'descripcion': 'Contraseña de 2 caracteres',
                'longitud': 2,
                'valid': False,
                'error': 'Ensure this value has at least 8 characters'
            },
            {
                'data': {'password1': 'P', 'password2': 'P'},
                'descripcion': 'Contraseña de 1 carácter',
                'longitud': 1,
                'valid': False,
                'error': 'Ensure this value has at least 8 characters'
            }
        ]
        
        for caso in casos_tamano_invalido:
            with self.subTest(caso=caso['descripcion']):
                self._verificar_caso_test(caso)


class TestFormularioUsuario(TestCase):
    """
    Tests para el formulario Paso1PersonalForm.
    Valida las funciones clean_username() y clean_email() que verifican
    que el username y email no estén duplicados en la base de datos.
    """
    
    def setUp(self):
        """
        Crea un usuario de prueba antes de cada test.
        Este usuario se usará para verificar la validación de duplicados.
        """
        self.usuario_existente = Usuario.objects.create_user(
            username='usuario_existente',
            email='existente@ejemplo.com',
            password='TestPass123',
            first_name='Usuario',
            last_name='Existente'
        )
    
    def test_clean_username(self):
        """
        Test para validar que clean_username() detecte usernames duplicados.
        """
        casos_username = [
            {
                'data': {
                    'username': 'usuario_nuevo',
                    'email': 'nuevo@ejemplo.com',
                    'first_name': 'Nuevo',
                    'last_name': 'Usuario'
                },
                'descripcion': 'Username válido (no existe en la base de datos)',
                'valid': True,
                'error': None
            },
            {
                'data': {
                    'username': 'usuario_existente',
                    'email': 'nuevo@ejemplo.com',
                    'first_name': 'Nuevo',
                    'last_name': 'Usuario'
                },
                'descripcion': 'Username duplicado (ya existe en la base de datos)',
                'valid': False,
                'error': 'Este nombre de usuario ya está en uso.'
            },
            {
                'data': {
                    'username': '',
                    'email': 'nuevo@ejemplo.com',
                    'first_name': 'Nuevo',
                    'last_name': 'Usuario'
                },
                'descripcion': 'Username vacío',
                'valid': False,
                'error': 'Este campo es obligatorio.'
            }
        ]
        
        for caso in casos_username:
            with self.subTest(caso=caso['descripcion']):
                form = Paso1PersonalForm(data=caso['data'])
                self.assertEqual(
                    form.is_valid(),
                    caso['valid'],
                    f"Fallo en: {caso['descripcion']}"
                )
                
                if not caso['valid'] and caso.get('error'):
                    self.assertIn(
                        caso['error'],
                        str(form.errors),
                        f"El error '{caso['error']}' no se encontró en: {caso['descripcion']}"
                    )
    
    def test_clean_email(self):
        """
        Test para validar que clean_email() detecte emails duplicados.
        """
        casos_email = [
            {
                'data': {
                    'username': 'usuario_nuevo',
                    'email': 'nuevo@ejemplo.com',
                    'first_name': 'Nuevo',
                    'last_name': 'Usuario'
                },
                'descripcion': 'Email válido (no existe en la base de datos)',
                'valid': True,
                'error': None
            },
            {
                'data': {
                    'username': 'usuario_nuevo',
                    'email': 'existente@ejemplo.com',
                    'first_name': 'Nuevo',
                    'last_name': 'Usuario'
                },
                'descripcion': 'Email duplicado (ya existe en la base de datos)',
                'valid': False,
                'error': 'Este correo electrónico ya está registrado.'
            },
            {
                'data': {
                    'username': 'usuario_nuevo',
                    'email': 'correo_invalido',
                    'first_name': 'Nuevo',
                    'last_name': 'Usuario'
                },
                'descripcion': 'Email con formato inválido',
                'valid': False,
                'error': 'Introduzca una dirección de correo electrónico válida.'
            },
            {
                'data': {
                    'username': 'usuario_nuevo',
                    'email': '',
                    'first_name': 'Nuevo',
                    'last_name': 'Usuario'
                },
                'descripcion': 'Email vacío',
                'valid': False,
                'error': 'Este campo es obligatorio.'
            }
        ]
        
        for caso in casos_email:
            with self.subTest(caso=caso['descripcion']):
                form = Paso1PersonalForm(data=caso['data'])
                self.assertEqual(
                    form.is_valid(),
                    caso['valid'],
                    f"Fallo en: {caso['descripcion']}"
                )
                
                if not caso['valid'] and caso.get('error'):
                    self.assertIn(
                        caso['error'],
                        str(form.errors),
                        f"El error '{caso['error']}' no se encontró en: {caso['descripcion']}"
                    )

