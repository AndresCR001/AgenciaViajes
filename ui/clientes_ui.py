import flet as ft
from models.cliente_model import crear_cliente, listar_clientes

def clientes_ui(page: ft.Page):
    nombre = ft.TextField(label="Nombre")
    telefono = ft.TextField(label="Teléfono")
    direccion = ft.TextField(label="Dirección")
    resultado = ft.Text(value="")

    def guardar(e):
        crear_cliente(nombre.value, telefono.value, direccion.value)
        resultado.value = "Cliente agregado ✅"
        page.update()

    boton = ft.ElevatedButton("Guardar Cliente", on_click=guardar)

    page.controls.clear()
    page.add(
        ft.Column([
            ft.Text("Gestión de Clientes", size=24, weight="bold"),
            nombre,
            telefono,
            direccion,
            boton,
            resultado
        ])
    )
