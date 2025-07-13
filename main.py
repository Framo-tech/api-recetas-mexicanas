from fastapi import FastAPI
import json

app = FastAPI()

# Cargar las recetas al iniciar la API
with open("recetas_mexicanas.json", encoding="utf-8") as f:
    recetas = json.load(f)

@app.get("/")
def inicio():
    return {"mensaje": "Bienvenido a la API de Recetas Mexicanas 🇲🇽"}

@app.get("/recetas")
def obtener_todas():
    return recetas

@app.get("/receta/{id_receta}")
def obtener_por_id(id_receta: str):
    for receta in recetas:
        if receta["id"] == id_receta:
            return receta
    return {"error": "Receta no encontrada"}
