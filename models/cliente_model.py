from database.connection import get_db

db = get_db()
usuarios = db["usuarios"]
clientes = db["clientes"]

def crear_usuario(usuario, contraseña, rol):
    """
    Registra un nuevo usuario en la base de datos.
    Retorna True si se creó, False si ya existe.
    """
    if usuarios.find_one({"usuario": usuario}):
        return False  # Usuario ya existe
    usuarios.insert_one({"usuario": usuario, "contraseña": contraseña, "rol": rol})
    return True

def validar_usuario(usuario, contraseña):
    """
    Valida si el usuario y contraseña existen en la DB.
    """
    user = usuarios.find_one({"usuario": usuario, "contraseña": contraseña})
    return user is not None



def crear_cliente(nombre, telefono, direccion):
    doc = {"nombre": nombre, "telefono": telefono, "direccion": direccion}
    clientes.insert_one(doc)
    return True

def listar_clientes():
    return list(clientes.find({}, {"_id": 0}))
