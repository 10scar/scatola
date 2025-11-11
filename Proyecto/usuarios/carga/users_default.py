from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

def poblar_datos():
    User = get_user_model()

    # --- Crear usuario administrador ---
    if not User.objects.filter(username="admin").exists():
        admin_user = User.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="admin123",
            first_name="oscar",
            last_name="User"
        )
        admin_group = Group.objects.get(name="Administrador")
        admin_user.groups.add(admin_group)
        print("Usuario administrador creado y asignado al grupo 'Administrador'.")

    # --- Crear usuario estudiante ---
    if not User.objects.filter(username="estudiante").exists():
        student_user = User.objects.create_user(
            username="estudiante",
            email="estudiante@example.com",
            password="estudiante123",
            first_name="Estudiante",
            last_name="Demo"
        )
        student_group = Group.objects.get(name="Estudiante")
        student_user.groups.add(student_group)
        print("Usuario estudiante creado y asignado al grupo 'Estudiante'.")