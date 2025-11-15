from openai import OpenAI
import gradio as gr
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

def responder(pergunta):
    if not pergunta:
        return "Por favor, escreva sua pergunta."
    resp = client.responses.create(
        model="gpt-5.1-mini",
        input=pergunta
    )
    # dependendo da versão do SDK, o campo pode variar; aqui usamos output_text
    return getattr(resp, "output_text", str(resp))

interface = gr.Interface(
    fn=responder,
    inputs=gr.Textbox(lines=3, placeholder="Digite sua pergunta aqui..."),
    outputs=gr.Textbox(label="Resposta"),
    title="Chatbot — IA na Prática"
)

if __name__ == "__main__":
    interface.launch()
