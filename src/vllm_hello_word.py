
from openai import OpenAI
import config

# client = OpenAI(base_url=config.VLLM_ENDPOINT, api_key=config.OPENAI_API_KEY)
client = config.CUSTOM_CLIENT

resp = client.responses.create(
    model=config.MODEL_NAME ,
    input="What is machine learning ?",
    #max_tokens=50 
)

print(resp.choices[0].text) 
