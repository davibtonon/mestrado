# from langchain_community.document_loaders import JSONLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# import json
# from tools import LogLoader



# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_ollama import ChatOllama


# json_data = LogLoader().get_doc(DATA_DIR / "file_01.json")
# # print(json_data[2])
# # print(len(json_data[:10]))
# splitter = RecursiveCharacterTextSplitter(
#     chunk_size=1000,
#     chunk_overlap=100
# )

# split_docs = splitter.split_documents(json_data)

# print(f"Total de chunks: {len(split_docs)}")
# # print(split_docs[0])


# # 1. Configuração do Modelo Local
# llm = ChatOllama(
#     model="hf.co/mradermacher/SecGPT-7B-i1-GGUF:IQ4_XS",
#     num_ctx=4096,
#     temperature=0)

# # 2. PROMPT DE MAPEAMENTO (MAP)
# map_prompt = ChatPromptTemplate.from_template(
#     "Analyze this JSON log excerpt and identify MITRE ATT&CK tactics, suspicious IPs, and anomalies: {context}"
# )

# # 3. PROMPT DE CONSOLIDAÇÃO (REDUCE)
# reduce_prompt = ChatPromptTemplate.from_template(
#     "Combine these partial analyses into a structured final incident report."
#     "Highlight the verdict (Attack Yes/No) and the MITRE techniques found:\n\n{summaries}"
# )


# map_chain = map_prompt | llm | StrOutputParser()

# def deploy_analysis(docs):
#     # Executa o mapeamento para cada split do log
#     partial_results = map_chain.batch([{"context": d.page_content} for d in docs])
    
#     # Junta os resultados e passa para o prompt final
#     combined_content = "\n\n".join(partial_results)
#     final_report = (reduce_prompt | llm | StrOutputParser()).invoke({"summaries": combined_content})
    
#     return final_report

# relatorio = deploy_analysis(split_docs)
# print(relatorio)

# # splitter = RecursiveJsonSplitter()

# # json_chunks = splitter.split_json(json_data=json_data, convert_lists=True)

# # for chunk in json_chunks[:3]:
#     # print(chunk)

# # with open(DATA_DIR / "file_01.json", "r", encoding="utf-8") as f:
# #     json_data = json.load(f)

# # # json_data = JSONLoader(file_path= DATA_DIR / "file_01.json", jq_schema='.[]', text_content=False)

# # print(type(json_data))
# # print(json_data)

# # docs = splitter.create_documents(texts=[json_data])
# # for doc in docs[:3]:
# #     print(doc)
# # #for chunk in json_chunks[:3]:
# # #    print(chunk)


# # print()

# # # loader = JSONLoader(file_path='C:\\davi_tonon\\mestrado\data\\raw\\file_01.json', jq_schema='.[]', text_content=False)
# # # docs = loader.load()

# # # text_splitter = RecursiveCharacterTextSplitter(chunk_size=4000, chunk_overlap=400)
# # # split_docs = text_splitter.split_documents(docs)

# # import json
# # from langchain_text_splitters import RecursiveJsonSplitter

# # with open("data\\raw\\psh_powershell_httplistener_2020-11-0204130683.json", "r", encoding="utf-8") as f:
# #     data = json.load(f)

# # with open("data\\raw\\file_01.json", "r", encoding="utf-8") as f:
# #     data = json.load(f)


# # splitter = RecursiveJsonSplitter(max_chunk_size=1000,     )

# # json_chunks = splitter.split_json(json_data=data, convert_lists=True)

# # for i, chunk in enumerate(json_chunks[:], start=1):
# #     print(f"Chunk {i}:")
# #     print(chunk)
# #     print("-" * 80)
from langchain_text_splitters import CharacterTextSplitter
from tools import LogLoader
from config import DATA_DIR

# with open(DATA_DIR / 'sh_arp_cache_2020-11-10074812.log', "r", encoding="utf-8") as f:
#     state_of_the_union = f.read()

# text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
#     encoding_name="cl100k_base", chunk_size=1000, chunk_overlap=0
# )
# texts = text_splitter.split_text(state_of_the_union)
files = [
            DATA_DIR / "file_02.log",
            DATA_DIR / 'sh_arp_cache_2020-11-10074812.log',
            DATA_DIR / 'Microsoft365DefenderEvents.json',
            DATA_DIR / 'WindowsEvents.json',
            DATA_DIR / "file_01.json",
            DATA_DIR / "file_03.csv",

   
    ]


for file in files:
    test = LogLoader.get_doc(file)
    print(f"{file}: {len(test)}")


# test = LogLoader.get_doc(DATA_DIR / 'sh_arp_cache_2020-11-10074812.log')
# print(len(test))

# json_data = LogLoader().get_doc(DATA_DIR / "Microsoft365DefenderEvents.json")
# print(len(json_data))