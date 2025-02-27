# 🤖 ChatBot IA + RAG + Automação de Processos

## FastAPI + LangChain + DocLing + FAISS

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100.1-green?style=for-the-badge&logo=fastapi)
![LangChain](https://img.shields.io/badge/LangChain-0.1.0-yellow?style=for-the-badge)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple?style=for-the-badge&logo=bootstrap)
![FAISS](https://img.shields.io/badge/FAISS-Indexing-blueviolet?style=for-the-badge)
![HTMX](https://img.shields.io/badge/HTMX-Frontend-orange?style=for-the-badge)
![DocLing](https://img.shields.io/badge/DocLing-Parsing-blue?style=for-the-badge)

🚀 Este projeto combina um **ChatBot IA**, um **Sistema de Busca Inteligente baseado em RAG (Retrieval-Augmented Generation)** e uma **Automação de Processos**. Ele utiliza **FastAPI**, **LangChain**, **DocLing**, **FAISS** e **Bootstrap** para oferecer:

- 💬 **Chatbot IA** baseado em **LLMs**  
- 🔍 **Busca inteligente em documentos** **(PDF, DOCX, XLSX, CSV, HTML)**  
- 🤖 **Automação de extração, geração de relatórios e resumo de conteúdo**  
- 📄 **Processamento avançado de arquivos com DocLing**  
- 🎨 **Interface moderna e responsiva com Bootstrap + HTMX**  

---

## 📌 Tecnologias Utilizadas

- **[FastAPI](https://fastapi.tiangolo.com/)** - Framework web moderno para Python 🚀  
- **[LangChain](https://www.langchain.com/)** - Framework para trabalhar com modelos de linguagem (LLMs) 🧠  
- **[DocLing](https://ds4sd.github.io/docling/)** - Biblioteca para parsing de documentos diversos 📄  
- **[FAISS](https://faiss.ai/)** - Indexação vetorial para busca semântica rápida ⚡  
- **[HTMX](https://htmx.org/)** - Biblioteca para interações dinâmicas sem JavaScript excessivo 🔥  
- **[Bootstrap 5](https://getbootstrap.com/)** - Framework CSS para UI responsiva 🎨  
- **[Uvicorn](https://www.uvicorn.org/)** - Servidor ASGI para FastAPI ⚡  
- **[Python-Dotenv](https://pypi.org/project/python-dotenv/)** - Gerenciamento seguro de variáveis de ambiente 🔐  

---

## ⚙️ Instalação e Configuração

### 🔹 1. Clonar o repositório
```bash
git clone https://github.com/joaomazza/langchain-ai
cd langchain-ai
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
uvicorn server:app --reload
```
Acesse:
```
http://127.0.0.1:8000/chat
```

### 🔹 2. Executar o Sistema de Busca Inteligente (RAG)
```bash
uvicorn server:app --reload
```
Acesse:
```
http://127.0.0.1:8000/busca
```

### 🔹 3. Executar a Automação de Processos
```bash
uvicorn server:app --reload
```
Acesse:
```
http://127.0.0.1:8000/automacao
```

---

## 📌 Estrutura do Projeto

📂 **langchain-ai/**  
│-- 📂 **data/** → Arquivos para indexação (PDF, DOCX, XLSX, CSV, TXT)  
│-- 📂 **output/** → Diretório para arquivos processados  
│-- 📂 **resources/** → Módulos de processamento e automação  
│   ├── automation.py → Automação de relatórios e resumo de conteúdos  
│   ├── searching.py → Indexação e busca inteligente com FAISS  
│-- 📂 **routes/** → Módulos das rotas FastAPI  
│   ├── automacao.py → Rota para automação  
│   ├── busca.py → Rota de busca inteligente  
│   ├── chat.py → Rota do chatbot  
│-- 📂 **static/** → Arquivos estáticos (CSS, JS, imagens)  
│   ├── styles.css  
│-- 📂 **templates/** → Templates HTML  
│   ├── index.html → Página inicial  
│   ├── chat.html → Interface do chatbot  
│   ├── busca.html → Interface da busca inteligente  
│   ├── automacao.html → Interface da automação de processos  
│-- 📜 **.env** → Variáveis de ambiente (API Key)  
│-- 📜 **.gitignore** → Arquivos ignorados pelo Git  
│-- 📜 **README.md** → Documentação do projeto  
│-- 📜 **requirements.txt** → Dependências do projeto  
│-- 📜 **server.py** → Backend FastAPI que une todas as rotas  

---

## 🛠️ Funcionalidades Implementadas

✅ **Chatbot integrado com LangChain** 📢  
✅ **Busca Inteligente com RAG e FAISS** 🔍  
✅ **Indexação e extração de PDFs, Word, Excel, HTML com DocLing** 📄  
✅ **Automação de processos para gerar relatórios e resumos** 📊  
✅ **Interface moderna com Bootstrap 5 + HTMX** 🎨  
✅ **Modo escuro inspirado no tema Dracula** 🧛  
✅ **Gerenciamento seguro da API Key com `.env`** 🔐  

---

## 🏗️ Melhorias Futuras

🚀 **Adicionar histórico de mensagens no ChatBot** 📜  
🚀 **Suporte a múltiplos usuários** 👥  
🚀 **Integração com banco de dados para logs** 📊  
🚀 **Adicionar suporte a mais formatos como JSON, XML** 📝  
🚀 **Salvar e carregar embeddings para evitar reprocessamento** ⚡  
🚀 **Testar diferentes modelos (Mistral, Llama 2, Claude)** 🧠  

---

## 🤝 Contribuição
Se quiser contribuir com melhorias ou novas funcionalidades, fique à vontade para enviar um Pull Request! 😃🔥

📩 Para dúvidas ou sugestões, me chame! 🚀