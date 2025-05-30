"""
Aplicación Principal del Chatbot
-------------------------------
Página de bienvenida y navegación principal.
"""

import streamlit as st
import os
from dotenv import load_dotenv
import openai
from datetime import datetime, timedelta
import pandas as pd
import plotly.express as px
import requests

# Configuración de la página (debe ser la primera llamada a Streamlit)
st.set_page_config(
    page_title="Mercado Eléctrico - Chatbot & Dashboard",
    page_icon="⚡",
    layout="wide"
)

# Cargar variables de entorno
env_path = os.path.join(os.path.dirname(__file__), 'key.env')
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

# Función para obtener datos de la API de EIA
def obtener_datos_gas_natural():
    url = f"https://api.eia.gov/v2/natural-gas/pri/fut/data/?frequency=weekly&data[0]=value&facets[series][]=NG.RNGWHHD.W&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000&api_key={EIA_API_KEY}"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 403:
            st.error("Error de autenticación. La API key no es válida o ha expirado.")
            return None
            
        response.raise_for_status()
        data = response.json()
        
        # Verificar si hay datos en la respuesta
        if 'response' not in data or 'data' not in data['response']:
            st.error("No se encontraron datos en la respuesta de la API")
            return None
        
        # Convertir datos a DataFrame
        df = pd.DataFrame(data['response']['data'])
        
        # Verificar si hay datos en el DataFrame
        if df.empty:
            st.error("No hay datos disponibles para el período seleccionado")
            return None
            
        # Convertir la columna de fecha
        df['period'] = pd.to_datetime(df['period'])
        df = df.sort_values('period')
        
        # Filtrar por último año
        fecha_inicio = datetime.now() - timedelta(days=365)
        df = df[df['period'].dt.date >= fecha_inicio.date()]
        
        return df
    except requests.exceptions.RequestException as e:
        st.error(f"Error en la petición HTTP: {str(e)}")
        return None
    except Exception as e:
        st.error(f"Error al procesar los datos: {str(e)}")
        return None

# Contenido principal
st.title("⚡ Mercado Eléctrico")

# Descripción del proyecto
st.markdown("""
### Bienvenido a nuestra plataforma de análisis del mercado eléctrico

Esta aplicación te permite:
- 🤖 Interactuar con un asistente inteligente especializado en el mercado eléctrico
- 📊 Visualizar datos en tiempo real sobre precios y tendencias
- 📈 Analizar información relevante del sector energético

Nuestro objetivo es proporcionarte herramientas y conocimientos para entender mejor el mercado eléctrico y tomar decisiones informadas.
""")

# Sección de navegación
st.markdown("---")
st.markdown("### ¿Qué te gustaría explorar?")
col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 💬 Chatbot Asistente")
    st.markdown("""
    Nuestro asistente virtual puede ayudarte con:
    - Información sobre el mercado eléctrico
    - Análisis de tendencias
    - Explicaciones técnicas
    - Consultas sobre precios y tarifas
    """)
    if st.button("Ir al Chatbot", key="chatbot_btn", use_container_width=True):
        st.switch_page("pages/Chatbot.py")

with col2:
    st.markdown("#### 📊 Dashboard")
    st.markdown("""
    Visualiza y analiza:
    - Precios del gas natural
    - Tendencias del mercado
    - Datos históricos
    - Gráficos interactivos
    """)
    if st.button("Ir al Dashboard", key="dashboard_btn", use_container_width=True):
        st.switch_page("pages/Dashboard.py")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>Desarrollado con ❤️ para el sector energético</p>
</div>
""", unsafe_allow_html=True) 