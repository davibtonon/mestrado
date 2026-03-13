from langchain.tools import tool 
from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document

import pandas as pd
import os
from pathlib import Path

LOG_CACHE = None
CSV_PATH = None

def set_csv_path(path):
    global CSV_PATH
    CSV_PATH = path

class LogLoader:
    _LOADER = {
        '.txt': TextLoader,
        '.log': TextLoader
    }

    @classmethod
    def get_doc(cls, path:str) -> Document:
        ext = Path(path).suffix
        loader = cls._LOADER.get(ext)

        if not loader:
            raise ValueError(f"Unsupported file type: {ext}")
        
        return loader(path).load()
    

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
    
