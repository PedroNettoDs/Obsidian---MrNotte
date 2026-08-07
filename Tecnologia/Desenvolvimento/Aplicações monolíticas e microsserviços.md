## **Aplicação monolítica**
Tudo funciona em um 'único bloco'
[[FrontEnd]], [[BackEnd]], Banco de dados e outros componentes conectados no sistema 'tudo em um'

Isso é denominado como **[[acoplamento forte]]**, esses componentes estão fortemente interligados, formando uma aplicação **monolítica**.

Nesse tipo de arquitetura, se um componente falhar, isso pode causar a falha de outros e até derrubar toda a aplicação.

> **Para manter a disponibilidade da aplicação quando um único componente falha, você pode projetar essa aplicação com uma abordagem de   
> microsserviços.  

---
## **Microsserviços**
Na abordagem de **microsserviços**, os componentes da aplicação ficam separados e independentes, assim denominado como **[[Acoplamento fraco]]**.

Se um serviço falhar, os demais continuam funcionando. Isso torna o sistema mais resiliente e mais fácil de escalar.

---
## Resumindo

- **Monolítico**: tudo junto e fortemente conectado. Se uma parte quebra, pode afetar tudo.
    
- **Microsserviços**: tudo separado e independente. Se uma parte quebra, o resto continua funcionando.