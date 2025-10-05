import flet as ft
from models.usuario_model import crear_usuario
import importlib

def registro_ui(page: ft.Page):
    page.title = "Agencia de Viajes - Registro de Usuario"
    page.theme_mode = "light"

    usuario = ft.TextField(label="Usuario", width=300)
    contraseña = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=300)
    rol = ft.Dropdown(
        label="Rol del Usuario",
        width=300,
        options=[
            ft.dropdown.Option("atencion", "Encargado de atención al público"),
            ft.dropdown.Option("turismo", "Encargado de turismo"),
            ft.dropdown.Option("gerente", "Gerente de la empresa")
        ]
    )
    mensaje = ft.Text("", color="red")

    # Función para registrar usuario
    def registrar(e):
        success = crear_usuario(usuario.value, contraseña.value, rol.value)
        if success:
            mensaje.value = "Usuario registrado ✅"
            mensaje.color = "green"
            page.update()
        else:
            mensaje.value = "El usuario ya existe ❌"
            mensaje.color = "red"
            page.update()

    # Función para volver al login sin causar circular import
    def volver_al_login(e):
        page.controls.clear()
        mod = importlib.import_module("ui.inicio_ui")
        mod.inicio_ui(page)

    page.controls.clear()
    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Registro de Usuario", size=36, weight="bold"),
                    usuario,
                    contraseña,
                    rol,
                    ft.Row([
                        ft.ElevatedButton("Registrar", on_click=registrar, width=200),
                        ft.ElevatedButton("Volver al Login", on_click=volver_al_login)
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
