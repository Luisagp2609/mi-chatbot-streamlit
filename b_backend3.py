import re
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
from langchain_experimental.sql import SQLDatabaseChain
from dotenv import load_dotenv
from sqlalchemy import create_engine
import os

# 📁 Cargar API Key desde archivo .env
load_dotenv("key.env")
api_key = os.getenv("OPENAI_API_KEY")

# 🔌 Conexión a MySQL (ajusta tus credenciales según sea necesario)
engine = create_engine("mysql+pymysql://root:#260901Lg@localhost:3306/mercado_electrico")
db = SQLDatabase(engine)

# 🤖 Configurar el modelo OpenAI
llm = ChatOpenAI(
    temperature=0.7,
    model_name='gpt-4o-mini'
)

# 🔗 Crear la cadena de conexión con ejecución automática
cadena = SQLDatabaseChain.from_llm(
    llm=llm,
    db=db,
    verbose=False,
    return_sql=False,               # ✅ Devuelve la respuesta en lenguaje natural
    return_intermediate_steps=False
)

# 🧽 Limpiar SQL generado por el modelo
def limpiar_sql(sql: str) -> str:
    sql = re.sub(r"```sql\s*|```", "", sql.strip(), flags=re.IGNORECASE)
    return sql.strip()

# 🧠 Prompt base en español
formato = """
Dada una pregunta del usuario:
1. Crea una consulta en MySQL válida para la base de datos.
2. Ejecuta la consulta usando la tabla `pos_generacion`.
3. Devuelve el dato de forma clara y en español.
4. No uses formato Markdown ni etiquetas como ```sql.
5. Si te piden la generacion, usa el campo `valor_pos_generacion` y le agregas la unidad (MWh) al resultado.

Pregunta:
{question}
"""

# 🚀 Función para consultar
def consulta(input_usuario):
    prompt = formato.format(question=input_usuario)
    resultado = cadena.run(prompt)
    return resultado

