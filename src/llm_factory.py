import os
from typing import Dict

from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.language_models import BaseLanguageModel
from langchain_ollama import ChatOllama
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatLlamaCpp

from config import settings

class LLMFactory:
    """Factory class to create Language Models based on provider name."""
    
    def __init__(self):
        self._creator: Dict[str, callable[[], BaseLanguageModel]] = {
            'openai': self._build_openai,
            'ollama': self._build_ollama,
            'gemini': self._build_gemini,
            'groq': self._build_groq,
            'llama': self._build_llama_cpp,
        }

    def _build_openai(self,) -> BaseLanguageModel:
        return ChatOpenAI(
            model = 'gpt-40',
            api_key = settings.OPENAI_API_KEY,
            temperature = settings.TEMPERATURE
        )
    def _build_groq(self,) -> BaseLanguageModel:
        return ChatGroq(
            model = 'openai/gpt-oss-20b',
            max_tokens = settings.NUM_TOKENS ,
        )
    
    def _build_ollama(self) -> BaseLanguageModel:
        return ChatOllama(
            model = settings.OLLAMA_MODEL,
            base_url = settings.OLLAMA_URL,
            temperature = settings.TEMPERATURE,
            num_ctx = settings.NUM_TOKENS,
            num_predict= 1000

           # reasoning = True
        )
    
    def _build_gemini(self) -> BaseLanguageModel:
       return ChatGoogleGenerativeAI(model=settings.GOOGLE_MODEL)


    def _build_llama_cpp(self) -> BaseLanguageModel:
        return ChatOpenAI(
            base_url="http://localhost:8080/v1",
            model = settings.LLAMA_MODEL,
            api_key = settings.OPENAI_API_KEY,
            temperature = settings.TEMPERATURE,
            max_tokens = settings.NUM_TOKENS,

        )
    

    def get_model(self, provider_name: str = settings.LLM_PROVIDER):
        print(f"LLMFactory: Getting model for provider '{provider_name}' - {settings.active_model}")
        creator = self._creator.get(provider_name.lower())
        if not creator:
            raise ValueError(f"Provider '{provider_name}' is not supported.")
       
        return creator()