import flet as ft
from models.cliente_model import crear_cliente, listar_clientes

def clientes_ui(page: ft.Page, menu_ui):  # Recibimos la función del menú principal
    nombre = ft.TextField(label="Nombre")
    telefono = ft.TextField(label="Teléfono")
    direccion = ft.TextField(label="Dirección")
    resultado = ft.Text(value="")

    def guardar(e):
        crear_cliente(nombre.value, telefono.value, direccion.value)
        resultado.value = "Cliente agregado ✅"
        page.update()

    def volver(e):
        # Limpiamos la página y llamamos al menú principal
        page.controls.clear()
        menu_ui(page)
        page.update()

    boton_guardar = ft.ElevatedButton("Guardar Cliente", on_click=guardar)
    boton_volver = ft.ElevatedButton("⬅ Volver", on_click=volver)

    page.controls.clear()
    page.add(
        ft.Column([
            ft.Text("Gestión de Clientes", size=24, weight="bold"),
            nombre,
            telefono,
            direccion,
            ft.Row([boton_guardar, boton_volver], alignment="spaceBetween"),
            resultado
        ])
    )
