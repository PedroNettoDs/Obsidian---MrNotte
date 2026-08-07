---
aliases:
  - Secure Shell
tags:
  - Protocolos
Camada OSI: 7 - Aplicação
porta: 22
---
O SSH é um [[Protocolo de comunicação]] que permite o acesso a outro computador, garantindo a segurança durante essa comunicação.

Comumente utiliza a [[Porta 22]] ([[TCP]])

Existindo também '[[Chaves SSH]]' para garantir a comunicação segura

https://medium.com/@e_moreira/fundamentos-do-ssh-arquitetura-seguran%C3%A7a-e-implementa%C3%A7%C3%A3o-avan%C3%A7ada-a3d43efa0b97

---
### Criar a chave SSH
```
ssh-keygen
```
1. Questionará o nome da chave
2. Questionará a senha da chave
**obs**: criará dois arquivos no [[Path]] que você estiver

---
### Copiar a chave SSH
```
ssh-copy-id -i <nome da chave>.pub <caminho que será copiado>
```
**obs:** o parâmetro `-i` é para especificar o nome do arquivo;
**<caminho que será copiado>,** você utiliza o SSH de algum local, exemplo: *netto@192.168.0.1*


