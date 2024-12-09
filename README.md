
# Proyecto de Clasificación de Sentimientos

Este proyecto permite clasificar según tags dinámicos una publicaciones mediante un modelo de IA utilizando Groq.

## Requisitos
- Python 9.x o superior
- Instalar dependencias utilizando `pip`

## Instalación

1. Clona el repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_REPOSITORIO>
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Crea un archivo `.env` en la raíz del proyecto con la siguiente variable:
   ```bash
   API_KEY=tu_clave_de_API_aqui
   ```

## Ejecución

1. Primero, ejecuta la API (`app.py`):
   ```bash
   python app.py
   ```

2. Luego, ejecuta la interfaz de usuario con Streamlit (`front.py`):
   ```bash
   streamlit run front.py
   ```
