# 🧠 Projeto de Mestrado — Estrutura de Dados e Código

Este repositório contém toda a estrutura organizada para o desenvolvimento do projeto de mestrado, incluindo bases de dados, notebooks, scripts, resultados e documentação.

---

## 📂 Estrutura de Pastas

```
meu_projeto_mestrado/
│
├── data/
│   ├── raw/               # Bases originais (não alteradas)
│   ├── processed/         # Dados tratados / limpos
│   ├── external/          # Dados públicos de terceiros
│   └── interim/           # Arquivos temporários de pré-processamento
│
├── notebooks/
│   ├── exploracao.ipynb   # Análise exploratória (EDA)
│   ├── modelagem.ipynb    # Modelos e testes
│   └── resultados.ipynb   # Visualização e métricas
│
├── src/
│   ├── __init__.py
│   ├── data_preparation.py
│   ├── feature_engineering.py
│   ├── model_training.py
│   └── evaluation.py
│
├── reports/
│   ├── figures/           # Gráficos e imagens
│   ├── tables/            # Tabelas em CSV, LaTeX, etc.
│   └── paper/             # Rascunhos do artigo ou dissertação
│
├── environment.yml         # Lista de dependências (conda)
├── requirements.txt        # Lista de dependências (pip)
├── README.md               # Explica o objetivo e como rodar o projeto
└── .gitignore              # Ignora arquivos pesados e temporários
```

---

## 🧩 Descrição das Pastas

| Pasta | Descrição |
|:------|:-----------|
| **data/raw** | Dados originais, sem qualquer modificação. |
| **data/processed** | Dados limpos e transformados, prontos para análise. |
| **data/external** | Dados públicos ou de terceiros usados como apoio. |
| **data/interim** | Arquivos intermediários ou de pré-processamento. |
| **notebooks/** | Notebooks Jupyter para experimentos, análises e visualizações. |
| **src/** | Scripts e funções Python reutilizáveis. |
| **reports/** | Resultados, gráficos, tabelas e documentos do projeto. |

---

## ⚙️ Como Criar a Estrutura Automaticamente

No terminal Linux, execute:

```bash
mkdir -p meu_projeto_mestrado/{data/{raw,processed,external,interim},notebooks,src,reports/{figures,tables,paper}}
touch meu_projeto_mestrado/{README.md,requirements.txt,environment.yml,.gitignore}
```

---

## 🧠 Sugestão de Workflow

1. **Baixe ou colete os dados originais** em `data/raw/`.
2. **Crie notebooks** em `notebooks/` para explorar e testar hipóteses.
3. **Transforme códigos reutilizáveis** em funções dentro de `src/`.
4. **Salve resultados** (gráficos, tabelas) em `reports/`.
5. **Mantenha o ambiente atualizado** com:
   ```bash
   conda env export > environment.yml
   ```
6. **Use controle de versão (Git)** para rastrear suas mudanças e versões do projeto.

---

## 💾 Dependências

Se estiver usando **Conda**, instale as dependências com:

```bash
conda env create -f environment.yml
conda activate meu_projeto
```

Se preferir **pip**:

```bash
pip install -r requirements.txt
```

---

## 🧩 Boas Práticas

- Não edite os dados originais — mantenha-os sempre em `data/raw/`.
- Versione apenas os códigos e metadados, **não os datasets grandes**.
- Documente cada etapa no README ou em notebooks.
- Mantenha os nomes das pastas e arquivos em **inglês**, padronizados e descritivos.
- Faça backup regular (GitHub, GitLab, ou cloud).

---

✍️ **Autor:** *Seu Nome Aqui*  
🎓 **Instituição:** *Nome do Programa de Mestrado / Universidade*  
📅 **Início do projeto:** *mês/ano*
