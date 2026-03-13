from langchain.agents import create_agent
from langchain_core.prompts import PromptTemplate 

from tools import load_csv
from llm_factory import LLMFactory
from prompt import FIRST_TEMPLATE, SYSTEM_PROMPT

## Prompt usando para inicia o agent
def built_prompt(path_file):
    #prompt = PromptTemplate.from_template(FIRST_TEMPLATE)
    prompt = PromptTemplate.from_template(SYSTEM_PROMPT)
    return prompt.invoke({"path_file": path_file}).text


def agent(path_file:str, provider='ollama'):
    system_prompt= built_prompt(path_file)
    return create_agent(
        model= LLMFactory().get_model(provider), 
        system_prompt=system_prompt,
        tools=[load_csv],
        #stream=False
    )
