# Mi Chatbot con OpenAI

Este es un chatbot interactivo construido con Streamlit y OpenAI GPT-3.5.

## Características

- Interfaz de chat intuitiva
- Respuestas coherentes y contextuales
- Historial de conversación
- Diseño responsive

## Configuración en Hugging Face Spaces

1. Crea un nuevo Space en Hugging Face
2. Selecciona "Streamlit" como SDK
3. Conecta tu repositorio
4. Agrega las siguientes variables de entorno en la configuración del Space:
   - `OPENAI_API_KEY`: Tu API key de OpenAI

## Estructura del Proyecto

```
.
├── App.py              # Aplicación principal
├── requirements.txt    # Dependencias
├── key.env            # Variables de entorno (local)
└── src/
    └── chatbot/       # Módulo del chatbot
```

## Desarrollo Local

1. Clona el repositorio
2. Crea un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   .\venv\Scripts\activate   # Windows
   ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Crea un archivo `key.env` con tu API key:
   ```
   OPENAI_API_KEY=tu_api_key_aqui
   ```
5. Ejecuta la aplicación:
   ```bash
   streamlit run App.py
   ```

## Licencia

MIT 