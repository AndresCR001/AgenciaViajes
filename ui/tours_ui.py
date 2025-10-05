import flet as ft
from models.tour_model import crear_tour, listar_tours

def tours_ui(page: ft.Page, menu_ui):  # Recibimos menu_ui para retroceder
    codigo = ft.TextField(label="Código del Tour")
    destino = ft.TextField(label="Destino")
    fecha_salida = ft.TextField(label="Fecha de salida (YYYY-MM-DD)")
    fecha_llegada = ft.TextField(label="Fecha de llegada (YYYY-MM-DD)")
    plazas_totales = ft.TextField(label="Plazas Totales", input_filter=ft.NumbersOnlyInputFilter())

    resultado = ft.Text("")

    def guardar(e):
        crear_tour(
            codigo.value,
            destino.value,
            fecha_salida.value,
            fecha_llegada.value,
            int(plazas_totales.value)
        )
        resultado.value = "Tour registrado ✅"
        page.update()

    def refrescar(e):
        data = listar_tours()
        items = [
            ft.Text(f"{t['codigo']} | {t['destino']} | {t['plazas_ocupadas']}/{t['plazas_totales']} plazas")
            for t in data
        ]
        tabla.controls = items
        page.update()

    def volver(e):
        page.controls.clear()
        menu_ui(page)
        page.update()

    tabla = ft.Column()
    boton_volver = ft.ElevatedButton("⬅ Volver", on_click=volver)

    page.controls.clear()
    page.add(
        ft.Column([
            ft.Row([ft.Text("Gestión de Tours", size=24, weight="bold"), boton_volver], alignment="spaceBetween"),
            codigo,
            destino,
            fecha_salida,
            fecha_llegada,
            plazas_totales,
            ft.Row([
                ft.ElevatedButton("Guardar Tour", on_click=guardar),
                ft.ElevatedButton("Refrescar Lista", on_click=refrescar)
            ]),
            resultado,
            ft.Divider(),
            ft.Text("Lista de Tours:", size=18, weight="bold"),
            tabla
        ])
    )
