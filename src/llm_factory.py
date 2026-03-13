import os
from typing import Dict

from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.language_models import BaseLanguageModel
from langchain_ollama import ChatOllama
from langchain_groq import ChatGroq


from config import settings

class LLMFactory:
    def __init__(self):
        self._creator: Dict[str, callable[[], BaseLanguageModel]] = {
            'openai': self._build_openai,
            'ollama': self._build_ollama,
            'gemini': self._build_gemini,
            'groq': self._build_groq
        }

    def _build_openai(self,) -> BaseLanguageModel:
        return ChatOpenAI(
            model = 'gpt-40',
            api_key = settings.OPENAI_API_KEY,
            temperature = 0
        )
    def _build_groq(self,) -> BaseLanguageModel:
        return ChatGroq(
            model = 'openai/gpt-oss-20b',
            max_tokens=None,

        )
    def _build_ollama(self, model: str = 'phi4-mini') -> BaseLanguageModel:
        return ChatOllama(
            model = settings.OLLAMA_MODEL,
            base_url = settings.OLLAMA_URL,
           # reasoning = True
        )
    
    def _build_gemini(self, model: str = 'gemini-2.5-flash-lite') -> BaseLanguageModel:
       return ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

    def get_model(self, provider_name: str):
        print(f"LLMFactory: Getting model for provider '{provider_name}'")
        creator = self._creator.get(provider_name.lower())
        if not creator:
            raise ValueError(f"Provider '{provider_name}' is not supported.")
       
        return creator()