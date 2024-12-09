from flask import Flask, request, jsonify
from main import classify_sentiment  # Importamos la función desde main.py

# Crear la aplicación Flask
app = Flask(__name__)

# Endpoint para clasificar el sentimiento
@app.route('/classify', methods=['POST'])
def classify():
    # Obtener los datos del JSON enviado en la petición
    data = request.get_json()

    # Asegurarse de que los parámetros 'text' y 'tags' están en el cuerpo de la petición
    if not data or 'text' not in data or 'tags' not in data:
        return jsonify({"error": "Faltan parámetros en la solicitud"}), 400

    text = data['text']
    tags = data['tags']

    # Llamar a la función de clasificación de sentimientos
    classification = classify_sentiment(text, tags)

    # Devolver el resultado como respuesta en formato JSON
    return jsonify({"sentiment": classification})

# Ejecutar la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True)
