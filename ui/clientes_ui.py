import flet as ft
from models.cliente_model import crear_cliente, listar_clientes

def clientes_ui(page: ft.Page, menu_ui, user):
    nombre = ft.TextField(label="Nombre")
    telefono = ft.TextField(label="Teléfono")
    direccion = ft.TextField(label="Dirección")
    resultado = ft.Text(value="")

    def guardar(e):
        if user["rol"].lower() != "atencion":
            ft.alert("No tiene permisos para registrar clientes")
            return
        crear_cliente(nombre.value, telefono.value, direccion.value)
        resultado.value = "Cliente agregado ✅"
        page.update()

    def refrescar(e):
        data = listar_clientes()
        items = [ft.Text(f"{c['nombre']} | {c['telefono']} | {c['direccion']}") for c in data]
        tabla.controls = items
        page.update()

    def volver(e):
        page.controls.clear()
        menu_ui(page, user)
        page.update()

    boton_guardar = ft.ElevatedButton("Guardar Cliente", on_click=guardar)
    boton_refrescar = ft.ElevatedButton("Refrescar Lista", on_click=refrescar)
    boton_volver = ft.ElevatedButton("⬅ Volver", on_click=volver)

    tabla = ft.Column()

    page.controls.clear()
    page.add(
        ft.Column([
            ft.Text("Gestión de Clientes", size=24, weight="bold"),
            nombre,
            telefono,
            direccion,
            ft.Row([boton_guardar, boton_refrescar, boton_volver], alignment="spaceBetween"),
            ft.Divider(),
            ft.Text("Lista de Clientes:", size=18, weight="bold"),
            tabla,
            resultado
        ])
    )
    page.update()
