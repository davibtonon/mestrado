from model import agent, google_model, send_prompt, prompt_test

my_agent = agent(google_model)
send_prompt(my_agent,prompt_test())

