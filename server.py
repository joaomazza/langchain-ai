import os

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

# Importando rotas separadas
from routes.chat import chat 
from routes.busca import busca 
from routes.automacao import automacao 

# Criar pastas se não existirem
for folder in ["output", "data"]:
    os.makedirs(folder, exist_ok=True)

# Criar API FastAPI
app = FastAPI()

# Montar diretórios estáticos corretamente
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/output", StaticFiles(directory="output"), name="output")

templates = Jinja2Templates(directory="templates")

# Página inicial
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Incluindo os módulos
app.include_router(chat, prefix="/chat")
app.include_router(busca, prefix="/busca")
app.include_router(automacao, prefix="/automacao")

# Inicializar o servidor
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)