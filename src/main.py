from config import DATA_DIR
from model import agent
from langchain_core.messages import HumanMessage
from tools import set_csv_path


# def run_analysis(path_file:str):
#     set_csv_path(path_file)

#     return agent(path_file=path_file, provider='ollama').invoke({
#         "messages": [
#             HumanMessage(content=f"""
#                          Analyse the file {path_file} and:
                         
#                          1. Call load_csv to inspect structure.
#                          2. Query for suspicious patterns, anomalies, and security events.
#                          3. Map findings to MITRE ATT&CK tactics, techniques and procedures.
#                          4. Produce the full structured report.
                         
#                          File: {path_file}
#                          """)
#         ]
#     }
#     )

def run_analysis(path_file:str, provider: str | None = None):

    set_csv_path(path_file)

    if provider:
        from config import settings
        settings.LLM_PROVIDER = provider

    return agent(path_file=path_file).invoke({
        "messages": [
            HumanMessage(content=f"""
                         Analyse the file {path_file} and:
                         
                         1. Call 'load_log_file' to read the file.
                         2. Query for suspicious patterns, anomalies, and security events.
                         3. Map findings to MITRE ATT&CK tactics, techniques and procedures.
                         4. Produce the full structured report.
                         
                         File: {path_file}
                         """)
        ]
    }
    )

def print_analysis(path_file:str):
    result = run_analysis(path_file)
    messages = result.get("messages", [])
    if not messages:
        print("No messages returned from agent.")
        return None
    
    last_message = messages[-1]
    print("=== Agent Trace ===")
    for msg in messages:
        print(f"[{msg.__class__.__name__}]: {msg.content}")
    
    print("\n=== Final Report ===")
    print(last_message.content)


file_path = DATA_DIR / "file_linux.log"

print(file_path)
print_analysis(str(file_path))

