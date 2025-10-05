from pymongo import MongoClient

def get_db():
    try:
        # Conexión local (asegúrate que MongoDB esté corriendo)
        client = MongoClient("mongodb://localhost:27017/")
        db = client["agencia_viajes_db"]
        return db
    except Exception as e:
        print("Error al conectar a MongoDB:", e)
        return None
