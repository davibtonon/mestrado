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

    LLM_PROVIDER: Literal['openai', 'ollama', 'gemini', 'llama'] = Field(default='llama')

    # 2. Chaves de API (o Pydantic valida se é string)
    OPENAI_API_KEY: str = Field(default="sk-placeholder")
    
    # Config for Google Gemini.
    GOOGLE_API_KEY: str = Field(default="ai-placeholder")
    GOOGLE_MODEL: str = Field(default="gemini-2.5-flash-lite")
    
    GROG_API_KEY: str = Field(default="gsk-placeholder")

    # Config for Ollama
    OLLAMA_URL: str = Field(default="http://localhost:11434")
    OLLAMA_MODEL: str = Field(default="qwen2.5:7b")
    

    LLAMA_MODEL: str = Field(default="foundation-sec-8b-reasoning-q4_k_m.gguf")
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # Config Gerais
    TEMPERATURE: float= Field(default=0.0, ge=0.0, le=1.0)
    NUM_TOKENS: int = Field(default=500)
    CHUNK_SIZE: int = Field(default=1000, gt=0, le=4096)

    CHUNK_OVERLAP: int = Field(default=100, ge=0) 
    
    @property
    def active_model(self):
        mapping = {
            "ollama": self.OLLAMA_MODEL,
            "gemini": self.GOOGLE_MODEL,
            "llama": self.LLAMA_MODEL,
        }

        return mapping.get(self.LLM_PROVIDER)

settings = Settings()

# Configurações de diretórios
PROJECT_DIR  = Path(__file__).resolve().parents[1]
BASE_DIR  = PROJECT_DIR / "src"           # project root
DATA_DIR = PROJECT_DIR / "data" / "raw"
LLM_REPORT = PROJECT_DIR / "data" /'report'



