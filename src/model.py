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
    reduce_chain = REDUCE_PROMPT | llm_agent | StrOutputParser()

    # Segurança extra: limitar tamanho enviado no map
    map_inputs = [
        {"context": d.page_content[:800]}
        for d in docs
    ]

    partial_results = map_chain.batch(
        map_inputs,
        config={"max_concurrency": 2}
    )

    # Remove vazios
    partial_results = [r.strip() for r in partial_results if r and r.strip()]

    # Reduce em árvore para não estourar contexto
    step = 3

    while len(partial_results) > 1:
        reduced = []

        for i in range(0, len(partial_results), step):
            batch = "\n\n".join(partial_results[i:i + step])

            result = reduce_chain.invoke({
                "summaries": batch[:2500]  # trava de segurança
            })

            if result and result.strip():
                reduced.append(result.strip())

        partial_results = reduced

    return partial_results[0] if partial_results else "Nenhum resultado gerado."



if __name__ == "__main__":
    files = [
       # DATA_DIR / "file_02.log",
       # DATA_DIR / "file_03.csv",
       # DATA_DIR / "file_01.json",
       DATA_DIR / 'file_03_drain3_output.txt',
       DATA_DIR / 'file_01_drain3_output.txt',
       
    ]

    for file in files:
        json_data = LogLoader().get_doc(file)
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100 )
        split_docs = splitter.split_documents(json_data)

        print(f"Total de chunks: {len(split_docs)}")
        
        relatorio = deploy_analysis(split_docs)
        print(relatorio)

        save_file(relatorio, file)
        