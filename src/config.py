from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, HttpUrl
from typing import Literal

from dotenv import load_dotenv
from openai import OpenAI
import os
from pathlib import Path

# Carrega variáveis do .env automaticamente
load_dotenv()


class Settings(BaseSettings):
    LLM_PROVIDER: Literal['openai', 'ollama', 'gemini'] = Field(default='ollama')

    # 2. Chaves de API (o Pydantic valida se é string)
    OPENAI_API_KEY: str = Field(default="sk-placeholder")
    GOOGLE_API_KEY: str = Field(default="ai-placeholder")
    GROG_API_KEY: str = Field(default="gsk-placeholder")
    
    OLLAMA_URL: str = Field(default="http://localhost:11434")
    OLLAMA_MODEL: str = Field(default="phi4-mini")
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()

# Configurações de diretórios
BASE_DIR = Path(__file__).parent        # src/
PROJECT_DIR = BASE_DIR.parent           # project root
DATA_DIR = PROJECT_DIR / "data" / "raw"

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
VLLM_ENDPOINT = os.getenv("VLLM_ENDPOINT", "http://localhost:8000/v1")

DEBUG = os.getenv("DEBUG", "False").lower() == "true"
RUN_LOCAL = True

try:
    CUSTOM_CLIENT = OpenAI(
        base_url=VLLM_ENDPOINT,
        api_key=OPENAI_API_KEY)
except Exception as e:
    print(f"Error initializing OpenAI client: {e}")
    CUSTOM_CLIENT = None