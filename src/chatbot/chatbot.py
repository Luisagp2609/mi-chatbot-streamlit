"""
Implementación principal del Chatbot
----------------------------------
Este módulo contiene la clase Chatbot que maneja la lógica principal
de interacción con el modelo de OpenAI.
"""

from typing import List, Dict, Any
import openai
from .prompts import ChatPromptTemplate
from .utils import format_response

class Chatbot:
    def __init__(self, api_key: str = None, model: str = "gpt-3.5-turbo"):
        """
        Inicializa el chatbot con la API de OpenAI.
        
        Args:
            api_key (str): Clave de API de OpenAI
            model (str): Modelo a utilizar (por defecto: gpt-3.5-turbo)
        """
        self.model = model
        if api_key:
            openai.api_key = api_key
        self.chat_history: List[Dict[str, str]] = []
        self.prompt_template = ChatPromptTemplate()
        
    def generate_response(self, user_input: str) -> str:
        """
        Genera una respuesta basada en el input del usuario usando OpenAI.
        
        Args:
            user_input (str): Mensaje del usuario
            
        Returns:
            str: Respuesta generada por el modelo
        """
        # Preparar el mensaje del sistema
        system_message = {
            "role": "system",
            "content": self.prompt_template.get_system_prompt()
        }
        
        # Preparar el historial de chat
        messages = [system_message]
        for msg in self.chat_history:
            messages.append({
                "role": "user" if msg["role"] == "user" else "assistant",
                "content": msg["content"]
            })
        
        # Agregar el nuevo mensaje del usuario
        messages.append({
            "role": "user",
            "content": user_input
        })
        
        try:
            # Llamar a la API de OpenAI
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=150
            )
            
            # Extraer la respuesta
            assistant_response = response.choices[0].message.content
            
            # Actualizar historial
            self.chat_history.append({
                "role": "user",
                "content": user_input
            })
            self.chat_history.append({
                "role": "assistant",
                "content": assistant_response
            })
            
            return format_response(assistant_response)
            
        except Exception as e:
            return f"Lo siento, ha ocurrido un error: {str(e)}"
    
    def get_chat_history(self) -> List[Dict[str, str]]:
        """
        Retorna el historial de la conversación.
        
        Returns:
            List[Dict[str, str]]: Lista de mensajes en el formato {role: str, content: str}
        """
        return self.chat_history
    
    def clear_history(self) -> None:
        """Limpia el historial de la conversación."""
        self.chat_history = [] 