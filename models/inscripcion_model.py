from database.connection import get_db
from models.tour_model import obtener_tour, actualizar_plazas

db = get_db()
inscripciones = db["inscripciones"]

def inscribir_cliente(cod_cliente, cod_tour, forma_pago):
    tour = obtener_tour(cod_tour)
    if not tour:
        return "El tour no existe."
    if tour["plazas_ocupadas"] >= tour["plazas_totales"]:
        return "No hay plazas disponibles."

    inscripciones.insert_one({
        "cod_cliente": cod_cliente,
        "cod_tour": cod_tour,
        "forma_pago": forma_pago
    })

    # actualizar plazas ocupadas
    nuevas_plazas = tour["plazas_ocupadas"] + 1
    actualizar_plazas(cod_tour, nuevas_plazas)
    return "Cliente inscrito correctamente."

def listar_inscripciones():
    return list(inscripciones.find({}, {"_id": 0}))
