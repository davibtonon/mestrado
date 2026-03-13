import os
from config import DATA_DIR
from model import agent, google_model, send_prompt, prompt_test
from langchain_core.messages import HumanMessage
from tools import set_csv_path


def run_analysis(path_file:str, model_func=google_model):
    set_csv_path(path_file)

    return agent(path_file=path_file).invoke({
        "messages": [
            HumanMessage(content=f"""
                         Analyse the file {path_file} and:
                         
                         1. Call load_csv with path_file="{path_file}" to inspect structure.
                         2. Query for suspicious patterns, anomalies, and security events.
                         3. Map findings to MITRE ATT&CK tactics, techniques and procedures.
                         4. Produce the full structured report.
                         
                         File: {path_file}
                         """)
        ]
    }
    )


def print_analysis(path_file:str, model_func=google_model):
    result = run_analysis(path_file, model_func)
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


file_path = DATA_DIR / "AWS_S3_HoneyBucketLogs.csv"

print(file_path)
print_analysis(str(file_path))

        #my_agent = agent(google_model).invoke({"messages": "Analise o arquivo AWS_S3_HoneyBucketLogs.csv e mapear para as taticas, tecnicas e procedimento matriz Mitre ATT&CK"})
#print(run_analysis(
 #   os.path.join(DATA_DIR, "AWS_S3_HoneyBucketLogs.csv"), 
  #  google_model)["messages"][-1].content)

