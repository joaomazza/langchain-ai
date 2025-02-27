import os
from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv
from fastapi.templating import Jinja2Templates
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI

from resources.searching import load_documents_docling

# Carregar variáveis do .env
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Criar modelo LLM
llm = ChatOpenAI(model_name="gpt-4", openai_api_key=openai_api_key)

# Criar banco vetorial para busca
vectorstore = load_documents_docling()
retriever = vectorstore.as_retriever() if vectorstore else None

# Criar pipeline RAG
qa_chain = RetrievalQA.from_chain_type(llm, retriever=retriever) if retriever else None

busca = APIRouter()
templates = Jinja2Templates(directory="templates")  # Corrigido: templates estava ausente

@busca.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("busca.html", {"request": request})

@busca.get("/search", response_class=HTMLResponse)
async def search(query: str = Form(...)):
    try:
        if qa_chain:
            result = qa_chain.run(query)
        else:
            result = "⚠️ Nenhuma base de conhecimento carregada."
        return f"""<div class="bot-message"><strong>🤖 IA:</strong> {result}</div>"""
    except Exception as e:
        return f"""<script>document.getElementById('error-message').innerText = "Erro ao processar: {str(e)}";</script>"""