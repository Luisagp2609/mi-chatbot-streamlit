import streamlit as st

st.set_page_config(
    page_title="Dashboard - Mi Chatbot",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dashboard")

st.markdown("""
### Próximamente
En esta sección podrás ver:
- Estadísticas de uso del chatbot
- Gráficos de interacción
- Métricas de rendimiento
- Análisis de conversaciones
""")

# Placeholder para futuras gráficas
col1, col2 = st.columns(2)

with col1:
    st.info("Aquí irá el primer gráfico")
    
with col2:
    st.info("Aquí irá el segundo gráfico") 