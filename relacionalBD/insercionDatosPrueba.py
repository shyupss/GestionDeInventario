import re
import json
import random
import psycopg2
import unicodedata
from faker import Faker

MAX: int = int(10e3)

# Llamamos los json con datos para la selección
with open("./categorias.json", "r", encoding="utf-8") as f:
    Categorias = json.load(f)
    
with open("./proveedores.json", "r", encoding="utf-8") as f:
    Proveedores = json.load(f)

with open("./productos.json", "r", encoding="utf-8") as f:
    Productos = json.load(f)

with open("./unidadesMedida.json", "r", encoding="utf-8") as f:
    UnidadesMedida = json.load(f)
    
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
cur = conn.cursor()

# Función para pasar a campbell keys
def campbellKeyOfString(text: str) -> str:
	text = unicodedata.normalize('NFD', text)
	text = text.encode('ascii', 'ignore').decode('utf-8')
	text = text.lower()
	text = re.sub(r'[^a-z0-9]', '', text)
	return text

# Inserción de datos sobre la tabla "categorias"
for id, categoria in enumerate(Categorias):
	cur.execute("INSERT INTO categorias (id_categoria, nombre) VALUES (%s, %s)",
               (id+1, categoria)
               )
conn.commit()

# Inserción de datos sobre la tabla de "proveedores"
for id, proveedor in enumerate(Proveedores):
	cur.execute("INSERT INTO proveedores (id_proveedor, nombre, correo, telefono) VALUES (%s, %s, %s, %s)",
               (id+1, proveedor, fake.email(domain=f"{campbellKeyOfString(proveedor)}.com"), fake.phone_number())
               )
conn.commit()

# Inserción de datos sobre la tabla "trabajador"
for id in range (30):
	cur.execute("INSERT INTO trabajador (id_trabajador, nombre, telefono, correo, rol) VALUES (%s, %s, %s, %s, %s)",
               (id+1, fake.name(), fake.phone_number(), fake.email(), random.choice(["vendedor", "conserje", "marketing", "ingeniero", "administrador"]))
               )
conn.commit()

# Inserción de datos sobre la tabla "compras"
for id in range (MAX):
	precio_total = round(random.uniform(1e4, 1e6), 2)
	cur.execute("INSERT INTO compras (id_compra, fecha, precio_total, id_proveedor) VALUES (%s, %s, %s, %s)",
               (id+1, fake.date(), precio_total, random.randint(1, len(Proveedores)))
               )
conn.commit()

# Inserción de datos sobre la tabla "productos"
for id, producto in enumerate(Productos):
	precio_unitario = round(random.uniform(1e2, 1e4), 2)
	stock = random.randint(1000, 10000)
	min_stock = random.randint(10, 100)
	cur.execute("INSERT INTO productos (id_producto, nombre, descripcion, precio_unitario, unidad_medida, stock, min_stock, id_categoria) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
               (id+1, producto, "desc general", precio_unitario, random.choice(UnidadesMedida), stock, min_stock, random.randint(1, len(Categorias)))
               )
conn.commit()

# Inserción de datos sobre la tabla "ventas"
for id in range (MAX):
	precio_total = round(random.uniform(1e4, 1e6), 2)
	cur.execute("INSERT INTO ventas (id_venta, fecha, precio_total, id_proveedor) VALUES (%s, %s, %s, %s)",
               (id+1, fake.date(), precio_total, random.randint(1, len(Proveedores)))
               )
conn.commit()

cur.close()
conn.close()