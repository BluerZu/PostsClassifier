from dotenv import load_dotenv
import os
from groq import Groq
import json

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Extraer la clave API desde el archivo .env
api_key = os.getenv("API_KEY")

# Inicialización del cliente de Groq
client = Groq(api_key=api_key)


# Función para clasificar el sentimiento de una publicación
def classify_sentiment(text: str, tags: list):
    # Crear el prompt dinámico según los tags proporcionados
    tags_str = ", ".join(tags)
    prompt = f"""
    You are a content classifier. Your task is to correctly detect the general sentiment of the following text.
    You can use the following tags to classify the sentiment:
    {tags_str}

    The text to classify is: "{text}"

    Please respond with a JSON object containing the corresponding tag as the value of the "response" key.
    Example format:
    {{
        "response": "Positive"
    }}
    """

    # Enviar el texto al modelo para obtener la clasificación
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3-8b-8192",
    )

    # Obtener la respuesta del modelo y convertirla a JSON
    response = chat_completion.choices[0].message.content
    try:
        # Intentar cargar la respuesta como un JSON
        sentiment = json.loads(response)
        return sentiment["response"]
    except json.JSONDecodeError:
        return "Error: La respuesta no tiene el formato JSON."

# Ejemplo de uso con tags dinámicos

#Tags 1
tags = ["Positivo", "Negativo", "Neutro"]

#Tags 2
# tags = ["Política", "Deportes", "Ciencia", "Otro"]

# Texto Positivo-Deportivo:
text_post = "La TRI jugará un partido importante este domingo, todos vamos a apoyarlos."

#Texto Negativo-Político:
# text_post = "Espero que pronto se largen los del partido derechista centro izquierdistas, no apoyan en nada al país."

#Texto Neutro-Científico:
# text_post = "Hoy se discute un importante partido de investigación sobre las diferencias genéticas entre especies."

#Texto de Positivo-Otro:
# text_post = "Me gusta desayunar pizza."

classification = classify_sentiment(text_post, tags)
print(f"Publicación: {text_post}")
print(f"El sentimiento de la publicación es: {classification}")
