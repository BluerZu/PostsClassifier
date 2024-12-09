import streamlit as st
import requests

# URL de tu API Flask
API_URL = "http://127.0.0.1:5000/classify"

# Título de la interfaz
st.title("Clasificador de Sentimiento de Publicaciones")

# Campo para ingresar el texto
text_input = st.text_area("Ingrese el texto a clasificar", "")

# Campo para ingresar los tags (separados por comas)
tags_input = st.text_input("Ingrese los tags (separados por coma)", "Positivo, Negativo, Neutro")

# Convertir los tags en una lista
tags = [tag.strip() for tag in tags_input.split(",")]

# Botón para realizar la clasificación
if st.button("Clasificar Sentimiento"):
    if text_input and tags:
        # Enviar los datos al API
        payload = {"text": text_input, "tags": tags}
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            result = response.json()
            st.success(f"Sentimiento clasificado: {result['sentiment']}")
        else:
            st.error("Error al clasificar el sentimiento")
    else:
        st.warning("Por favor, ingrese un texto y los tags.")

