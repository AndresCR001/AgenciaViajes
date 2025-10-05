from database.connection import get_db

db = get_db()
clientes = db["clientes"]

def crear_cliente(nombre, telefono, direccion):
    doc = {"nombre": nombre, "telefono": telefono, "direccion": direccion}
    clientes.insert_one(doc)
    return True

def listar_clientes():
    return list(clientes.find({}, {"_id": 0}))
