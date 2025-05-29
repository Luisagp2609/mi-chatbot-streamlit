"""
Módulo de conexión y consultas a la base de datos MySQL
-----------------------------------------------------
Este módulo maneja todas las interacciones con la base de datos del mercado eléctrico.
"""

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
import pandas as pd
from typing import Optional, Dict, Any
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DatabaseConnection:
    def __init__(self):
        """Inicializa la conexión a la base de datos."""
        self.engine = None
        self.connection = None
        self._conectar_db()

    def _conectar_db(self) -> None:
        """
        Establece la conexión con la base de datos MySQL.
        Las credenciales se cargan desde el archivo .env
        """
        try:
            # Cargar variables de entorno
            load_dotenv("key.env")
            
            # Obtener credenciales
            user = os.getenv("DB_USER", "root")
            password = os.getenv("DB_PASSWORD", "#260901Lg")
            host = os.getenv("DB_HOST", "localhost")
            port = os.getenv("DB_PORT", "3306")
            database = os.getenv("DB_NAME", "mercado_electrico")
            
            # Crear string de conexión
            connection_string = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
            
            # Crear engine
            self.engine = create_engine(connection_string)
            logger.info("Conexión a la base de datos establecida correctamente")
            
        except Exception as e:
            logger.error(f"Error al conectar con la base de datos: {str(e)}")
            raise

    def ejecutar_consulta(self, query: str) -> Optional[pd.DataFrame]:
        """
        Ejecuta una consulta SQL y retorna los resultados como DataFrame.
        
        Args:
            query (str): Consulta SQL a ejecutar
            
        Returns:
            Optional[pd.DataFrame]: DataFrame con los resultados o None si hay error
        """
        try:
            df = pd.read_sql(query, self.engine)
            return df
        except Exception as e:
            logger.error(f"Error al ejecutar la consulta: {str(e)}")
            return None

    def obtener_datos_generacion(self, 
                               fecha_inicio: Optional[str] = None,
                               fecha_fin: Optional[str] = None,
                               limite: int = 1000) -> Optional[pd.DataFrame]:
        """
        Obtiene datos de generación eléctrica con filtros opcionales.
        
        Args:
            fecha_inicio (str, optional): Fecha inicial en formato 'YYYY-MM-DD'
            fecha_fin (str, optional): Fecha final en formato 'YYYY-MM-DD'
            limite (int, optional): Límite de registros a retornar
            
        Returns:
            Optional[pd.DataFrame]: DataFrame con los datos de generación
        """
        try:
            query = """
            SELECT fecha, valor_pos_generacion
            FROM pos_generacion
            WHERE 1=1
            """
            
            # Agregar filtros si se proporcionan
            if fecha_inicio:
                query += f" AND fecha >= '{fecha_inicio}'"
            if fecha_fin:
                query += f" AND fecha <= '{fecha_fin}'"
                
            query += f" ORDER BY fecha DESC LIMIT {limite}"
            
            return self.ejecutar_consulta(query)
            
        except Exception as e:
            logger.error(f"Error al obtener datos de generación: {str(e)}")
            return None

    def cerrar_conexion(self) -> None:
        """Cierra la conexión con la base de datos."""
        if self.engine:
            self.engine.dispose()
            logger.info("Conexión a la base de datos cerrada correctamente")

# Ejemplo de uso
if __name__ == "__main__":
    # Crear instancia de la conexión
    db = DatabaseConnection()
    
    try:
        # Ejemplo de consulta
        df = db.obtener_datos_generacion(limite=5)
        if df is not None:
            print("Datos obtenidos:")
            print(df)
    finally:
        # Cerrar conexión
        db.cerrar_conexion() 