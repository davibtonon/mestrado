# Imagem base do Anaconda
FROM continuumio/anaconda3

# Evita prompts interativos
ENV DEBIAN_FRONTEND=nointeractive

# Instala o Jupyter Notebook
RUN conda install -y --quiet jupyter

# Cria diretórios de trabalho no container
RUN mkdir -p /workspace/data/raw \
  /workspace/data/processed \
  /workspace/notebooks \
  /workspace/src 

# Define o diretórios de trabalho padrão
WORKDIR /workspace

# Expõe a porta do Jupyter
EXPOSE 8888

# Comando padrão para iniciar o Jupyter Notebook
CMD ["jupyter", "notebook", "--notebook-dir=/workspace/notebooks", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]


