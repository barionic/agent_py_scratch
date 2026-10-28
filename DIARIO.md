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

## Missão 019 — Representação do resultado da geração

- Criamos `FinishReason` com os estados `COMPLETED`,
  `LENGTH_LIMIT` e `UNKNOWN`.
- Criamos `GenerationResult`, agrupando o texto gerado
  e o motivo do encerramento.
- Atualizamos o contrato `LLMClient` para retornar
  `GenerationResult`.
- Adaptamos `FakeLLMClient` e `app.py`.
- Adaptamos `OpenRouterClient`, normalizando `finish_reason`.
- Adaptamos `OllamaClient`, normalizando `done_reason`.
- Testamos os três provedores: Fake, OpenRouter e Ollama.
- Observamos respostas interrompidas por limites de geração.
- Aprendemos que o encerramento técnico não garante
  que a resposta seja suficiente ou factualmente correta.
- Mantivemos os diagnósticos de experimentação comentados.

### Aprendizados e decisões pendentes

- O limite de tokens continua sendo um parâmetro técnico,
  não uma meta de tamanho da resposta.
- Ainda precisamos definir como configurar limites e lidar
  com respostas interrompidas.
- A concisão e o aprofundamento sob demanda serão explorados
  numa etapa posterior.

### Próximos passos

- Revisar a implementação e o estado do Git.
- Confirmar os arquivos finais e os testes.
- Atualizar este diário e fechar a missão com um commit.
- Depois, retomar a evolução do comportamento do agente,
  incluindo instruções, identidade e personalidade.
- Investigar a integração com Ollama Cloud numa etapa futura.

## Método de aprendizagem
1. Entender o problema e formular uma hipótese.
2. Fazer uma alteração pequena.
3. Executar um experimento.
4. Interpretar a evidência.
5. Registrar o aprendizado e só então avançar.
