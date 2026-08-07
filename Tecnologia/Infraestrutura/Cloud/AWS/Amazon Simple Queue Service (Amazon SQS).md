---
aliases:
  - Amazon Simple Queue Service
  - Amazon SQS
  - SQS
tags:
---
[[Queue]] da [[Amazon Web Services (AWS)|Amazon Web Services]] 

Usando nosso poder de imaginação, visualize você no supermercado, é dia de pagamento e só tem um operador disponível (calma, respira), em fim, todos os outros consumidores estão com seus produtos e precisam processar eles para saber quanto vão pagar.

Para poder garantir o fluxo fluindo, existe justamente uma 'fila';
Sem essa fila, cada solicitação teria que ser processada ao mesmo tempo o que causaria uma sobrecarregando o sistema.

Portanto o **Amazon SQS** é esse enfileiramento.

Onde os pedidos ficam armazenados até poderem ser processados. 
Assim, não sobrecarregado as instâncias e as solicitações não se perdem e são processadas quando possível.
Isso é chamado de **[[Acoplamento fraco]]**, evitando falhas no sistema.

Assim o **SQS** armazena as solicitações entre componentes, e o **[[Amazon Simple Notification Service (Amazon SNS)]]**, envia notificações para os destinatários, como notificações push, SMS ou e-mails.

- **Amazon Simple Notification Service (SNS)**: envia notificações para vários destinatários ao mesmo tempo.

- **Amazon Simple Queue Service (SQS)**: armazena e gerencia mensagens entre os componentes de forma confiável.