# mestrado

## 📁 Estrutura do Projeto

```text
├── data/                # Bases de dados (raw, processed, etc.)
├── docs/                # Documentação adicional do projeto
├── notebooks/           # Jupyter Notebooks para análise e experimentos
│   └───atomic           # Notebooks copiados Security-Datasets
│   └───compound         # Notebooks copiados Security-Datasets
├── src/                 # Código-fonte principal do projeto
├── .gitignore           # Arquivos e pastas ignorados pelo Git
├── docker-compose.yml   # Orquestração de containers Docker
├── Dockerfile           # Definição da imagem Docker do projeto
├── example.env          # Modelo de variáveis de ambiente
├── mise.toml            # Configuração do gerenciador de ferramentas (não estou usando)
├── pyproject.toml       # Configuração de dependências e build (Python)
├── README.md            # Documentação principal (este arquivo)
└── uv.lock              # Arquivo de trava de dependências (gerado pelo uv)
``` 

# Como Iniciar

- Instalar UV
- uv venv
- uv sync

Caso deseje ver os notebooks do Security-Datasets
```
uv run jupyter lab
```


# Testes com 3 logs diferentes

Selecioneis três arquivos diferentes com para os testes. O conjuntos de dados simula ambiente real e cada um vez com a respectivas TTP's utilizadas, o que ajuda a testa os modelos.

Mudei os nomes dos arquivos originais por uma questão de facilidade:

- ec2_proxy_s3_exfiltration_2020-09-14011940 -> file_01.json 
- sh_binary_padding_dd_2020-11-10081941.log  -> file_02.log
- AWS_S3_HoneyBucketLogs.csv -> file_03.json

 ## Privillege_escalation - file_01.json

Táticas e tecnicas:

- Tactics:	TA0001,TA0003,TA0004,TA0005,TA0009
- Techniques: T1078.004,T1530


Ollama resultados:
- Tactics:
- Techniques:

Gemini resultado:

- Tactics:
- Techniques:

## Teste 02 - Defesen Evasion - file_02.log

- Tactics: TA0005
- Techniques: T1027.001

Ollama resultados:
- Tactics:
- Techniques:


Gemini resultado:

- Tactics:
- Techniques:


## Teste 03 - Discovery - file_03.csv

- Tactics: TA0007
- Techniques: T1580

Ollama resultados:
- Tactics:
- Techniques:


Gemini resultado:

- Tactics:
- Techniques:


## Notebooks originais

 [AWS Privellege Escalation](./notebooks/atomic/aws/privilege_escalation/SDAWS-200914011940.ipynb)  
 [Linux Defense Evasion](./notebooks/atomic/linux/defense_evasion/SDLIN-201110081941.ipynb)  
 [AWS Discovery](./notebooks/atomic/aws/discovery/SDAWS-2202181000.ipynb)  
 
 