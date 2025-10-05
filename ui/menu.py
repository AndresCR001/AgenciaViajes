import flet as ft
from ui.clientes_ui import clientes_ui
from ui.tours_ui import tours_ui
from ui.reportes_ui import reportes_ui

def menu(page: ft.Page,user):
    page.title = "Agencia de Viajes - Sistema"
    page.theme_mode = "light"

    # Pasamos menu como menu_ui para que los submenus puedan volver
    def abrir_clientes(e): clientes_ui(page, menu)
    def abrir_tours(e): tours_ui(page, menu)
    def abrir_reportes(e): reportes_ui(page, menu)

    page.controls.clear()  # Limpiar la página antes de agregar los controles
    page.add(
        ft.Column([
            ft.Text("Agencia de Viajes", size=30, weight="bold"),
            ft.ElevatedButton("Clientes", on_click=abrir_clientes),
            ft.ElevatedButton("Tours", on_click=abrir_tours),
            ft.ElevatedButton("Reportes (Gerente)", on_click=abrir_reportes)
        ])
    )
    page.update()
