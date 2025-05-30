# ⚡ Mercado Eléctrico - Chatbot & Dashboard

## 📝 Descripción
Aplicación web interactiva que combina un chatbot especializado en el mercado eléctrico con un dashboard para visualización de datos en tiempo real. La aplicación permite a los usuarios obtener información precisa sobre el mercado eléctrico y visualizar datos relevantes del sector.

## ✨ Características Principales

### 🤖 Chatbot Asistente
- Asistente virtual especializado en el mercado eléctrico
- Respuestas precisas y contextuales
- Sugerencias de preguntas relevantes
- Interfaz de chat intuitiva

### 📊 Dashboard
- Visualización de precios del gas natural
- Gráficos interactivos
- Filtros de fecha
- Tabla de datos detallada

## 🚀 Instalación

1. Clonar el repositorio:
```bash
git clone [URL_DEL_REPOSITORIO]
cd mi_chatbot_streamlit
```

2. Instalar dependencias:
```bash
pip install -r requirements_minimal.txt
```

3. Configurar variables de entorno:
   - Crear archivo `key.env` en la raíz del proyecto
   - Agregar las siguientes variables:
     ```
     OPENAI_API_KEY=tu_api_key_de_openai
     EIA_API_KEY=tu_api_key_de_eia
     ```

4. Ejecutar la aplicación:
```bash
streamlit run App.py
```

## 📦 Dependencias Principales
- streamlit==1.32.0
- pandas==2.2.1
- plotly==5.19.0
- requests==2.31.0
- python-dotenv==1.0.1
- openai==1.12.0

## 🏗️ Estructura del Proyecto
```
mi_chatbot_streamlit/
├── App.py                 # Aplicación principal
├── pages/
│   ├── Chatbot.py        # Módulo del chatbot
│   └── Dashboard.py      # Módulo del dashboard
├── key.env               # Variables de entorno
├── requirements_minimal.txt  # Dependencias
└── README.md             # Documentación
```

## 🔑 API Keys Requeridas
- OpenAI API Key: Para el funcionamiento del chatbot
- EIA API Key: Para obtener datos del mercado eléctrico

## 🤝 Contribución
Las contribuciones son bienvenidas. Por favor, lee las guías de contribución antes de enviar un pull request.

## 📄 Licencia
Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 📞 Contacto
Para preguntas o sugerencias, por favor abre un issue en el repositorio. 