---
Camada OSI: 6 - Apresentação
tags:
  - Protocolos
aliases:
  - SSL
  - Secure Sockets Layer
---
## Sobre
É um [[Protocolo de comunicação |protocolo]] de segurança de internet baseado em [[Criptografia]].
Sendo o ancestral do método de criptografia '[[TLS]]'

Sites que utilizam o **SSL/TLS** tem o `https` em sua URL em vez de **HTTP**.

Dessa forma, todo o tráfego entre cliente até servidor e vice-versa, ficam embaralhados com caracteres, que somente os dois pontos, tem o conhecimento de como descriptografar.
Pois, caso não houve esse embaralhamento do verdadeiro conteúdo sendo trafegado na rede, informações como 'nome, usuário, senha, número do cartão' seriam facilmente capturados, com o ataque denominado [[Main-In-The-Middle]].

## Certificado SSL
