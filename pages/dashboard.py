import streamlit as st
import pandas as pd
import plotly.express as px
import requests
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv('key.env')
EIA_API_KEY = os.getenv('EIA_API_KEY')

st.set_page_config(
    page_title="Dashboard - Mercado Eléctrico",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dashboard del Mercado Eléctrico")

# Sección de Precios del Gas Natural
st.header("Precios del Gas Natural")

# Filtros de fecha
col1, col2 = st.columns(2)
with col1:
    fecha_inicio = st.date_input(
        "Fecha Inicio",
        datetime.now() - timedelta(days=365)
    )
with col2:
    fecha_fin = st.date_input(
        "Fecha Fin",
        datetime.now()
    )

# Función para obtener datos de la API de EIA
def obtener_datos_gas_natural():
    url = f"https://api.eia.gov/v2/natural-gas/pri/fut/data/?frequency=weekly&data[0]=value&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000&api_key={EIA_API_KEY}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # Convertir datos a DataFrame
        df = pd.DataFrame(data['response']['data'])
        df['period'] = pd.to_datetime(df['period'])
        df = df.sort_values('period')
        
        # Filtrar por rango de fechas
        df = df[(df['period'].dt.date >= fecha_inicio) & 
                (df['period'].dt.date <= fecha_fin)]
        
        return df
    except Exception as e:
        st.error(f"Error al obtener datos: {str(e)}")
        return None

# Obtener y mostrar datos
df_gas = obtener_datos_gas_natural()

if df_gas is not None:
    # Crear gráfico
    fig = px.line(
        df_gas,
        x='period',
        y='value',
        title='Precios Spot del Gas Natural',
        labels={
            'period': 'Fecha',
            'value': 'Precio (USD/MMBtu)'
        }
    )
    
    # Personalizar gráfico
    fig.update_layout(
        xaxis_title="Fecha",
        yaxis_title="Precio (USD/MMBtu)",
        hovermode='x unified',
        showlegend=True
    )
    
    # Mostrar gráfico
    st.plotly_chart(fig, use_container_width=True)
    
    # Mostrar datos en tabla
    st.subheader("Datos Detallados")
    st.dataframe(df_gas[['period', 'value']].rename(columns={
        'period': 'Fecha',
        'value': 'Precio (USD/MMBtu)'
    }))
else:
    st.warning("No se pudieron cargar los datos. Por favor, verifica la conexión y los filtros seleccionados.") 