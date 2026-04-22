from langchain.tools import tool 
from langchain_community.document_loaders import TextLoader, JSONLoader
from langchain_core.documents import Document
from sqlalchemy import text
from config import settings, LLM_REPORT
# from transformers import AutoTokenizer
from langchain_text_splitters import CharacterTextSplitter,RecursiveJsonSplitter,RecursiveCharacterTextSplitter

import pandas as pd
import os
import json
import csv
from typing import List

from pathlib import Path
import requests
from config import DATA_DIR
#from llama_cpp import Llama


LOG_CACHE = None
CSV_PATH = None

def set_csv_path(path):
    global CSV_PATH
    CSV_PATH = path

class LogLoader:
    _LOADER = {
        '.txt': TextLoader,
        '.log': TextLoader,
        '.json': JSONLoader,
    }

    @staticmethod
    def get_doc(path:str) -> List[Document]:
        ext = Path(path).suffix.lower()
        # tokenizer = AutoTokenizer.from_pretrained("hf-internal-testing/llama-tokenizer")

        # with open(path, "r", encoding="utf-8") as f:
        #     text = f.read()

        # tokens = tokenizer.encode(text)
        # print(f"Número de tokens: {len(tokens)}")
        
        
        if ext in ['.txt', '.log']:
            return LogLoader._load_text(path)
        elif ext == '.json':
            return LogLoader._load_json(path)
        elif ext == '.csv':
            return LogLoader._load_csv(path)
        else:
            raise ValueError(f"Unsupported file type: {ext}")


    @staticmethod
    def _load_text(path: str):

        with open(path, 'r', encoding='utf-8') as f:
            data = f.read()

        text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
            encoding_name="cl100k_base", 
            chunk_size=settings.CHUNK_SIZE, 
            chunk_overlap=settings.CHUNK_OVERLAP
            )
            
        return text_splitter.split_text(data)


    @staticmethod
    def _load_json(path: str):
        
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        splitter = RecursiveJsonSplitter( 
            max_chunk_size=settings.CHUNK_SIZE,
           )
        
        return  splitter.split_json(json_data=data,  convert_lists=True)
    

    @staticmethod
    def _load_json_metadata(path: str) -> list[Document]:
        docs = []
        
        with open(path, 'r', encoding='utf-8') as f:
            
            first_char = f.read(1)
            f.seek(0)
            if first_char == '[':
                data = json.load(f)
                print(enumerate(data))

                for i, item in enumerate(data):
                    docs.append(
                        Document(
                            page_content=json.dumps(item, ensure_ascii=False),
                            metadata={
                                "source": path,
                                "index": i
                            }))
                
            else:
                for i, line in enumerate(f):
                    line = line.strip()
                    if line:
                        try:
                            item = json.loads(line)
                            content = json.dumps(item, ensure_ascii=False)
                        except json.JSONDecodeError:
                            content = line

                        docs.append(
                            Document(
                                page_content=content,
                                metadata={
                                    "source": path,
                                    "index":i,
                                }))

        
        return docs

    @staticmethod
    def _load_csv(path: str) -> List[Document]:

        docs = []
        with open(path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                docs.append(Document(page_content=json.dumps(row)))
        
        splitter = RecursiveCharacterTextSplitter(
             chunk_size=settings.CHUNK_SIZE,
             chunk_overlap=settings.CHUNK_OVERLAP,
        )

        return splitter.split_documents(docs)


@tool
def load_log_file(path: str) -> list[Document]:
    """Load log file and return its content as a Document."""
    docs = LogLoader.get_doc(path)

    return docs


@tool
def load_csv(query:str | None = None, max_rows:int | None = 1000):
    """Load and query CSV logs. max_rows is the maximum number of rows to return."""
    
    global LOG_CACHE, CSV_PATH
    
    print("Path recebido:", CSV_PATH)
    print("Arquivo existe:", os.path.exists(CSV_PATH))
    
    try:
        if LOG_CACHE is None:
            LOG_CACHE = pd.read_csv(CSV_PATH)

        df = LOG_CACHE

        if query is None:
            return {
                "status": "ok",
                "columns": list(df.columns),
                "rows": len(df),
                "sample": df.head(5).to_dict(),
                "message": "Use a query parameter  to filter logs."
            }

        result = df.query(query).head(max_rows)

        return {
            "status": "ok",
            "returned_rows": len(result),
            "query_executed": query,
            "data": result.to_dict()
        }

    except Exception as e:
        return {"Status": "Error", "message": str(e) }
    

def save_file(msg, path_file):
    base_name = Path(path_file).stem
    
    file_name = f'{base_name}_{settings.LLM_PROVIDER}.txt'           

    if settings.LLM_PROVIDER == "ollama":
        file_name = f'{base_name}_{settings.OLLAMA_MODEL}.txt'
    
    full_path = LLM_REPORT / file_name

    with open(full_path, "w", encoding="utf-8") as f:
        f.write(msg)
    
    print(f"Saved to: {full_path}")



def count_tokens(file_path):
    """Extrai texto de diferentes tipos de arquivos."""

    SERVER_URL = "http://localhost:8080/tokenize"
    
    llm = Llama(
    model_path="..\\models\\foundation-sec-1.1-8b-instruct-q4_k_m.gguf",
    n_ctx=65536,
    verbose=False
    )

    files_chuncks = LogLoader.get_doc(file_path)
    n_tokesns = 0
    print(f"Processndo: {file_path.name}")
    print(f"Total de chunks: {len(files_chuncks)}")
    texts = []

    for chunk in files_chuncks:
        if isinstance(chunk, (dict, list)):
            texts.append(json.dumps(chunk, ensure_ascii=False))
        else:
            texts.append(str(chunk))
    texts = "\n\n".join(texts)
    tokens = llm.tokenize(texts.encode("utf-8"))

    print(f"Número de tokens: {len(tokens)}")


if __name__ == '__main__':
    files = [
                DATA_DIR / "file_02.log",
                DATA_DIR / 'sh_arp_cache_2020-11-10074812.log',
                DATA_DIR / 'Microsoft365DefenderEvents.json',
                DATA_DIR / 'WindowsEvents.json',
                DATA_DIR / "file_01.json",
                DATA_DIR / "file_03.csv",
        ]
    
    for file in files:
        count_tokens(file)