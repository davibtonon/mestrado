
---
title: "ADR [Número Sequencial]: [Título da Decisão]"
date: "YYYY-MM-DD"
authors: ["Seu Nome", "Manus AI"]
status: "Proposto" # Proposto, Aceito, Superado, Rejeitado
tags: ["arquitetura", "LLM", "LangChain", "segurança", "agentes"]
---

# ADR [Número Sequencial]: [Título da Decisão]

## 1. Status

[Status da decisão: Proposto, Aceito, Superado, Rejeitado. Inclua a data da última atualização e, se superado, o ADR que o substituiu.]

## 2. Contexto

[Descreva o problema ou a força motriz que levou a esta decisão. Qual é o desafio técnico ou de pesquisa que precisa ser resolvido? Quais são os requisitos funcionais e não funcionais relevantes? Inclua informações sobre o domínio de Segurança da Informação, o uso de LLMs, LangChain ou agentes.]

*Exemplo: "Estamos desenvolvendo um agente de segurança baseado em LLM para detectar ataques de injeção de prompt. A escolha do modelo de linguagem é crucial para a eficácia e o custo. Modelos open-source como Llama 2 oferecem flexibilidade, mas podem ter desempenho inferior a modelos proprietários como GPT-4 em tarefas complexas de raciocínio e segurança."*

## 3. Decisão

[Descreva a decisão tomada. Qual foi a solução escolhida? Seja específico sobre as tecnologias, abordagens ou configurações. Justifique a escolha em relação às alternativas consideradas.]

*Exemplo: "Decidimos utilizar o modelo `gpt-3.5-turbo` da OpenAI para a fase inicial de prototipagem do agente de detecção de injeção de prompt. Embora seja um modelo proprietário, ele oferece um bom equilíbrio entre desempenho, custo e facilidade de integração via API. Isso nos permitirá validar rapidamente a arquitetura do agente antes de explorar otimizações com modelos open-source."*

## 4. Alternativas Consideradas

[Liste e descreva brevemente as alternativas que foram avaliadas, mas não escolhidas. Explique os motivos pelos quais foram descartadas.]

*Exemplo:
- **Llama 2 (Open-source)**: Considerado pela flexibilidade e controle total, mas descartado devido à complexidade de hospedagem e ajuste fino inicial, o que atrasaria a validação da prova de conceito.
- **Bard/Gemini (Google)**: Avaliado, mas a API e as ferramentas de integração com LangChain eram menos maduras no momento da decisão em comparação com a OpenAI.
- **Abordagem baseada em regras (Regex)**: Descartada por ser menos flexível e escalável para detectar variações complexas de injeção de prompt em comparação com a capacidade de raciocínio de um LLM."*

## 5. Consequências

[Descreva as implicações da decisão. Quais são os pontos positivos (benefícios) e negativos (custos, riscos, compromissos) resultantes desta escolha? Como isso afeta o projeto, a equipe, o cronograma e a pesquisa de mestrado?]

*Exemplo:
- **Positivas**: Rápida prototipagem e validação da arquitetura do agente; acesso a um modelo de alta performance para detecção de ameaças complexas; vasta documentação e suporte da comunidade LangChain para integração com OpenAI.
- **Negativas**: Dependência de um provedor externo (OpenAI); custos associados ao uso da API; potencial dificuldade em reproduzir resultados exatos em um ambiente totalmente controlado para a dissertação, caso a política de uso do modelo mude; preocupações com privacidade de dados sensíveis (mitigadas pelo uso de dados sintéticos ou anonimizados para testes iniciais).
- **Próximos Passos**: Monitorar o desempenho e os custos do `gpt-3.5-turbo`; planejar a transição para um modelo open-source ajustado (`fine-tuned`) em uma fase posterior, se necessário, para garantir maior controle e reprodutibilidade."*

## 6. Referências

[Liste quaisquer documentos, artigos, discussões ou outras fontes que foram consultadas para tomar esta decisão.]

- [Link para documentação do modelo GPT-3.5 Turbo](https://platform.openai.com/docs/models/gpt-3-5)
- [Artigo sobre injeção de prompt em LLMs](https://arxiv.org/abs/2302.05737)
