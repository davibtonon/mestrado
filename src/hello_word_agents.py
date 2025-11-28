from openai import OpenAI


BASE_URL = "http://localhost:11434/v1"
MODEL = "llama3.2"
PATH_FILE = "Incident_response.txt"

client = OpenAI(
    base_url=BASE_URL,
    api_key = "ollama")
# response = client.chat.completions.create(
#     model="llama3.2",
#     messages=[
#         {"role": "system", "content": "Você é um assistente útil"},
#         {"role": "user", "content": "Explique o que é aprendizado de supervisionado"},
#     ]
# )
#

# client.files.create(
#     file=open(PATH_FILE, "rb"),
#     purpose="fine-tune",
#     expires_after={
#     "anchor": "created_at",
#     "seconds": 2592000
#   }
# )
# response = client.responses.create(
#     model=MODEL,
#     tools=[{ "type": "web_search_preview" }],
#     input="What was a positive news story from today?",
# )
with open("incident_event_log.csv", "r", encoding="utf-8") as ev:
    event = ev.read()

with open(PATH_FILE, "r", encoding="utf-8") as f:
    texto = f.read()

prompt = f"""Analise arquivo separado por virgula e responda em pt-br:
        {event}"""
response = client.chat.completions.create(
    model = MODEL,
    messages=[{"role": "user", "content": prompt}]
)


print(response.choices[0].message.content)
