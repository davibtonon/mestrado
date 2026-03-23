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
    """Class to hold all configuration settings for the application."""

    LLM_PROVIDER: Literal['openai', 'ollama', 'gemini'] = Field(default='ollama')

    # 2. Chaves de API (o Pydantic valida se é string)
    OPENAI_API_KEY: str = Field(default="sk-placeholder")
    
    # Config for Google Gemini.
    GOOGLE_API_KEY: str = Field(default="ai-placeholder")
    GOOGLE_MODEL: str = Field(default="gemini-2.5-flash-lite")
    
    GROG_API_KEY: str = Field(default="gsk-placeholder")

    # Config for Ollama
    OLLAMA_URL: str = Field(default="http://localhost:11434")
    OLLAMA_MODEL: str = Field(default="qwen2.5:7b")
    
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()

# Configurações de diretórios
PROJECT_DIR  = Path(__file__).resolve().parents[1]
BASE_DIR  = PROJECT_DIR / "src"           # project root
DATA_DIR = PROJECT_DIR / "data" / "raw"



