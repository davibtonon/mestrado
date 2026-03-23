from langchain.tools import tool 
from langchain_community.document_loaders import TextLoader, JSONLoader
from langchain_core.documents import Document

import pandas as pd
import os
import json
import csv
from typing import List

from pathlib import Path

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

        if ext in ['.txt', '.log']:
            return LogLoader._load_text(path)
        elif ext == '.json':
            return LogLoader._load_json(path)
        elif ext == '.csv':
            return LogLoader._load_csv(path)
        else:
            raise ValueError(f"Unsupported file type: {ext}")


    @staticmethod
    def _load_text(path: str) -> List[Document]:
        docs = []
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:
                    docs.append(Document(page_content=line))
        
        return docs


    @staticmethod
    def _load_json(path: str) -> list[Document]:
        docs = []
        
        with open(path, 'r', encoding='utf-8') as f:
            
            first_char = f.read(1)
            f.seek(0)
            if first_char == '[':
                data = json.load(f)
                for item in data:
                    docs.append(Document(page_content=json.dumps(item)))
            else:
                for line in f:
                    line = line.strip()
                    if line:
                        docs.append(Document(page_content=line))

        
        return docs

    @staticmethod
    def _load_csv(path: str) -> List[Document]:

        docs = []
        with open(path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                docs.append(Document(page_content=json.dumps(row)))

        return docs


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
    

if __name__ == '__main__':
    from config import DATA_DIR

    # Caminho do arquivo de log
    file_path = DATA_DIR / "file_linux.log"
    file_01 = DATA_DIR / "file_03.csv"
    path_file = file_01

    docs = LogLoader.get_doc(path_file)


    print(f"Total de documentos carregados: {len(docs)}")
    for i, doc in enumerate(docs[:5]):
        print(f"Documento {i+1}:", doc.page_content)