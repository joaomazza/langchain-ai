import os
from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

# Carregar variáveis do .env
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Configurar modelo do chatbot
llm = ChatOpenAI(model_name="gpt-4", openai_api_key=openai_api_key)

chat = APIRouter()
templates = Jinja2Templates(directory="templates")

# Corrigido: Removemos "/" para evitar duplicação no `server.py`
@chat.get("/", response_class=HTMLResponse)
async def get_chat(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})

@chat.post("/chat", response_class=HTMLResponse)
async def reposta_chat(message: str = Form(...)):  
    try:
        response = llm.invoke([HumanMessage(content=message)])
        return f"""<div class="bot-message"><strong>🤖 Bot:</strong> {response.content}</div>"""
    except Exception as e:
        return f"""<script>document.getElementById('error-message').innerText = "Erro ao processar: {str(e)}";</script>"""
