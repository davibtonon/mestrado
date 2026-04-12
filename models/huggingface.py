from huggingface_hub import hf_hub_download

# # Download the model foundation-sec-8b-reasoning-q4_k_m 
# hf_hub_download(
#     repo_id="fdtn-ai/Foundation-Sec-8B-Reasoning-Q4_K_M-GGUF", 
#     filename="foundation-sec-8b-reasoning-q4_k_m.gguf",
#     local_dir="./models")




hf_hub_download(
    repo_id="fdtn-ai/Foundation-Sec-1.1-8B-Instruct-Q4_K_M-GGUF", 
    filename="foundation-sec-1.1-8b-instruct-q4_k_m.gguf",
    local_dir="./models")

