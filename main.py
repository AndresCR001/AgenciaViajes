import flet as ft
from ui.inicio_ui import inicio_ui

def main(page: ft.Page):
    inicio_ui(page)

ft.app(target=main)
