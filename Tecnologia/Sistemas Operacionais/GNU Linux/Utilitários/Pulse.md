---
aliases:
  - PulseAudio
---
**[PulseAudio](https://www.google.com/search?client=firefox-b-d&channel=entpr&q=PulseAudio&mstk=AUtExfDQ9LYlEVlmh21PCwdBZzrIFhEtMQMrQCGXZXJnMuyNfmngqFUsZ6tdgragOQK7blzkuehRY2x9Ldq8Fl-pMJx5WgaNaz0v1gE0q7mjmAreMCxyfVziVCB1ahr5Fvskrr41tVSjhOoPPmwLLYL9RmGHFOghccguWiVKF4VA8SBUsLc&csui=3&ved=2ahUKEwjI9ICNjOuRAxXVIbkGHWKlBwIQgK4QegQIARAC)**, um servidor de som que atua como um intermediário ([[middleware]]) entre seus aplicativos e o [[Hardware]] de áudio

**Funções Principais do PulseAudio:**

- **Gerenciamento de Áudio:** Mixa sons de vários aplicativos, permitindo controlar o volume de cada um individualmente.
- **Intermediário (Middleware):** Conecta os aplicativos ao hardware de áudio (ALSA), oferecendo mais controle do que o ALSA sozinho.
- **Streaming de Rede:** Permite enviar áudio de um computador para outro na rede.
- **Configurações Avançadas:** Oferece recursos como mudança de formato de áudio e contagem de canais. 

**Contexto Atual (PipeWire):**

- O **[[PipeWire]]** é um sucessor que visa unificar o gerenciamento de áudio e vídeo, sendo compatível com PulseAudio e JACK, e está se tornando o novo padrão em distribuições como Fedora e [[Ubuntu]]. 

**Em Resumo:** Se você ouve falar de "Pulse" no [[Linux]], pense em **PulseAudio**, o sistema que gerencia seu som do dia a dia, embora o **PipeWire** seja a tecnologia mais recente que está assumindo essa função