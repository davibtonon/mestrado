
## 1. Estrutura de Diretórios no Repositório GitHub

Para garantir uma organização clara e facilitar a integração entre o código, as decisões arquiteturais e os registros de pesquisa, propõe-se a seguinte estrutura de diretórios no repositório GitHub:

```
/seu-repositorio-mestrado
├── .github/              # Configurações do GitHub (workflows, templates de issues, etc.)
├── src/                  # Código-fonte do seu projeto (LLMs, LangChain, agentes)
│   ├── agents/
│   ├── models/
│   └── ...
├── docs/                 # Documentação geral do projeto
│   ├── adr/              # Architecture Decision Records (ADRs)
│   │   ├── 0001-nome-da-decisao.md
│   │   ├── 0002-outra-decisao.md
│   │   └── ...
│   ├── research-logs/    # Diários de Pesquisa (Research Logs)
│   │   ├── 2026-02-13-experimento-inicial-langchain.md
│   │   ├── 2026-02-14-ajuste-prompt-agente-seguranca.md
│   │   └── ...
│   ├── README.md         # README principal do projeto
│   └── ...
├── data/                 # Conjuntos de dados, logs de experimentos, etc.
├── notebooks/            # Jupyter notebooks para experimentação e análise
├── .gitignore
└── LICENSE
```

- **`/src`**: Contém todo o código-fonte do seu projeto. É onde os agentes, modelos de LLM e implementações com LangChain serão desenvolvidos.
- **`/docs`**: Este diretório centraliza toda a documentação. É aqui que os ADRs e os Research Logs serão armazenados.
    - **`/docs/adr`**: Dedicado aos **Architecture Decision Records**. Cada decisão arquitetural significativa (e.g., escolha de um LLM específico, estratégia de *prompting*, framework de agente) deve ter seu próprio arquivo Markdown, prefixado com um número sequencial para facilitar a ordenação e referência.
    - **`/docs/research-logs`**: Contém os **Diários de Pesquisa**. Cada entrada de diário pode ser um arquivo Markdown separado, nomeado com a data para fácil rastreabilidade. Isso permitirá registrar experimentos, observações, resultados e próximas etapas de forma cronológica.
- **`/data`**: Para armazenar dados brutos, conjuntos de dados de treinamento/teste, e logs de saída de experimentos.
- **`/notebooks`**: Para notebooks Jupyter ou outros ambientes interativos de experimentação.

## 2. Fluxo de Trabalho Integrado GitHub e Obsidian

O fluxo de trabalho proposto visa maximizar a eficiência e a rastreabilidade, aproveitando as capacidades do Obsidian para escrita e organização, e do GitHub para versionamento e colaboração (se aplicável).

1.  **Criação do Repositório GitHub**: Inicie seu projeto de mestrado criando um repositório no GitHub com a estrutura de diretórios sugerida.
2.  **Configuração do Obsidian Vault**: Crie um novo *vault* do Obsidian dentro do diretório raiz do seu repositório GitHub (`/seu-repositorio-mestrado`). Isso permitirá que o Obsidian gerencie os arquivos Markdown diretamente nos diretórios `/docs/adr` e `/docs/research-logs`.
3.  **Instalação do Plugin Obsidian Git**: Instale e configure o plugin `Obsidian Git` dentro do seu *vault* do Obsidian. Este plugin automatizará a sincronização das suas notas Markdown com o repositório GitHub. Configure-o para fazer *commits* e *pushes* automaticamente em intervalos regulares ou manualmente quando desejar.
4.  **Criação de ADRs**: 
    - Ao tomar uma decisão arquitetural significativa, crie um novo arquivo Markdown no diretório `/docs/adr` (e.g., `0003-escolha-modelo-llm.md`).
    - Utilize um template padronizado (a ser fornecido na próxima fase) para preencher o ADR com Título, Status, Contexto, Decisão e Consequências.
    - Escreva o ADR no Obsidian, aproveitando seus recursos de linkagem interna para referenciar outros ADRs, Research Logs ou seções do código.
5.  **Registro de Research Logs**: 
    - Para cada experimento, observação ou iteração de pesquisa, crie um novo arquivo Markdown no diretório `/docs/research-logs` (e.g., `2026-02-15-experimento-ajuste-hiperparametros.md`).
    - Utilize um template (a ser fornecido) para registrar a data, hipótese, experimento, resultados, reflexões e próximos passos.
    - Inclua links para o código-fonte relevante (`/src`) ou para os dados (`/data`) quando apropriado.
6.  **Versionamento com Git**: 
    - O plugin Obsidian Git cuidará da maioria dos *commits* e *pushes* para os arquivos Markdown.
    - Para alterações no código (`/src`) ou outros arquivos, utilize o fluxo de trabalho Git padrão (adicionar, *commit*, *push*).
    - **Importante**: Faça *commits* frequentes e com mensagens descritivas, vinculando as alterações de código aos ADRs ou Research Logs relevantes sempre que possível (e.g., "`feat: Implementa agente ReAct conforme ADR-0002`").
7.  **Revisão e Referência**: 
    - Durante o desenvolvimento, consulte os ADRs para relembrar as decisões tomadas e seus fundamentos.
    - Revise os Research Logs para entender o histórico de experimentos e evitar repetir erros.
    - Para a escrita da dissertação, estes documentos servirão como uma fonte rica e organizada de informações sobre o processo de pesquisa e desenvolvimento.

Este sistema garante que todas as decisões e experimentos sejam registrados de forma persistente e versionada, facilitando a rastreabilidade e a escrita final da sua dissertação de mestrado.
