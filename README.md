# 🤖 ChatBot IA + RAG

## FastAPI + LangChain + DocLing

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100.1-green?style=for-the-badge&logo=fastapi)
![LangChain](https://img.shields.io/badge/LangChain-0.1.0-yellow?style=for-the-badge)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple?style=for-the-badge&logo=bootstrap)

🚀 Este projeto combina um **ChatBot IA** com um **Sistema de Busca Inteligente baseado em RAG (Retrieval-Augmented Generation)** utilizando **FastAPI**, **LangChain**, **DocLing** e **Bootstrap**. O sistema permite:

- Conversar com um chatbot baseado em **LLMs** 📢
- Buscar informações em documentos **PDF, DOCX, XLSX, CSV, HTML** 🔍
- Processar arquivos com **DocLing** para extrair e indexar conteúdo 📄

---

## 📌 Tecnologias Utilizadas

- **[FastAPI](https://fastapi.tiangolo.com/)** - Framework web moderno para Python 🚀
- **[LangChain](https://www.langchain.com/)** - Framework para trabalhar com modelos de linguagem (LLMs) 🧠
- **[Docling](https://ds4sd.github.io/docling/)** - Simplifies document processing, parsing diverse formats 🧠
- **[HTMX](https://htmx.org/)** - Biblioteca para interações dinâmicas sem JavaScript excessivo 🔥
- **[Bootstrap 5](https://getbootstrap.com/)** - Framework CSS para UI responsiva 🎨
- **[Uvicorn](https://www.uvicorn.org/)** - Servidor ASGI para FastAPI ⚡
- **[Python-Dotenv](https://pypi.org/project/python-dotenv/)** - Gerenciamento seguro de variáveis de ambiente 🔐

---

## ⚙️ Instalação e Configuração

### 🔹 1. Clonar o repositório
```bash
    git clone https://github.com/joaomazza/langchain-ai
    cd chatbot-fastapi
```

### 🔹 2. Criar um ambiente virtual (opcional, mas recomendado)
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate    # Windows
```

### 🔹 3. Instalar as dependências
```bash
pip install -r requirements.txt
```

### 🔹 4. Configurar a chave da API OpenAI
Crie um arquivo **`.env`** na raiz do projeto e adicione:
```ini
OPENAI_API_KEY=SUA_CHAVE_AQUI
```

---


## 🚀 Como Rodar o Projeto

### 🔹 1. Executar o ChatBot Simples
```bash
uvicorn server-chat:app --reload
```
Acesse:
```
http://127.0.0.1:8000/
```

### 🔹 2. Executar o Sistema de Busca Inteligente (RAG)
```bash
uvicorn server:app --reload
```
Acesse:
```
http://127.0.0.1:8000/
```
```

Agora você pode interagir com o chatbot! 🤖💬

---

## 📌 Estrutura do Projeto

📂 langchain-ai/
│-- 📂 data/              # Arquivos para indexação (PDF, DOCX, XLSX, CSV, TXT)
│   ├── docs.txt
│   ├── exemplo.pdf
│   ├── exemplo.docx
│   ├── exemplo.xlsx
│-- 📂 static/            # Arquivos estáticos (CSS)
│   ├── styles.css
│-- 📂 templates/         # Templates HTML para renderização
│   ├── index.html        # Interface do chatbot e busca inteligente
│   ├── index-chat.html   # Interface exclusiva do chatbot
│-- 📜 .env               # Variáveis de ambiente (API Key)
│-- 📜 .gitignore         # Arquivos ignorados pelo Git
│-- 📜 README.md          # Documentação do projeto
│-- 📜 requirements.txt   # Dependências do projeto
│-- 📜 server.py          # Backend FastAPI (Busca Inteligente RAG)
│-- 📜 server-chat.py     # Backend FastAPI (ChatBot simples)
│-- 📜 test_docling.py    # Teste de extração de texto com DocLing
│-- 📜 comecando.py       # Script inicial de teste
```

---

## 🛠️ Funcionalidades Implementadas

✅ **Chatbot integrado com LangChain** 📢  
✅ **Busca Inteligente com RAG e FAISS** 🔍  
✅ **Indexação e extração de PDFs, Word, Excel, HTML com DocLing** 📄  
✅ **Interface moderna com Bootstrap 5** 🎨  
✅ **Modo escuro inspirado no tema Dracula** 🧛  
✅ **Gerenciamento seguro da API Key com `.env`** 🔐  

---

## 🏗️ Melhorias Futuras

🚀 **Adicionar histórico de mensagens** 📜  
🚀 **Suporte a múltiplos usuários** 👥  
🚀 **Integração com banco de dados para logs** 📊  
🚀 **Adicionar suporte a mais formatos como JSON, XML** 📝  
🚀 **Salvar e carregar embeddings para evitar reprocessamento** ⚡  
🚀 **Testar diferentes modelos (Mistral, Llama 2, Claude)** 🧠  

---

## 🤝 Contribuição
Se quiser contribuir com melhorias ou novas funcionalidades, fique à vontade para enviar um Pull Request! 😃🔥

📩 Para dúvidas ou sugestões, me chame! 🚀

