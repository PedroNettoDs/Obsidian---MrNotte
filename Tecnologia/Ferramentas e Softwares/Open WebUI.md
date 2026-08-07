O Open WebUI é essencialmente um **frontend de chat**: ele não é o agente, não executa código, não tem memória própria. Ele é a janela pela qual você conversa com o Ollama. 
Pensa nele como o "rosto" do Alfred, enquanto o Ollama é o cérebro.

O que ele oferece nativamente que é útil pro seu projeto:

**Interface** — histórico de conversas, múltiplos chats, suporte a markdown, syntax highlight em código. Tudo que você já usa no ChatGPT, mas local.

**Tools** — o Open WebUI tem um sistema de Tools em Python. Você escreve uma função, ele expõe pro modelo como ferramenta chamável. Foi assim que você criou o web scraper antes. Esse é o ponto de extensão principal.

**Knowledge Base** — [[RAG - Retrieval-Augmented Generation]] nativo. Você sobe documentos e ele indexa. Mais simples que o Flowise, mas menos flexível.

**Pipelines** — um sistema de middleware que intercepta mensagens antes de chegarem ao modelo. Dá pra injetar contexto, chamar APIs externas, filtrar output.

**Model System Prompts** — você pode criar um "modelo" chamado Alfred com o soul prompt fixo, sem precisar redigitar toda vez.

---