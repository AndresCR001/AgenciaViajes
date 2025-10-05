import flet as ft
from database.connection import get_db
from ui.menu import menu

db = get_db()
usuarios_col = db["usuarios"]

def inicio_ui(page: ft.Page):
    page.title = "Agencia de Viajes - Login"
    page.theme_mode = "light"

    usuario = ft.TextField(label="Usuario", width=300)
    contraseña = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=300)
    mensaje = ft.Text("", color="red")

    def iniciar_sesion(e):
        user = usuarios_col.find_one({"usuario": usuario.value, "contraseña": contraseña.value})
        if user:
            mensaje.value = f"¡Login exitoso! ✅ (Rol: {user['rol']})"
            mensaje.color = "green"
            page.update()
            page.controls.clear()    
            menu(page, user)
        else:
            mensaje.value = "Usuario o contraseña incorrectos ❌"
            mensaje.color = "red"
            page.update()

    def abrir_registro(e):
        # Importación local para evitar circular import
        from ui.registro_ui import registro_ui
        registro_ui(page)

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
                        ft.ElevatedButton("Registrar Usuario", on_click=abrir_registro, width=200)
                    ]),
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
