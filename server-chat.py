import os
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

# Carregar variáveis do .env
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Configurar modelo do chatbot
llm = ChatOpenAI(model_name="gpt-4", openai_api_key=openai_api_key)

static_path = os.path.abspath("static")
print(f"📂 Caminho absoluto do diretório estático: {static_path}")
print(f"📄 Arquivos dentro do diretório estático: {os.listdir(static_path) if os.path.exists(static_path) else 'Diretório não encontrado!'}")

# Criar aplicação FastAPI
app = FastAPI()

# Configurar diretório de templates e arquivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Rota da interface do chatbot
@app.get("/", response_class=HTMLResponse)
async def get_chat(request: Request):
    return templates.TemplateResponse("index-chat.html", {"request": request})

# Endpoint para processar mensagens
@app.post("/chat", response_class=HTMLResponse)
async def chat(message: str = Form(...)):  # Pegando o campo "message" corretamente
    try:
        response = llm.invoke([HumanMessage(content=message)])
        return f"""
        <div class="bot-message"><strong>🤖 Bot:</strong> {response.content}</div>
        """
    except Exception as e:
        return f"""
        <script>
            document.getElementById('error-message').innerText = "Erro ao processar: {str(e)}";
        </script>
        """