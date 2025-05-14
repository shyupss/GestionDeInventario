from pymongo import MongoClient
from random import choice

eventos: list = []
posibles_eventos: list = [
    "venta_realizada", 
    "stock_bajo", 
    "producto_agotado", 
    "nueva_compra", 
    "producto_agregado", 
    "usuario_creado", 
    "login_fallido"
]

def crear_eventos():

    for i in range(100):
        evento = {}
        evento_seleccionado = choice(posibles_eventos)
        print(f"Se va a registrar un evento {evento_seleccionado}")


def main():
    # global coleccion_evento

    # client = MongoClient("mongodb://localhost:27017/")
    # db_eventos = client["eventos_emprendimiento"]
    # coleccion_evento = db_eventos["eventos"]
    crear_eventos()


if __name__ == "__main__":
    main()