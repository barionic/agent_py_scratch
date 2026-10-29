# Diário de Engenharia de Agentes

## Objetivo
Aprender engenharia de agentes de IA construindo um projeto em Python, com experimentos pequenos e compreensão das decisões.

## Histórico anterior
- As Missões 001–008 fazem parte da etapa inicial de aprendizagem, registrada originalmente nas conversas.
- O conteúdo detalhado dessas missões ainda não foi reconstruído e confirmado neste diário.
- O registro detalhado disponível neste documento começa na Missão 009.

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
- Criamos `FinishReason` com os estados `COMPLETED`, `LENGTH_LIMIT` e `UNKNOWN`.
- Criamos `GenerationResult`, agrupando o texto gerado e o motivo do encerramento.
- Atualizamos o contrato `LLMClient` para retornar `GenerationResult`.
- Adaptamos `FakeLLMClient` e `app.py`.
- Adaptamos `OpenRouterClient`, normalizando `finish_reason`.
- Adaptamos `OllamaClient`, normalizando `done_reason`.
- Testamos os três provedores: Fake, OpenRouter e Ollama.
- Observamos respostas interrompidas por limites de geração.
- Aprendemos que o encerramento técnico não garante que a resposta seja suficiente ou factualmente correta.
- Mantivemos os diagnósticos de experimentação comentados.

## Missão 020 — Integração com Ollama Cloud
- Criamos OllamaCloudClient em ollama_cloud_client.py.
- Configuramos o endpoint remoto https://ollama.com/api/chat.
- Configuramos a autenticação por OLLAMA_API_KEY, obtida do ambiente.
- Integramos o provedor ollama-cloud à seleção de clientes em main.py.
- Mantivemos o contrato LLMClient e o retorno GenerationResult.
- Consultamos /api/tags para identificar os modelos disponíveis no Cloud.
- Observamos HTTP 404 ao tentar usar qwen3.5:0.8b, que não constava na lista retornada.
- Observamos HTTP 402 ao tentar usar gpt-oss:20b, indicando exigência de pagamento.
- Testamos o modelo beam: uma resposta retornou LENGTH_LIMIT e outra retornou COMPLETED.
- Validamos a integração sem armazenar a chave no repositório.

## Missão 021 — Tratamento dos resultados da geração
- Atualizamos app.py para tratar os estados de encerramento da geração.
- Para COMPLETED, a resposta é exibida sem aviso adicional.
- Para LENGTH_LIMIT, a resposta é exibida com um aviso de possível interrupção.
- Para UNKNOWN, a resposta é exibida com um aviso sobre o motivo desconhecido.
- Tornamos FakeLLMClient configurável para simular diferentes estados.
- Criamos testes automatizados para os três estados usando unittest.
- Executamos os três testes e confirmamos que passaram.

### Aprendizados
- O limite de tokens continua sendo um parâmetro técnico, não uma meta de tamanho da resposta.
- A concisão e o aprofundamento sob demanda serão explorados numa etapa posterior.
- Modelos disponíveis localmente não estão necessariamente disponíveis no Ollama Cloud.
- A listagem de modelos não garante acesso gratuito à geração.
- O contrato comum permite adicionar outro provedor sem alterar a interface esperada pela aplicação.
- Os motivos de encerramento continuam sendo normalizados entre provedores.
- O encerramento técnico não garante que a resposta seja suficiente ou factualmente correta.

### Decisões pendentes
- Definir como configurar os limites de geração.
- Investigar como favorecer respostas que concluam unidades de sentido.
- Projetar uma estratégia de continuação para respostas interrompidas, evitando repetições e perda de contexto.

### Próximos passos
- Implementar um loop de conversa com histórico de mensagens.
- Investigar instruções de geração e limites adequados para favorecer respostas completas.
- Avançar na gestão de contexto e memória conforme o roadmap.

## Método de aprendizagem
1. Entender o problema e formular uma hipótese.
2. Fazer uma alteração pequena.
3. Executar um experimento.
4. Interpretar a evidência.
5. Registrar o aprendizado e só então avançar.