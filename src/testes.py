from langchain_community.document_loaders import JSONLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import DATA_DIR
import json
from tools import LogLoader



from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama


json_data = LogLoader().get_doc(DATA_DIR / "file_01.json")
# print(json_data[2])
# print(len(json_data[:10]))
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100
)

split_docs = splitter.split_documents(json_data)

print(f"Total de chunks: {len(split_docs)}")
# print(split_docs[0])


# 1. Configuração do Modelo Local
llm = ChatOllama(
    model="hf.co/mradermacher/SecGPT-7B-i1-GGUF:IQ4_XS",
    num_ctx=4096,
    temperature=0)

# 2. PROMPT DE MAPEAMENTO (MAP)
map_prompt = ChatPromptTemplate.from_template(
    "Analyze this JSON log excerpt and identify MITRE ATT&CK tactics, suspicious IPs, and anomalies: {context}"
)

# 3. PROMPT DE CONSOLIDAÇÃO (REDUCE)
reduce_prompt = ChatPromptTemplate.from_template(
    "Combine these partial analyses into a structured final incident report."
    "Highlight the verdict (Attack Yes/No) and the MITRE techniques found:\n\n{summaries}"
)


map_chain = map_prompt | llm | StrOutputParser()

def deploy_analysis(docs):
    # Executa o mapeamento para cada split do log
    partial_results = map_chain.batch([{"context": d.page_content} for d in docs])
    
    # Junta os resultados e passa para o prompt final
    combined_content = "\n\n".join(partial_results)
    final_report = (reduce_prompt | llm | StrOutputParser()).invoke({"summaries": combined_content})
    
    return final_report

relatorio = deploy_analysis(split_docs)
print(relatorio)

# splitter = RecursiveJsonSplitter()

# json_chunks = splitter.split_json(json_data=json_data, convert_lists=True)

# for chunk in json_chunks[:3]:
    # print(chunk)

# with open(DATA_DIR / "file_01.json", "r", encoding="utf-8") as f:
#     json_data = json.load(f)

# # json_data = JSONLoader(file_path= DATA_DIR / "file_01.json", jq_schema='.[]', text_content=False)

# print(type(json_data))
# print(json_data)

# docs = splitter.create_documents(texts=[json_data])
# for doc in docs[:3]:
#     print(doc)
# #for chunk in json_chunks[:3]:
# #    print(chunk)


# print()

# # loader = JSONLoader(file_path='C:\\davi_tonon\\mestrado\data\\raw\\file_01.json', jq_schema='.[]', text_content=False)
# # docs = loader.load()

# # text_splitter = RecursiveCharacterTextSplitter(chunk_size=4000, chunk_overlap=400)
# # split_docs = text_splitter.split_documents(docs)