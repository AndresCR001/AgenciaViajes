from database.connection import get_db

db = get_db()
usuarios = db["usuarios"]

def crear_usuario(usuario, contraseña, rol):
    if usuarios.find_one({"usuario": usuario}):
        return False
    usuarios.insert_one({"usuario": usuario, "contraseña": contraseña, "rol": rol})
    return True

def validar_usuario(usuario, contraseña):
    return usuarios.find_one({"usuario": usuario, "contraseña": contraseña})
