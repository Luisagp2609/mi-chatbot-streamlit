#lanzar con streamlit run c_front_end.py en el terminal

import b_backend3
import streamlit as st
from streamlit_chat import message

st.title("ChatBot para el Mercado Eléctrico")
st.write("Puedes hacerme a mi todas las preguntas!!")

if 'preguntas' not in st.session_state:
    st.session_state.preguntas = []
if 'respuestas' not in st.session_state:
    st.session_state.respuestas = []

def click():
    if st.session_state.user != '':
        pregunta = st.session_state.user
        respuesta = b_backend3.consulta(pregunta)

        st.session_state.preguntas.append(pregunta)
        st.session_state.respuestas.append(respuesta)

        # Limpiar el input de usuario después de enviar la pregunta
        st.session_state.user = ''


with st.form('my-form'):
   query = st.text_input('¿En qué te puedo ayudar?:', key='user', help='Pulsa Enviar para hacer la pregunta')
   submit_button = st.form_submit_button('Enviar',on_click=click)

if st.session_state.preguntas:
    for i in range(len(st.session_state.preguntas)):
        message(st.session_state.preguntas[i], is_user=True, key=f"user_{i}")
        message(st.session_state.respuestas[i], key=f"bot_{i}")


    # Opción para continuar la conversación
    continuar_conversacion = st.checkbox('Quieres hacer otra pregunta?')
    if not continuar_conversacion:
        st.session_state.preguntas = []
        st.session_state.respuestas = []









