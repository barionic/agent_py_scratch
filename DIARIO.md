# Diário de Engenharia de Agentes

## Objetivo
Aprender engenharia de agentes de IA construindo um projeto
em Python, com experimentos pequenos e compreensão das decisões.

## Missão 009 — Cliente Ollama
- Estudamos HTTP, JSON, urllib, type hints e return vs print.
- Identificamos limitações da implementação inicial.

## Missão 010 — Separação de responsabilidades
- Separamos a comunicação com o modelo da lógica da aplicação.

## Missão 011 — Ponto de entrada
- Centralizamos a execução em main.py.

## Missão 012 — Configuração do modelo e provedor
- Exploramos a separação entre escolher o modelo e escolher
  como acessá-lo.

## Missão 013 — Contrato LLMClient
- Introduzimos Protocol para definir o contrato dos clientes.

## Missão 014 — Cliente simulado
- Criamos FakeLLMClient para testar sem depender de uma API.

## Missão 015 — Organização da aplicação
- Extraímos a lógica da aplicação para app.py.
- main.py passou a montar as dependências.

## Missão 016 — Seleção do provedor
- Introduzimos LLM_PROVIDER.

## Missão 017 — Seleção do modelo
- Introduzimos LLM_MODEL e a configuração do modelo no cliente.

## Missão 018 — Integração com OpenRouter
- Criamos OpenRouterClient usando urllib.
- Configuramos a chave por OPENROUTER_API_KEY.
- Testamos FakeLLMClient e OpenRouterClient.
- Investigamos respostas com content=None.
- Adicionamos tratamento explícito para respostas sem texto.
- Commit: c7e25a5 — feat: add OpenRouter LLM client

## Próxima missão
019 — Investigar como separar as instruções e a identidade
do agente em arquivos Markdown e carregá-las na aplicação.

## Método de aprendizagem
1. Entender o problema e formular uma hipótese.
2. Fazer uma alteração pequena.
3. Executar um experimento.
4. Interpretar a evidência.
5. Registrar o aprendizado e só então avançar.
