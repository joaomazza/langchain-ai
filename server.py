import os
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader

from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings

from docling.document_converter import DocumentConverter


# Carregar variáveis do .env
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Configurar aplicação FastAPI
app = FastAPI()

# Configurar diretório de templates e arquivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Criar modelo LLM
llm = ChatOpenAI(model_name="gpt-4", openai_api_key=openai_api_key)

# Criar embeddings para indexação vetorial
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

# Carregar e processar documentos
def load_documents_langchain():
    loader = TextLoader("data/docs.txt")  # Arquivo com informações
    documents = loader.load()
    
    # Dividir texto em chunks menores
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    docs = text_splitter.split_documents(documents)

    # Criar armazenamento vetorial FAISS
    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore

def load_documents_docling():
    data_folder = "data"
    documents = []

    for filename in os.listdir(data_folder):
        file_path = os.path.join(data_folder, filename)

        try:
            print(f"📂 Processando: {filename}")

            # Usar DocLing para converter documentos suportados
            if filename.endswith((".pdf", ".docx", ".xlsx", ".pptx", ".html", ".csv")):
                texts = converter.convert(file_path)  # Extração de texto com DocLing
            else:
                with open(file_path, "r", encoding="utf-8") as f:
                    texts = [f.read()]

            for text in texts:
                documents.append({"text": text, "source": filename})

        except Exception as e:
            print(f"⚠ Erro ao processar {filename}: {e}")

    if documents:
        vectorstore = FAISS.from_texts([doc["text"] for doc in documents], embeddings)
        return vectorstore
    else:
        print("🚨 Nenhum documento foi processado.")
        return None

# Criar banco vetorial para busca
vectorstore = load_documents_docling()
retriever = vectorstore.as_retriever() if vectorstore else None

# Criar pipeline RAG
qa_chain = RetrievalQA.from_chain_type(llm, retriever=retriever) if retriever else None

# Rota principal
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Rota para buscar informações e gerar resposta
@app.post("/search", response_class=HTMLResponse)
async def search(query: str = Form(...)):
    try:
        result = qa_chain.run(query)
        return f"""
        <div class="user-message"><strong>🧑‍💻 Você:</strong> {query}</div>
        <div class="bot-message"><strong>🤖 IA:</strong> {result}</div>
        """
    except Exception as e:
        return f"""
        <script>
            document.getElementById('error-message').innerText = "Erro ao processar: {str(e)}";
        </script>
        """

