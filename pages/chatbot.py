import streamlit as st
import os
from dotenv import load_dotenv
import openai
from datetime import datetime, timedelta
import pandas as pd
import plotly.express as px
import requests

# Configuración de la página
st.set_page_config(
    page_title="Chatbot - Mercado Eléctrico",
    page_icon="🤖",
    layout="wide"
)

# Cargar variables de entorno
env_path = os.path.join(os.path.dirname(__file__), '..', 'key.env')
load_dotenv(env_path)

# Obtener API keys
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
EIA_API_KEY = os.getenv('EIA_API_KEY')

# Verificar API keys
if not EIA_API_KEY:
    st.error("⚠️ No se encontró la API key de EIA. Por favor, asegúrate de que el archivo 'key.env' existe y contiene tu API key de EIA.")
    st.stop()

if not OPENAI_API_KEY:
    st.error("⚠️ No se encontró la API key de OpenAI. Por favor, asegúrate de que el archivo 'key.env' existe y contiene tu API key de OpenAI.")
    st.stop()

# Inicializar el cliente de OpenAI
client = openai.OpenAI(api_key=OPENAI_API_KEY)

# Título y descripción
st.title("🤖 Chatbot Asistente")
st.markdown("""
¡Hola! Soy tu asistente virtual especializado en el mercado eléctrico. 
Puedo ayudarte a entender mejor el sector energético y responder tus preguntas sobre:
- Precios y tarifas del mercado eléctrico
- Tendencias y análisis del sector
- Conceptos técnicos y regulaciones
- Datos históricos y proyecciones
""")

# Inicializar el historial del chat en session_state si no existe
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": """¡Hola! Soy tu asistente virtual especializado en el mercado eléctrico. 
            ¿En qué puedo ayudarte hoy? Aquí hay algunas preguntas que puedo responder:

            1. ¿Cuál es el precio actual del gas natural?
            2. ¿Cómo funciona el mercado eléctrico mayorista?
            3. ¿Qué factores influyen en los precios de la electricidad?
            4. ¿Cuáles son las últimas tendencias en el sector energético?
            5. ¿Cómo se calculan las tarifas eléctricas?

            ¡Adelante, hazme cualquier pregunta!"""
        }
    ]

# Mostrar mensajes anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input del usuario
if prompt := st.chat_input("¿Qué te gustaría saber sobre el mercado eléctrico?"):
    # Agregar mensaje del usuario al historial
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Mostrar mensaje del usuario
    with st.chat_message("user"):
        st.markdown(prompt)

    # Obtener respuesta del asistente
    with st.chat_message("assistant"):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": """Eres un asistente especializado en el mercado eléctrico. 
                    Tu objetivo es proporcionar información precisa y útil sobre el sector energético, 
                    incluyendo precios, tendencias, regulaciones y conceptos técnicos. 
                    Mantén un tono profesional pero amigable, y siempre intenta ser lo más específico posible 
                    en tus respuestas."""},
                    *[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
                ]
            )
            response_content = response.choices[0].message.content
            st.markdown(response_content)
            
            # Agregar respuesta del asistente al historial
            st.session_state.messages.append({"role": "assistant", "content": response_content})
        except Exception as e:
            st.error(f"Error al obtener respuesta: {str(e)}")

# Botón para volver a la página principal
if st.button("Volver a la página principal"):
    st.switch_page("App.py") 