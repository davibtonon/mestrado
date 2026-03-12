import os
from dotenv import load_dotenv
from tools import load_csv

from langchain.agents import create_agent
from langchain_core.prompts import PromptTemplate 
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage

from langchain_google_genai import ChatGoogleGenerativeAI

from prompt import FIRST_TEMPLATE

load_dotenv()

## Prompt usando para inicia o agent

prompt = PromptTemplate.from_template(FIRST_TEMPLATE)
prompt_format = prompt.invoke({"log": "AWS_S3_HoneyBucketLogs.csv"}).text

name = "mistral-nemo"

def ollama_model():
    # Função para ser usada locais.
    return ChatOllama(
        model=name,
        model_provider='ollama',
        reasoning=True)


def google_model():
    # Função para cria o agent usando a LLM Gemini
    return ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")


def agent(model_func=ollama_model):
    
    return create_agent(
        model=model_func(),              # seu modelo ollama
        system_prompt=prompt_format,
        tools=[load_csv],
        #stream=False
    )

    #return agent# MUITO IMPORTANTE: não travar Jupyter


def prompt_test():
    messages = [
        SystemMessage(content="Você é um analista de dados especialista em ITSM."),
        HumanMessage(content="Explique o dataset."),
        HumanMessage(content="Agora conte os incidentes por prioridade."),
        HumanMessage(content="Agora gere insights avançados.")
    ]

    return  messages


def send_prompt(agent, messages):
    "Função para envia o prompt e mostra resposta"


    result = agent.invoke({"messages":"" })
    print(result["messages"][-1].content)