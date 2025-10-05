from database.connection import get_db

db = get_db()
clientes = db["clientes"]

def crear_cliente(nombre, telefono, direccion, ocupacion=""):
    doc = {"nombre": nombre, "telefono": telefono, "direccion": direccion, "ocupacion": ocupacion}
    clientes.insert_one(doc)
    return True

def listar_clientes():
    return list(clientes.find({}, {"_id": 0}))
