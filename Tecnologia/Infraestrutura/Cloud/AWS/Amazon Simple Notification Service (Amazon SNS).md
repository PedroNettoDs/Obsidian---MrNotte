---
aliases:
  - Amazon Simple Notification Service
  - Amazon SNS
  - SNS
tags:
---
[[Amazon Web Services (AWS)|Amazon Web Services]]

O **Amazon Simple Notification Service (SNS)** é um serviço de publicação/assinatura. 
Com ele, um editor envia mensagens para vários assinantes. Isso funciona de forma parecida com um newletter: o servidor recebe as solicitações e distribui para os assinantes, que podem ser servidores, e-mails, funções do [[AWS Lambda]] ou outros destinos.

- **Publicação de atualizações de um único tópico**
    - Pegando o exemplo de Newletter ou jornais digitais, nessa categoria, todos os assinantes recebem todas as noticias publicadas pelo site.

- **Publicação de atualizações de vários tópicos**
    - Já nessa função, o assinante escolhe, quais noticias ele deseja receber, por exemplo; quero somente notificações sobre política ou cantores pop, assim então, só chegará pautas com esses assuntos.