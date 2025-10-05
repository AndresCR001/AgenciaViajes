import flet as ft
from database.connection import get_db

db = get_db()
usuarios_col = db["usuarios"]

def registro_ui(page: ft.Page):
    page.title = "Registro de Usuario"
    page.theme_mode = "light"

    nombre_nuevo = ft.TextField(label="Usuario", width=300)
    clave_nueva = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=300)
    confirmar_clave = ft.TextField(label="Confirmar Contraseña", password=True, can_reveal_password=True, width=300)
    rol_usuario = ft.Dropdown(
        label="Rol",
        options=[
            ft.dropdown.Option("atencion", text="Encargado de atención al público"),
            ft.dropdown.Option("turismo", text="Encargado de turismo"),
            ft.dropdown.Option("gerente", text="Gerente de la empresa")
        ],
        value="atencion",
        width=300
    )
    mensaje_registro = ft.Text("", color="red")

    def guardar_nuevo(e):
        if not nombre_nuevo.value or not clave_nueva.value or not confirmar_clave.value:
            mensaje_registro.value = "Todos los campos son obligatorios ❌"
        elif clave_nueva.value != confirmar_clave.value:
            mensaje_registro.value = "Las contraseñas no coinciden ❌"
        elif usuarios_col.find_one({"usuario": nombre_nuevo.value}):
            mensaje_registro.value = "El usuario ya existe ❌"
        else:
            usuarios_col.insert_one({
                "usuario": nombre_nuevo.value,
                "contraseña": clave_nueva.value,
                "rol": rol_usuario.value
            })
            mensaje_registro.value = "Usuario registrado ✅"
        page.update()

    def volver_login(e):
        # Importación local para evitar circular import
        from ui.inicio_ui import inicio_ui
        inicio_ui(page)

    page.controls.clear()
    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Registro de Usuario", size=36, weight="bold"),
                    nombre_nuevo,
                    clave_nueva,
                    confirmar_clave,
                    rol_usuario,
                    ft.Row([
                        ft.ElevatedButton("Guardar", on_click=guardar_nuevo),
                        ft.ElevatedButton("Volver", on_click=volver_login)
                    ]),
                    mensaje_registro
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
