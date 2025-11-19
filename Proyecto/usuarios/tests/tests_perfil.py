from django.test import TestCase, Client
from django.urls import reverse
from usuarios.models import Usuario, Perfil, NivelFormacion
from usuarios.forms import PerfilUpdateForm, UserUpdateForm
# Create your tests here.

class PerfilSecurityTest(TestCase):

    def setUp(self):
        self.client = Client()

        self.usuario1 = Usuario.objects.create_user(
            username="user1", email="u1@gmail.com", password="12345678"
        )
        self.usuario2 = Usuario.objects.create_user(
            username="user2", email="u2@gmail.com", password="12345678"
        )

        Perfil.objects.create(usuario=self.usuario1, edad=20)
        Perfil.objects.create(usuario=self.usuario2, edad=30)

    def test_usuario_no_puede_modificar_otro_perfil(self):

        self.client.login(username="user1", password="12345678")

        response = self.client.post(
            reverse("usuarios:editar_perfil"),
            {
                "edad": 9999,
                "institucion": "Hackeado",
                "nivel_formacion": "",
            }
        )

        usuario2_perfil = Perfil.objects.get(usuario=self.usuario2)

        self.assertNotEqual(usuario2_perfil.edad, 9999)
        self.assertNotEqual(usuario2_perfil.institucion, "Hackeado")

class PerfilFormTests(TestCase):

    def test_edad_fuera_de_rango(self):

        form = PerfilUpdateForm(data={"edad": 150})
        self.assertFalse(form.is_valid())
        self.assertIn("edad", form.errors)

    def test_edad_valida(self):
        form = PerfilUpdateForm(data={
            "edad": 20
        })

        self.assertTrue(form.is_valid())

    def test_email_unico(self):

        u1 = Usuario.objects.create_user("user1", email="a@gmail.com", password="x12345678")
        u2 = Usuario.objects.create_user("user2", email="b@gmail.com", password="x12345678")

        form = UserUpdateForm(
            data={"first_name": "Nuevo", "email": "a@gmail.com"},
            instance=u2
        )

        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors)

class EditarPerfilViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = Usuario.objects.create_user(
            username="user", email="user@gmail.com", password="12345678"
        )
        self.nivel = NivelFormacion.objects.create(nombre="Universitario")

    def test_crea_perfil_si_no_existe(self):

        self.client.login(username="user", password="12345678")

        self.assertFalse(Perfil.objects.filter(usuario=self.user).exists())

        self.client.get(reverse("usuarios:editar_perfil"))

        self.assertTrue(Perfil.objects.filter(usuario=self.user).exists())

    def test_actualizacion_exitosa(self):

        self.client.login(username="user", password="12345678")

        response = self.client.post(reverse("usuarios:editar_perfil"), {
            "first_name": "NuevoNombre",
            "email": "nuevo@gmail.com",
            "edad": 22,
            "institucion": "Testeo",
            "nivel_formacion": self.nivel.id,
        })

        self.assertRedirects(response, reverse("usuarios:profile_details"))

        perfil = Perfil.objects.get(usuario=self.user)
        self.assertEqual(perfil.edad, 22)
        self.assertEqual(perfil.institucion, "Testeo")

    def test_actualizacion_invalida(self):
        """
        Caso límite:
        - POST inválido → NO guardar cambios.
        """

        self.client.login(username="user", password="12345678")

        Perfil.objects.create(usuario=self.user, edad=20)

        response = self.client.post(reverse("usuarios:editar_perfil"), {
            "edad": 200,  # Inválido
        })

        perfil = Perfil.objects.get(usuario=self.user)
        self.assertEqual(perfil.edad, 20)  # No cambió

        self.assertEqual(response.status_code, 200)  # Volvió al formulario


