import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

openai_api_key = os.getenv("OPENAI_API_KEY")

# Configurar modelo
llm = ChatOpenAI(model_name="gpt-4", openai_api_key=openai_api_key)

# Criar prompt de interação
messages = [
    SystemMessage(content="Você é um assistente especializado em tecnologia."),
    HumanMessage(content="Explique o que é LangChain.")
]

# Gerar resposta corretamente
resposta = llm.invoke(messages)
print(resposta.content)
