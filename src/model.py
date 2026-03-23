from langchain.agents import create_agent, AgentState
from langchain_core.prompts import PromptTemplate 

from tools import load_csv, load_log_file
from llm_factory import LLMFactory
from prompt import FIRST_TEMPLATE, SYSTEM_PROMPT

## Prompt usando para inicia o agent
def built_prompt(path_file):
    """Construct the system prompt for the agent, inserting the file path."""
    #prompt = PromptTemplate.from_template(FIRST_TEMPLATE)
    prompt = PromptTemplate.from_template(SYSTEM_PROMPT)
    return prompt.invoke({"path_file": path_file}).text


def agent(path_file:str):
    system_prompt= built_prompt(path_file)
    return create_agent(
        model= LLMFactory().get_model(), 
        system_prompt=system_prompt,
        tools=[load_log_file],
        debug=False
        #stream=False
    )
