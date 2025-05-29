"""
Utilidades para el Chatbot
-------------------------
Este módulo contiene funciones auxiliares utilizadas por el chatbot.
"""

import re
from typing import List, Dict, Any

def format_response(response: str) -> str:
    """
    Formatea la respuesta del modelo para mejorar su presentación.
    
    Args:
        response (str): Respuesta generada por el modelo
        
    Returns:
        str: Respuesta formateada
    """
    # Eliminar espacios múltiples
    response = re.sub(r'\s+', ' ', response)
    
    # Eliminar espacios al inicio y final
    response = response.strip()
    
    # Capitalizar la primera letra
    if response:
        response = response[0].upper() + response[1:]
    
    return response

def split_into_sentences(text: str) -> List[str]:
    """
    Divide un texto en oraciones.
    
    Args:
        text (str): Texto a dividir
        
    Returns:
        List[str]: Lista de oraciones
    """
    # Patrón para dividir en oraciones (considera puntos, signos de interrogación y exclamación)
    pattern = r'[.!?]+'
    sentences = re.split(pattern, text)
    
    # Limpiar oraciones vacías y espacios
    sentences = [s.strip() for s in sentences if s.strip()]
    
    return sentences

def extract_entities(text: str) -> List[str]:
    """
    Extrae entidades mencionadas en el texto.
    
    Args:
        text (str): Texto del que extraer entidades
        
    Returns:
        List[str]: Lista de entidades encontradas
    """
    # Patrón simple para nombres propios (palabras que empiezan con mayúscula)
    pattern = r'\b[A-Z][a-z]+\b'
    entities = re.findall(pattern, text)
    
    return list(set(entities))  # Eliminar duplicados 