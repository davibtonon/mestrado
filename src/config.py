from dotenv import load_dotenv
from openai import OpenAI

import os

# Carrega variáveis do .env automaticamente
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
VLLM_ENDPOINT = os.getenv("VLLM_ENDPOINT", "http://localhost:8000/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "llama-3-1b")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"


CUSTOM_CLIENT = OpenAI(
    base_url=VLLM_ENDPOINT,
    api_key=OPENAI_API_KEY)
