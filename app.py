"""
Aplicación Principal del Chatbot
-------------------------------
Página de bienvenida y navegación principal.
"""

import streamlit as st
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv('key.env')

# Configuración de la página
st.set_page_config(
    page_title="Mi Chatbot",
    page_icon="🤖",
    layout="wide"
)

# Obtener API key de las variables de entorno
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Sidebar
with st.sidebar:
    st.title("🤖 Mi Chatbot")
    st.markdown("---")
    st.markdown("### Acerca de")
    st.markdown("""
    Este chatbot utiliza OpenAI GPT-3.5 para proporcionar respuestas inteligentes y contextuales.
    """)
    st.markdown("---")
    st.markdown("### Enlaces útiles")
    st.markdown("- [Documentación de OpenAI](https://platform.openai.com/docs)")
    st.markdown("- [Documentación de Streamlit](https://docs.streamlit.io)")

# Contenido principal
st.title("Bienvenido a Mi Chatbot")
st.markdown("""
### ¿Qué puedes hacer?
- Hacer preguntas generales
- Obtener información sobre diversos temas
- Mantener conversaciones contextuales
- Ver estadísticas de uso en el dashboard
""")

# Mostrar mensaje si no hay API key
if not OPENAI_API_KEY:
    st.error("⚠️ No se encontró la API key de OpenAI. Por favor, asegúrate de que el archivo 'key.env' existe y contiene tu API key.")
    st.stop()

# Sección de navegación
st.markdown("---")
st.markdown("### Navegación")
col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 💬 Chatbot")
    st.markdown("Interactúa con el chatbot y haz tus preguntas.")
    if st.button("Ir al Chatbot", key="chatbot_btn"):
        st.switch_page("pages/chatbot.py")

with col2:
    st.markdown("#### 📊 Dashboard")
    st.markdown("Visualiza estadísticas y métricas de uso.")
    if st.button("Ir al Dashboard", key="dashboard_btn"):
        st.switch_page("pages/dashboard.py") 