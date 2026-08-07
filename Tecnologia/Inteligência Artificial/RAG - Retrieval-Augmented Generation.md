---
aliases:
  - Retrieval-Augmented Generation
  - RAG
---
### Sobre
Denominadas como tecnologia **Geração Aumentada por Recuperação**.

Pois combina o poder de processamento e de criatividade dos modelos de linguagem ([[LLM]]).

Pois ele conta com 'sistema de recuperação de informação em tempo real'.
Diferente de uma IA isolada, o **RAG** permite que a IA **consulte bases de dados externas**, antes de gerar respostas.

---
### Motivo
O [[LLM]] tradicionalmente possuem limitações, como '*amnésia*' e '*corte de conhecimento*', pois são feitos com dados estáticos e generalistas que podem estar desatualizados, dessa forma o RAG vem para mitigar:

 - **Alunicações**: Reduz a chances do modelo inventar informações, pois força-o a analisar os dados.
 - **Falta de Contexto Privado**: Permite que a IA acesse documentos internos de uma empresa, que não possam ser 'mandados para uma BigTech' (LGPD ai!)
 - **Custo de Retreinamento**: É uma alternativa muito mais barata e rápida que o 'fine-tuning', pois podemos atualizar o conhecimento da IA, apenas inserindo novos dados, sem necessidade de processamento computacional pesado.
---
### Pipeline Técnico do RAG
