import shutil
import os

from dotenv import load_dotenv
from fastapi import APIRouter, UploadFile, File, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse, JSONResponse, HTMLResponse
from resources.automation import extract_data, generate_report, summarize_text

# Carregar variáveis do .env
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

automacao = APIRouter()
templates = Jinja2Templates(directory="templates")  # Corrigido: templates estava ausente

@automacao.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("automacao.html", {"request": request})

# Corrigido: Alterado de GET para POST para suportar upload corretamente
@automacao.post("/automate/")
async def automate_process(file: UploadFile = File(...)):
    file_location = f"data/{file.filename}"
    
    # Salvar arquivo enviado
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extração de dados
    extracted_text = extract_data(file_location)
    
    if extracted_text:
        # Gerar resumo com IA (corrigido para incluir `openai_api_key`)
        summary = summarize_text(extracted_text, openai_api_key=openai_api_key)
        
        # Criar relatório
        generate_report(summary)

        return JSONResponse(content={
            "message": "Processamento concluído",
            "summary": summary,
            "report": "/output/relatorio_automatizado.docx"
        })
    
    return JSONResponse(content={"message": "Erro ao processar documento"}, status_code=400)
