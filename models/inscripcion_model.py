from database.connection import get_db

db = get_db()
inscripciones = db["inscripciones"]
tours = db["tours"]
clientes = db["clientes"]

def crear_inscripcion(cod_cliente, cod_tour, forma_pago):
    cliente = clientes.find_one({"nombre": cod_cliente})
    tour = tours.find_one({"codigo": cod_tour})
    if not cliente or not tour:
        return False
    if tour.get("plazas_ocupadas", 0) >= tour.get("plazas_totales", 0):
        return False
    inscripciones.insert_one({
        "cod_cliente": cod_cliente,
        "cod_tour": cod_tour,
        "forma_pago": forma_pago
    })
    tours.update_one({"codigo": cod_tour}, {"$inc": {"plazas_ocupadas": 1}})
    return True

def listar_inscripciones():
    return list(inscripciones.find({}, {"_id": 0}))

def eliminar_inscripcion(cod_cliente, cod_tour):
    result = inscripciones.delete_one({"cod_cliente": cod_cliente, "cod_tour": cod_tour})
    if result.deleted_count > 0:
        tours.update_one({"codigo": cod_tour}, {"$inc": {"plazas_ocupadas": -1}})
        return True
    return False

def actualizar_inscripcion(cod_cliente, cod_tour, nueva_forma_pago):
    result = inscripciones.update_one(
        {"cod_cliente": cod_cliente, "cod_tour": cod_tour},
        {"$set": {"forma_pago": nueva_forma_pago}}
    )
    return result.modified_count > 0
