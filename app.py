import streamlit as st
import openai
from prompts import get_prompt_context
from utils import simulate_event_response

st.set_page_config(page_title="EntradasYA - Soporte Virtual", page_icon="🎟️")
st.title("🎟️ EntradasYA - Asistente Virtual")

st.markdown("""
Este bot es un demo de un asistente virtual inteligente para boleterías digitales.
Pregunta lo que necesites sobre eventos, pagos o soporte. 😊
""")

# Sidebar config
with st.sidebar:
    st.header("🔑 Configuración")
    api_key = st.text_input("OpenAI API Key", type="password")
    st.markdown("""Este bot utiliza GPT para responder como si fuera el dueño de una boletería digital.""")

if not api_key:
    st.warning("Por favor, ingresa tu OpenAI API Key en la barra lateral.")
    st.stop()

openai.api_key = api_key

# Chat input/output
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Escribe tu mensaje:", placeholder="¿Qué eventos hay esta semana?", key="user_input")

if user_input:
    context = get_prompt_context(st.session_state.chat_history, user_input)

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=context,
            temperature=0.7
        )
        reply = response.choices[0].message.content.strip()
        reply = simulate_event_response(user_input, reply)

        st.session_state.chat_history.append(("Tú", user_input))
        st.session_state.chat_history.append(("EntradasYA", reply))

    except Exception as e:
        st.error(f"Error al conectar con OpenAI: {e}")

# Mostrar historial
for sender, message in st.session_state.chat_history:
    with st.chat_message(sender):
        st.markdown(message)