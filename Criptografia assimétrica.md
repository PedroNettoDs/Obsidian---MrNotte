## Sobre
Seguindo o conceito da [[Criptografia]], a forma assimétrica ou também conhecida como '*criptografia de chave pública*', vem para resolver o problema: 
"*Como enviar uma mensagem segura para alguém se vocês nunca se encontraram antes para combinar uma senha?*"

Mas por que o chamam de **Assimétrica**?
![[Exemplo assimétrica.png | 450]]

Como demonstrado na imagem, algo Assimétrico, é algo que não possui os dois lados idênticos, isso está presente no par de **CHAVES** que essa criptografia utiliza, sendo uma chave **Pública** e outra **Privada**.

### Chave Pública (Criptografar)
Essa chave é 'distribuída abertamente' e é usada para criptografar e verificar assinaturas digitais.

### Chave Privada (Descriptografar)
Mantida em segredo absoluto, pois é utilizada para descriptografar dados ou assinaturas digitais.

#### Matemática
O sistema é projetado para que seja 'computacionalmente inviável' tentar achar o divisor privado a partir da pública

---
## Geração das chaves
Com seu algoritmo a partir de uma chave pública, fica muito trabalhoso conhecer qual a chave privada que a gerou, por isso, a pública pode ser distribuída.

![[Criptografia assimétrica-1.png]]

Vamos imaginar, que nossa chave pública, entre todos os números que pode ser, seja o número 10.
Sabendo que a chave privada é um 'divisor' desses possíveis números, logo podemos tentar como chave privada os números: 2 ou 5
Claro, que na realidade, os números da chave pública são grandes e aleatórios, ficando difícil saber qual é o número divisor da chave privada correta. 

#### Troca de chaves
Os algoritmos assimétricos, são mais lentos, por conta dessa etapa de checagem da chaves, mas são utilizados pela sua segurança em protocolos como [[PGP]], [[SSH]] e [[SSL]]/[[TLS]].

Vamos imaginar que duas pessoas, Alice e Bob gerem seus pares de chaves público e privado, para fecharmos uma conexão confiável entre eles, cada um concede sua chave pública, dessa forma, se a Alice quiser conectar ao Bob, ela usará a chave pública gerada por ele, pois na máquina dele, ele tem o divisor correto.
Vamos supor que um hacker, tente conectar no mesmo caminho que Alice na máquina de Bob

![[Criptografia assimétrica-2.png]]

https://www.ibm.com/br-pt/think/topics/asymmetric-encryption

https://medium.com/@shadowfeit60/criptografia-assim%C3%A9trica-88ecdf761aac