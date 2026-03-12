from langchain.tools import tool 
from langchain_community.document_loaders import CSVLoader
import pandas as pd
import os



LOG_CACHE = None
CSV_PATH = None

def set_csv_path(path):
    global CSV_PATH
    CSV_PATH = path

@tool
def load_csv(query=None, max_rows:int=10):
    """Lê o CSV arquivo e permite consultas seguras para o agente"""
    global LOG_CACHE, CSV_PATH

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
    
