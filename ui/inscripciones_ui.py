import flet as ft
from models.inscripcion_model import crear_inscripcion, listar_inscripciones, eliminar_inscripcion, actualizar_inscripcion
from models.cliente_model import listar_clientes
from models.tour_model import listar_tours

def inscripciones_ui(page: ft.Page, menu_ui, user):
    if user["rol"].lower() != "atencion":
        ft.alert("No tiene permisos para gestionar inscripciones")
        return

    cod_cliente = ft.Dropdown(label="Cliente", width=300,
                              options=[ft.dropdown.Option(c["nombre"]) for c in listar_clientes()])
    cod_tour = ft.Dropdown(label="Tour", width=300,
                           options=[ft.dropdown.Option(t["codigo"]) for t in listar_tours()])
    forma_pago = ft.Dropdown(label="Forma de Pago", width=300,
                             options=[
                                 ft.dropdown.Option("contado"),
                                 ft.dropdown.Option("tarjeta"),
                                 ft.dropdown.Option("cuotas")
                             ])
    resultado = ft.Text("")

    def registrar(e):
        if crear_inscripcion(cod_cliente.value, cod_tour.value, forma_pago.value):
            resultado.value = "Inscripción registrada ✅"
        else:
            resultado.value = "No se pudo registrar la inscripción ❌ (tour lleno o cliente no existe)"
        refrescar(None)
        page.update()

    def eliminar(e):
        if eliminar_inscripcion(cod_cliente.value, cod_tour.value):
            resultado.value = "Inscripción eliminada ✅"
        else:
            resultado.value = "No se pudo eliminar la inscripción ❌"
        refrescar(None)
        page.update()

    def modificar(e):
        if actualizar_inscripcion(cod_cliente.value, cod_tour.value, forma_pago.value):
            resultado.value = "Inscripción actualizada ✅"
        else:
            resultado.value = "No se pudo actualizar la inscripción ❌"
        refrescar(None)
        page.update()

    def refrescar(e):
        data = listar_inscripciones()
        tabla.controls.clear()
        for i in data:
            tabla.controls.append(ft.Text(f"{i['cod_cliente']} | {i['cod_tour']} | {i['forma_pago']}"))
        page.update()

    def volver(e):
        page.controls.clear()
        menu_ui(page, user)
        page.update()

    tabla = ft.Column()
    boton_volver = ft.ElevatedButton("⬅ Volver", on_click=volver)

    page.controls.clear()
    page.add(
        ft.Column([
            ft.Row([ft.Text("Gestión de Inscripciones", size=24, weight="bold"), boton_volver], alignment="spaceBetween"),
            cod_cliente,
            cod_tour,
            forma_pago,
            ft.Row([
                ft.ElevatedButton("Registrar", on_click=registrar),
                ft.ElevatedButton("Eliminar", on_click=eliminar),
                ft.ElevatedButton("Modificar", on_click=modificar)
            ], alignment="spaceBetween"),
            ft.Divider(),
            ft.Text("Inscripciones existentes:", size=18, weight="bold"),
            tabla,
            resultado
        ])
    )
    refrescar(None)
