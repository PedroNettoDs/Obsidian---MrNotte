Podemos imaginar um site recebendo muito tráfego e fazendo diversas solicitações ao mesmo tempo. Sem uma fila, cada solicitação teria que ser processada imediatamente, o que causaria sobrecarga ao sistema. O **Amazon SQS** é a solução que gera esse enfileiramento.

Os pedidos ficam armazenados até poderem ser processados. Assim, não sobrecarrega as instâncias e as solicitações não se perdem e são processadas quando possível. Isso é chamado de **acoplamento fraco**, evitando falhas no sistema.

O **SQS** armazena as solicitações entre componentes, e o **Amazon SNS** envia notificações para os destinatários, como notificações push, SMS ou e-mails.

- **Amazon Simple Notification Service (SNS)**: Envia notificações para vários destinatários ao mesmo tempo
- **Amazon Simple Queue Service (SQS)**: Armazena e gerencia mensagens entre os componentes de forma confiável

![[Amazon Simple Notification Service (Amazon SNS)]]

![[Amazon Simple Queue Service (SQS)]]

