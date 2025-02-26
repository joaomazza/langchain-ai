# 🤖 ChatBot IA - FastAPI + LangChain + Bootstrap

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100.1-green?style=for-the-badge&logo=fastapi)
![LangChain](https://img.shields.io/badge/LangChain-0.1.0-yellow?style=for-the-badge)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple?style=for-the-badge&logo=bootstrap)

🚀 Um chatbot simples e poderoso construído com **FastAPI**, **LangChain** e **Bootstrap 5**. Este projeto permite conversar com uma IA via interface web moderna e responsiva.

---

## 📌 Tecnologias Utilizadas

- **[FastAPI](https://fastapi.tiangolo.com/)** - Framework web moderno para Python 🚀
- **[LangChain](https://www.langchain.com/)** - Framework para trabalhar com modelos de linguagem (LLMs) 🧠
- **[HTMX](https://htmx.org/)** - Biblioteca para interações dinâmicas sem JavaScript excessivo 🔥
- **[Bootstrap 5](https://getbootstrap.com/)** - Framework CSS para UI responsiva 🎨
- **[Uvicorn](https://www.uvicorn.org/)** - Servidor ASGI para FastAPI ⚡
- **[Python-Dotenv](https://pypi.org/project/python-dotenv/)** - Gerenciamento seguro de variáveis de ambiente 🔐

---

## ⚙️ Instalação e Configuração

### 🔹 1. Clonar o repositório
```bash
    git clone https://github.com/seu-usuario/chatbot-fastapi.git
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

### 🔹 1. Executar o servidor FastAPI
```bash
uvicorn server:app --reload
```

### 🔹 2. Acessar a interface web
Abra o navegador e acesse:
```
http://127.0.0.1:8000/
```

Agora você pode interagir com o chatbot! 🤖💬

---

## 📄 Estrutura do Projeto
```bash
📂 chatbot-fastapi/
│-- 📂 static/          # Arquivos estáticos (CSS, JS, imagens)
│   ├── styles.css      # Tema Dracula para o chat
│-- 📂 templates/       # Templates HTML para renderização
│   ├── index.html      # Interface do chatbot
│-- 📜 .env             # Variáveis de ambiente (API Key)
│-- 📜 requirements.txt # Dependências do projeto
│-- 📜 server.py        # Backend FastAPI
│-- 📜 README.md        # Documentação do projeto
```

---

## 🛠️ Funcionalidades Implementadas

✅ **Chatbot integrado com LangChain** 📢  
✅ **Interface moderna com Bootstrap 5** 🎨  
✅ **Respostas dinâmicas com HTMX (sem precisar de JS pesado!)** ⚡  
✅ **Efeito de "digitando..." enquanto a IA responde** ⏳  
✅ **Modo escuro inspirado no tema Dracula** 🧛  
✅ **Gerenciamento seguro da API Key com `.env`** 🔐  

---

## 🏗️ Melhorias Futuras

🚀 **Adicionar histórico de mensagens** 📜  
🚀 **Suporte a múltiplos usuários** 👥  
🚀 **Integração com banco de dados para logs** 📊  

---

## 🤝 Contribuição
Se quiser contribuir com melhorias ou novas funcionalidades, fique à vontade para enviar um Pull Request! 😃🔥

📩 Para dúvidas ou sugestões, me chame! 🚀

