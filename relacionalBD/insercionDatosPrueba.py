import os
import psycopg2
import json as js_
import random as rndm
from faker import Faker

MAX: int= int(10e3)

# Llamamos el json con datos para la selección

with open("../categories.json", "r", encoding="utf-8") as f:
    Categorias = js_.load(f)
    
print(Categorias)

# Creamos el objeto fake
fake = Faker()

# Conexión a la BD relacional
conn = psycopg2.connect(
	host="localhost",
	database="inventario_emprendimiento",
	user="usuario_emprendimiento",
	password="1234"
)
#cur = conn.cursor()

# acá inserto sobre categorías (:v, pero tengo que arreglar lo de arriba)
# Inserción de datos sobre la tabla "categorias"
#for i in range(MAX):
#    cur.execute("INSERT INTO categorias (id_categoria, nombre) VALUES (%s, %s)",
#                (i+1, "wrof")
#                )
#    conn.commit()
#
#