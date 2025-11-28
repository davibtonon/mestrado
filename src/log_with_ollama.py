from openai import OpenAI
import pandas as pd
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

OLLAMA_BASE_URL = "http://localhost:11434/v1"
OLLAMA_API_KEY = "ollama-key"  # Pode ser qualquer string não vazia
OLLAMA_MODEL = "llama3.2"


client = OpenAI(
    base_url=OLLAMA_BASE_URL,
    api_key=OLLAMA_API_KEY
)

def analyse_csv(path_file:str, n_rows:int= 50,) -> str:
    df = pd.read_csv(path_file)
    df_sample = df.head(n_rows)
    df_markdown = df_sample.to_markdown(index=False)
    
    return df_markdown

df_amostra = analyse_csv('incident_event_log.csv')

with open("Incident_response.txt") as f:
    metadados_txt = f.read()

sy_prompt = (
    "Você é um analista de dados especialista em logs. Analise os dados tabulares"
    "fornecidos (no formato Markdown) e responda de acordo com as instruções do usuário."
)

prompt_analise = "No arquivos de metadados tem informações sobre as coluans dos arquivos. O que poder me dizer ? Consegue encontra algum padrão ? Alguns do IP são de usuarios mal intencionados ?"

content = f"""
    ### DOCUMENTAÇÃO DAS COLUNAS (CRUCIAL):
    {metadados_txt}
    
    ### DADOS BRUTOS (Amostra de {len(df_amostra)} linhas):
    {df_amostra}
    
    ### INSTRUÇÃO DE ANÁLISE:
    {prompt_analise}

"""

messages = [
    {"role": "system", "content":sy_prompt},
    {"role": "user", "content":content}
]
response = client.chat.completions.create(
    model=OLLAMA_MODEL,
    messages=messages
)

print(response.choices[0].message.content)
