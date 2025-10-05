import flet as ft
from models.usuario_model import validar_usuario
from ui.menu import menu
import importlib

def inicio_ui(page: ft.Page):
    page.title = "Agencia de Viajes - Login"
    page.theme_mode = "light"

    usuario = ft.TextField(label="Usuario", width=300)
    contraseña = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=300)
    mensaje = ft.Text("", color="red")

    # Función para iniciar sesión
    def iniciar_sesion(e):
        user = validar_usuario(usuario.value, contraseña.value)
        if user:
            mensaje.value = "¡Login exitoso! ✅"
            mensaje.color = "green"
            page.update()
            page.controls.clear()
            menu(page, user)  # Pasamos el usuario para controlar permisos
        else:
            mensaje.value = "Usuario o contraseña incorrectos ❌"
            mensaje.color = "red"
            page.update()

    # Función para ir a registro de usuario
    def ir_a_registro(e):
        page.controls.clear()
        mod = importlib.import_module("ui.registro_ui")
        mod.registro_ui(page)

    page.controls.clear()
    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Inicio de Sesión", size=36, weight="bold"),
                    usuario,
                    contraseña,
                    ft.Row([
                        ft.ElevatedButton("Iniciar Sesión", on_click=iniciar_sesion, width=200),
                        ft.ElevatedButton("Registrarse", on_click=ir_a_registro, width=200)
                    ], alignment="center", spacing=20),
                    mensaje
                ],
                alignment="center",
                horizontal_alignment="center",
                spacing=20,
                tight=True
            ),
            padding=20
        )
    )
    page.update()
