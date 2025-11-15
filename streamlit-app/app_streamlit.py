import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("Demo: Chatbot com Streamlit")

pergunta = st.text_input("Digite sua pergunta")
if st.button("Enviar"):
    if pergunta.strip() == "":
        st.warning("Escreva algo primeiro.")
    else:
        with st.spinner("Gerando resposta..."):
            resp = client.responses.create(
                model="gpt-5.1-mini",
                input=pergunta
            )
            st.write(getattr(resp, "output_text", str(resp)))
