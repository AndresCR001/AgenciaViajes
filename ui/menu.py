import flet as ft
import importlib

from ui.clientes_ui import clientes_ui
from ui.tours_ui import tours_ui
from ui.reportes_ui import reportes_ui
from ui.inscripciones_ui import inscripciones_ui

def menu(page: ft.Page, user: dict):
    page.title = "Agencia de Viajes - Sistema"
    page.theme_mode = "light"

    controles = [ft.Text(f"Bienvenido {user['usuario']} - Rol: {user['rol']}", size=20)]
    rol = user.get("rol", "").lower()

    # Función para abrir UI dinámicamente
    def abrir_ui(modulo: str, funcion: str):
        mod = importlib.import_module(modulo)
        func = getattr(mod, funcion)
        # Si es inicio_ui, solo le pasamos page
        if funcion == "inicio_ui":
            func(page)
        else:
            func(page, menu, user)


    if rol == "atencion":
        controles.append(ft.ElevatedButton("Clientes", on_click=lambda e: clientes_ui(page, menu, user)))
        controles.append(ft.ElevatedButton("Inscripciones a Tours",
                                          on_click=lambda e: abrir_ui("ui.inscripciones_ui", "inscripciones_ui")))

    if rol == "turismo":
        controles.append(ft.ElevatedButton("Gestión de Tours", on_click=lambda e: tours_ui(page, menu, user)))
        controles.append(ft.ElevatedButton("Informe de Tours",
                                          on_click=lambda e: abrir_ui("ui.reportes_ui", "reportes_ui")))

    if rol == "gerente":
        controles.append(ft.ElevatedButton("Reportes del Gerente", 
                                           on_click=lambda e: reportes_ui(page, menu, user)))

    # Botón de logout
    controles.append(ft.ElevatedButton("Cerrar Sesión",
                                       on_click=lambda e: abrir_ui("ui.inicio_ui", "inicio_ui")))

    page.controls.clear()
    page.add(ft.Column(controles, alignment="center", spacing=20))
    page.update()
