import flet as ft
from ui.main_window import main_window

def main(page: ft.Page):
    main_window(page)

ft.app(target=main)
