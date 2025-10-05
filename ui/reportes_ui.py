import flet as ft
from database.connection import get_db

db = get_db()

def reportes_ui(page: ft.Page, menu_ui):  # Recibimos menu_ui para retroceder
    resultado = ft.Column()

    def clientes_en_cuotas(e):
        data = list(db["inscripciones"].find({"forma_pago": "cuotas"}, {"_id": 0}))
        resultado.controls.clear()
        resultado.controls.append(ft.Text("Clientes que pagaron en cuotas:", size=18, weight="bold"))
        resultado.controls += [ft.Text(str(i)) for i in data]
        page.update()

    def clientes_frecuentes(e):
        cantidad = int(input_viajes.value)
        pipeline = [
            {"$group": {"_id": "$cod_cliente", "total_viajes": {"$sum": 1}}},
            {"$match": {"total_viajes": {"$gt": cantidad}}}
        ]
        data = list(db["inscripciones"].aggregate(pipeline))
        resultado.controls.clear()
        resultado.controls.append(ft.Text(f"Clientes con más de {cantidad} viajes:", size=18, weight="bold"))
        resultado.controls += [ft.Text(str(i)) for i in data]
        page.update()

    def plazas_disponibles(e):
        cod_tour = input_tour.value
        tour = db["tours"].find_one({"codigo": cod_tour}, {"_id": 0})
        resultado.controls.clear()
        if tour:
            disp = tour["plazas_totales"] - tour["plazas_ocupadas"]
            resultado.controls.append(ft.Text(f"Plazas disponibles en {cod_tour}: {disp}", size=18))
        else:
            resultado.controls.append(ft.Text("Tour no encontrado.", color="red"))
        page.update()

    def volver(e):
        page.controls.clear()
        menu_ui(page)
        page.update()

    input_viajes = ft.TextField(label="Cantidad mínima de viajes", width=200)
    input_tour = ft.TextField(label="Código del tour", width=200)

    boton_volver = ft.ElevatedButton("⬅ Volver", on_click=volver)

    page.controls.clear()
    page.add(
        ft.Column([
            ft.Row([ft.Text("Reportes del Gerente", size=24, weight="bold"), boton_volver], alignment="spaceBetween"),
            ft.ElevatedButton("Clientes que pagan en cuotas", on_click=clientes_en_cuotas),
            ft.Row([input_viajes, ft.ElevatedButton("Buscar clientes frecuentes", on_click=clientes_frecuentes)]),
            ft.Row([input_tour, ft.ElevatedButton("Consultar plazas disponibles", on_click=plazas_disponibles)]),
            ft.Divider(),
            resultado
        ])
    )
