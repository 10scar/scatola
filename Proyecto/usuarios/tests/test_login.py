from django.test import TestCase, Client
from django.urls import reverse
from usuarios.models import Usuario, Perfil, NivelFormacion
from usuarios.forms import PerfilUpdateForm, UserUpdateForm

class LoginTests(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.login_url = reverse("login")

    def test_login_falla_con_email_en_vez_de_username(self):

        Usuario.objects.create_user(
            username="user123",
            email="user@test.com",
            password="12345678"
        )

        response = self.client.post(self.login_url, {
            "username": "user@test.com",  # ❌ email en lugar de username
            "password": "12345678"
        })

        # Status 200 → formulario recargado con error
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Usuario o contraseña incorrectos.")

    def test_login_falla_con_password_incorrecta(self):

        Usuario.objects.create_user(
            username="userx",
            email="userx@test.com",
            password="12345678"
        )

        response = self.client.post(self.login_url, {
            "username": "userx",
            "password": "clave_incorrecta"
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Usuario o contraseña incorrectos.")


    def test_login_exitoso_redireccion(self):

        user = Usuario.objects.create_user(
            username="testlogin",
            email="log@test.com",
            password="12345678"
        )

        response = self.client.post(self.login_url, {
            "username": "testlogin",
            "password": "12345678"
        })

        self.assertRedirects(response, reverse("dashboard_estudiante"))