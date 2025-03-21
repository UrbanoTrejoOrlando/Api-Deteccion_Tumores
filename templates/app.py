import os
from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Ruta donde están almacenadas las imágenes
static_folder = "static/images"

# Lista de nombres de imágenes secuenciales (1.png, 2.png, ..., n.png)
def get_images():
    return [f"{i}.png" for i in range(1, 7)]  # Asumiendo que tienes imágenes desde 1.png hasta 6.png

# Variable para llevar el control del índice de las imágenes
current_index = 0

@app.route("/")
def index():
    global current_index
    # Obtener las imágenes secuenciales
    image_files = get_images()
    
    # Mostrar las primeras 3 imágenes según el índice
    selected_images = image_files[current_index:current_index+3]

    # Crear las rutas completas a las imágenes
    image_paths = [f"/static/images/{image}" for image in selected_images]

    return render_template("index.html", images=image_paths)

@app.route("/next_images")
def next_images():
    global current_index
    # Obtener las imágenes secuenciales
    image_files = get_images()
    
    # Avanzar el índice de las imágenes, reiniciando cuando llegue al final
    current_index = (current_index + 3) % len(image_files)
    
    # Seleccionar las próximas 3 imágenes
    selected_images = image_files[current_index:current_index+3]

    # Crear las rutas completas a las imágenes
    image_paths = [f"/static/images/{image}" for image in selected_images]

    return jsonify({"images": image_paths})

if __name__ == "__main__":
    app.run(debug=True)
