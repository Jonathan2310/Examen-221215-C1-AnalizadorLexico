from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
import re

app = Flask(__name__)
CORS(app)
app.secret_key = 'clavee22'
logging.basicConfig(level=logging.DEBUG)

def analizar_producto(producto, precio_str):
    # Convertir precio a flotante
    if '.' in precio_str:
        precio = float(precio_str)
    else:
        precio = float(precio_str)
    
    return producto, precio

def calcular_precio_final(precio):
    iva = precio * 0.16
    precio_final = precio + iva
    return iva, precio_final

@app.route('/analizar', methods=['POST'])
def analizar():
    data = request.json
    producto = data.get('producto')
    precio_str = data.get('precio')
    
    if not producto or not precio_str:
        return jsonify({"error": "Producto o precio faltante"}), 400
    
    nombre, precio = analizar_producto(producto, precio_str)
    iva, precio_final = calcular_precio_final(precio)
    
    productos_procesados = [{
        "nombre": nombre,
        "precio": precio,
        "iva": iva,
        "precioFinal": precio_final
    }]
    
    return jsonify({"productosProcesados": productos_procesados})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
