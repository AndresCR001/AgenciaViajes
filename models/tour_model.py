from database.connection import get_db

db = get_db()
tours = db["tours"]

def crear_tour(codigo, destino, fecha_salida, fecha_llegada, plazas_totales):
    doc = {
        "codigo": codigo,
        "destino": destino,
        "fecha_salida": fecha_salida,
        "fecha_llegada": fecha_llegada,
        "plazas_totales": plazas_totales,
        "plazas_ocupadas": 0
    }
    tours.insert_one(doc)
    return True

def listar_tours():
    return list(tours.find({}, {"_id": 0}))
