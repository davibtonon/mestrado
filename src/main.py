from model import agent, google_model, send_prompt, prompt_test

my_agent = agent(google_model).invoke({"messages": "Analise o arquivo AWS_S3_HoneyBucketLogs.csv e mapear para as taticas, tecnicas e procedimento matriz Mitre ATT&CK"})
print(my_agent["messages"][-1].content)

