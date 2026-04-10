from langchain.agents import create_agent, AgentState
from langchain_core.prompts import PromptTemplate 

from tools import load_csv, load_log_file
from llm_factory import LLMFactory
from prompt import FIRST_TEMPLATE, SYSTEM_PROMPT, MAP_PROMPT, REDUCE_PROMPT
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_core.output_parsers import StrOutputParser
from tools import LogLoader, save_file
from config import DATA_DIR


## Prompt usando para inicia o agent
def built_prompt(path_file):
    """Construct the system prompt for the agent"""
    #prompt = PromptTemplate.from_template(FIRST_TEMPLATE)
    prompt = PromptTemplate.from_template(SYSTEM_PROMPT)
    return prompt.invoke({"context": path_file}).text


def agent(path_file:str=""):
    system_prompt= built_prompt(path_file)
    return create_agent(
        model= LLMFactory().get_model(), 
        system_prompt=system_prompt,
        #tools=[load_log_file],
        debug=False
        #stream=False
    )


def deploy_analysis(docs):
    llm_agent = LLMFactory().get_model()
    map_chain = MAP_PROMPT | llm_agent | StrOutputParser()
   
    # Executa o mapeamento para cada split do log
    partial_results = map_chain.batch([{"context": d.page_content} for d in docs])
    
    # Junta os resultados e passa para o prompt final
    combined_content = "\n\n".join(partial_results)
    final_report = (REDUCE_PROMPT | llm_agent | StrOutputParser()).invoke({"summaries": combined_content})
    
    return final_report



if __name__ == "__main__":
    files = [
        DATA_DIR / "file_02.log",
        DATA_DIR / "file_03.csv",
        DATA_DIR / "file_01.json",
    ]

    for file in files:
        json_data = LogLoader().get_doc(file)
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100 )
        split_docs = splitter.split_documents(json_data)

        print(f"Total de chunks: {len(split_docs)}")
        
        relatorio = deploy_analysis(split_docs)
        print(relatorio)

        save_file(relatorio, file)
        