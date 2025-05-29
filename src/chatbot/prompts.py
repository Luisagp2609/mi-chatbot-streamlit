"""
Plantillas de Prompts para el Chatbot
-----------------------------------
Este módulo contiene las plantillas de prompts utilizadas para
guiar las respuestas del modelo.
"""

from typing import Dict, Any

class ChatPromptTemplate:
    """Plantilla base para los prompts del chatbot."""
    
    DEFAULT_SYSTEM_PROMPT = """Eres un asistente virtual amigable y servicial.
    Tu objetivo es ayudar a los usuarios de manera clara y concisa.
    Mantén un tono profesional pero cercano."""
    
    def __init__(self, system_prompt: str = DEFAULT_SYSTEM_PROMPT):
        """
        Inicializa la plantilla de prompt.
        
        Args:
            system_prompt (str): Prompt del sistema que define el comportamiento del chatbot
        """
        self.system_prompt = system_prompt
    
    def format_prompt(self, user_input: str, chat_history: list = None) -> str:
        """
        Formatea el prompt completo con el historial de chat y el input del usuario.
        
        Args:
            user_input (str): Input del usuario
            chat_history (list, optional): Historial de la conversación
            
        Returns:
            str: Prompt formateado
        """
        prompt = f"{self.system_prompt}\n\n"
        
        if chat_history:
            for message in chat_history:
                prompt += f"Usuario: {message['user']}\n"
                prompt += f"Asistente: {message['assistant']}\n"
        
        prompt += f"Usuario: {user_input}\n"
        prompt += "Asistente:"
        
        return prompt
    
    def get_system_prompt(self) -> str:
        """Retorna el prompt del sistema."""
        return self.system_prompt 