from config import DATA_DIR, settings, LLM_REPORT
from model import agent
from langchain_core.messages import HumanMessage
from tools import set_csv_path
from prompt import CONTENT_PROMPT
from pathlib import Path


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
            HumanMessage(content=CONTENT_PROMPT.format(path_file=path_file))
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
    #for msg in messages:
    #    print(f"[{msg.__class__.__name__}]: {msg.content}")
    
    print("\n=== Final Report ===")
    print(last_message.content)

    save_file(last_message.content, path_file)


def save_file(msg, path_file):
    base_name = Path(path_file).stem
    provider = settings.LLM_PROVIDER
    
    if settings.LLM_PROVIDER == 'ollama':
        provider = settings.OLLAMA_MODEL

    file_name = f'{base_name}_{provider}.txt'
                     
    full_path = LLM_REPORT / file_name

    with open(full_path, "w", encoding="utf-8") as f:
        f.write(msg)
    
    print(f"Saved to: {full_path}")



# save_file('tes', file_path)

if __name__ == "__main__":

    files = [
        DATA_DIR / "file_01.json",
        DATA_DIR / "file_02.log",
        DATA_DIR / "file_03.csv"
    ]

    for file in files:
        print(file)
        print_analysis(str(file))
