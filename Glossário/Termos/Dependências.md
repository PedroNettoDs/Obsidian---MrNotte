---
aliases:
  - dependência
---
### Nota:
Bom, não sei exatamente o que escrever sobre 'dependência' que não seja propriamente dito, porém podemos descrever como: *não consigo viver sem oxigênio*

Ou seja, é algo que precisa existir para que outra viva.

Podemos levar isso para o sentido mais filosófico, sobre o que é existir, mas vamos deixar somente com isso, tá bom né?

---
Em 'Desenvolvimento', 'Instalações' e afins, a dependência pode ser por exemplo:
*Baixei um script em Python, para rodar, eu preciso do Python na minha máquina, além do Python em minha máquina, o script utiliza um código de uma biblioteca X, logo preciso instalar essa biblioteca*

Agora, se você não sabe o que é uma [[Biblioteca]], irmão? WTF.

---

Estive em dúvida de como funciona o lance de instalar dependências no [[Linux]] a cada [[apt - Advanced Package Tool|apt]] instalado, pesquisando, compreendi que, caso instalemos vários programas, eles sempre precisaram de sua dependência (ava?)

- Mas e se dois programas diferentes puxarem a mesma dependência?
R: Ele vai ver que já tem instalado e não prosseguirá

- Mas e se for versões diferentes da mesma dependência?
R: o apt ira pontuar, tentando substituir pela versão mais nova.

- Há como possuir duas versões simultaneamente da mesma dependência?
R: