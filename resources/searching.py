import os
from dotenv import load_dotenv

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader

from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings

from docling.document_converter import DocumentConverter

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

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
    """Carrega e processa documentos da pasta 'data' e cria um índice vetorial FAISS."""
    
    data_folder = "data"
    documents = []
    converter = DocumentConverter()  # Inicializa o conversor do DocLing

    for filename in os.listdir(data_folder):
        file_path = os.path.join(data_folder, filename)

        try:
            print(f"📂 Processando: {filename}")

            # Usar DocLing para converter documentos suportados
            if filename.endswith((".pdf", ".docx", ".xlsx", ".pptx", ".html", ".csv")):
                result = converter.convert(file_path)  # Extração de texto com DocLing

                # Verifica se a conversão foi bem-sucedida
                if result.status.value.lower() != "success":
                    print(f"⚠ Falha ao processar {filename}: {result.status.value}")
                    continue

                texts = []
                for text_item in result.document.texts:
                    if hasattr(text_item, 'text') and text_item.text:
                        texts.append(text_item.text.strip())

            else:
                # Para arquivos de texto padrão
                with open(file_path, "r", encoding="utf-8") as f:
                    texts = [f.read()]

            # Adiciona os textos processados ao vetor de documentos
            for text in texts:
                documents.append({"text": text, "source": filename})

        except Exception as e:
            print(f"⚠ Erro ao processar {filename}: {e}")

    # Criar o índice vetorial FAISS se houver documentos processados
    if documents:
        embeddings = OpenAIEmbeddings()
        vectorstore = FAISS.from_texts([doc["text"] for doc in documents], embeddings)
        return vectorstore
    else:
        print("🚨 Nenhum documento foi processado.")
        return None