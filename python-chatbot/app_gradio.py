import gradio as gr
from openai import OpenAI
import os
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Verificação simples: evita erros comuns para iniciantes
if not OPENAI_API_KEY:
    raise ValueError(
        "A variável OPENAI_API_KEY não foi encontrada.\n"
        "Crie o arquivo .env e adicione:\nOPENAI_API_KEY=sua_chave_aqui"
    )

# Inicializa o cliente da OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)

def responder(pergunta):
    """
    Função que envia a pergunta para a API e devolve a resposta.
    Inclui tratamento de erros e fallback para casos de retorno incompleto.
    """
    try:
        resposta = client.responses.create(
            model="gpt-5.1-mini",
            input=pergunta
        )

        # Campo mais moderno e estável para extrair texto
        texto = getattr(resposta, "output_text", None)

        if not texto:
            # Fallback caso o SDK mude no futuro
            return "A IA respondeu, mas o texto não pôde ser interpretado."

        return texto

    except Exception as e:
        # Log opcional no terminal
        print(f"Erro na API: {e}")
        return "Não foi possível obter resposta da IA no momento."

# Interface gráfica com Gradio
interface = gr.Interface(
    fn=responder,
    inputs=gr.Textbox(label="Pergunta", placeholder="Digite sua pergunta aqui..."),
    outputs=gr.Textbox(label="Resposta"),
    title="Meu Chatbot com IA"
)

# Executa o app
interface.launch()
