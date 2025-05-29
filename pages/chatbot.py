import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv('key.env')

# Obtener API key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Configuración de la página
st.set_page_config(
    page_title="Chatbot - Mi Asistente",
    page_icon="💬",
    layout="wide"
)

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
st.title("💬 Chatbot")
st.caption("🚀 Un chatbot potenciado por OpenAI GPT-3.5")

# Inicializar el historial de mensajes
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "¡Hola! ¿En qué puedo ayudarte hoy?"}]

# Mostrar el historial de mensajes
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Input del usuario
if prompt := st.chat_input():
    if not OPENAI_API_KEY:
        st.info("⚠️ No se encontró la API key de OpenAI. Por favor, asegúrate de que el archivo 'key.env' existe y contiene tu API key.")
        st.stop()

    # Agregar mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    try:
        # Obtener respuesta del modelo usando la nueva API
        client = OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
        )
        msg = response.choices[0].message.content

        # Agregar respuesta del asistente
        st.session_state.messages.append({"role": "assistant", "content": msg})
        st.chat_message("assistant").write(msg)
    except Exception as e:
        st.error(f"Error al comunicarse con OpenAI: {str(e)}")
        st.stop()

# Botón para limpiar el historial
if st.button("Limpiar Chat"):
    st.session_state.messages = [{"role": "assistant", "content": "¡Hola! ¿En qué puedo ayudarte hoy?"}]
    st.experimental_rerun() 