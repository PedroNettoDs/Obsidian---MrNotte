---
aliases:
  - Lambda
---
Executor de códigos da [[Amazon Web Services (AWS)|AWS]]

Diferente do EC2, no Lambda serve para alocar '**códigos, programas e executáveis**', vamos supor, você precisa rodar um script de rotina, você aloca no Lambda e através de um comando, executa ele.

Quanto ao custo, ele só cobrará o tempo em que o código permaneceu em execução.

1. Você faz upload do código para o Lambda
2. Configura o código para ser acionado pelos eventos de uma origem como serviços da AWS, aplicações móveis ou [[Endpoint]] HTTP
3. O Lambda executa o código somente quando acionado
4. Você paga apenas pelo tempo da execução.