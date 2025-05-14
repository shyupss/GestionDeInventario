from pymongo import MongoClient
from random import choice, randint
from faker import Faker

fake = Faker()
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


def llenar_formulario(evento: str, id: int) -> dict[str, str]:
    match evento:
            case "venta_realizada":
                return {
                    "id_evento": id,
                    "tipo_evento": "venta_realizada",
                    "fecha_hora": f"{fake.date()} {fake.time()}",
                    "mensaje": "Se realizó una venta",
                    "precio_total": float(fake.pydecimal(left_digits = 5, right_digits = 2, positive = True)),
                    "vendedor": fake.name(),
                    "id_venta": id + randint(1, 200)
                }
            case "stock_bajo":
                return {
                    "id_evento": id,
                    "tipo_evento": "stock_bajo",
                    "fecha_hora": f"{fake.date()} {fake.time()}",
                    "mensaje": "El stock está bajo el mínimo",
                    "id_producto": id + randint(1, 500),
                    "stock": 50
                }
            case "producto_agotado":
                return {
                    "id_evento": id,
                    "tipo_evento": "producto_agotado",
                    "fecha_hora": f"{fake.date()} {fake.time()}",
                    "mensaje": "Stock llegó a cero",
                    "id_producto": id + randint(1, 500)
                }
            case "nueva_compra":
                return {
                    "id_evento": id,
                    "tipo_evento": "nueva_compra",
                    "fecha_hora": f"{fake.date()} {fake.time()}",
                    "mensaje": "Se registró una compra de proveedor",
                    "id_proveedor": id + randint(1, 200),
                    "id_compra": id + randint(1, 500)
                }
            case "producto_agregado":
                return {
                    "id_evento": id,
                    "tipo_evento": "producto_agregado",
                    "fecha_hora": f"{fake.date()} {fake.time()}",
                    "mensaje": "Se agregó un nuevo producto",
                    "id_producto": id + randint(1, 500),
                    "id_categoria": randint(1, 20)
                }
            case "usuario_creado":
                return {
                    "id_evento": id,
                    "tipo_evento": "usuario_creado",
                    "fecha_hora": f"{fake.date()} {fake.time()}",
                    "mensaje": "Se agregó un nuevo trabajador",
                    "id_trabajador": id + randint(1, 200),
                    "rol": choice(["vendedor", "conserje", "marketing", "ingeniero", "administrador"])
                }
            case "login_fallido":
                return {
                    "id_evento": id,
                    "tipo_evento": "login_fallido",
                    "fecha_hora": f"{fake.date()} {fake.time()}",
                    "mensaje": "Intento fallido de inicio de sesión",
                    "nombre_usuario": fake.user_name()
                }


def crear_eventos():
    for i in range(100):
        evento_seleccionado = choice(posibles_eventos)
        print(f"Se va a registrar un evento {evento_seleccionado}")
        evento = llenar_formulario(evento_seleccionado, i)
        eventos.append(evento)
  


def main():
    global coleccion_evento

    client = MongoClient("mongodb://localhost:27017/")
    db_eventos = client["eventos_emprendimiento"]
    coleccion_evento = db_eventos["eventos"]
    crear_eventos()
    coleccion_evento.insert_many(eventos)


if __name__ == "__main__":
    main()