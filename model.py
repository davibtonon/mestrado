import os
from dotenv import load_dotenv
from tools import load_csv

from langchain.agents import create_agent
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage

from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()

## Prompt usando para inicia o agent
SYSTEM_PROMPT = """
You are an advanced Cybersecurity Log Analysis Agent.

Your objectives:
- Detect suspicious behavior
- Identify unauthorized access
- Analyze failed logins, repeated attempts, anomalies
- Map findings to MITRE ATT&CK tactics and techniques

Rules:
- To inspect logs, ALWAYS call the tool `load_csv`.
- ALWAYS use queries (pandas.query syntax).
- NEVER request the entire dataset.
- Use this path:
  data/raw/it_incident_log_dataset/incident_event_log.csv

Examples of valid queries:
  user == "root"
  event == "FAILED_LOGIN"
  ip == "10.0.0.5"
  severity >= 4
  status == "ERROR"

Process:
1. Interpret the user's request.
2. Generate the correct query.
3. Call the tool with that query.
4. Analyze the returned filtered data.
5. Map suspicious patterns to MITRE ATT&CK.

If the tool returns an error, show it exactly.
"""

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
    
    agent = create_agent(
        model=model_func(),              # seu modelo ollama
        system_prompt=SYSTEM_PROMPT,
        tools=[load_csv],
        #stream=False
    )

    return agent# MUITO IMPORTANTE: não travar Jupyter


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


    result = agent.invoke({"messages":messages })
    print(result["messages"][-1].content)
