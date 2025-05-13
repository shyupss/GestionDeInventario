from fastapi import FastAPI, HTTPException
import psycopg2

app = FastAPI()

# Conexión a la BD relacional
conn = psycopg2.connect(
	host="localhost",
	database="inventario_emprendimiento",
	user="usuario_emprendimiento",
	password="1234"
)
cur = conn.cursor()

# Ruta Raíz
@app.get("/")
def home():
    return {"mensaje":" API Web - Gestion De Inventario"}

# Get de prueba
@app.get("Oye/{nombre}")
def saludar(nombre: str):
    return {"mensaje": f"wena po {nombre}"}