---
aliases:
  - Env
---
Para um projeto em produção, não podemos deixar as senhas visíveis ao mundo, para isso existe a pasta ou arquivo:  **`.env`**  

O Env, é como se fosse a carteira que você pode colocar na carteira

Usado para armazenar variáveis de ambiente (configurações, chaves de API, segredos) de uma aplicação, separando-as do código-fonte para segurança e portabilidade, e sendo carregado por bibliotecas como `dotenv` em linguagens como [[Node.js]], [[Python]], [[PHP]], etc., permitindo configurar diferentes ambientes (desenvolvimento, produção) sem alterar o código. 

Para que serve

- **Armazenar informações sensíveis:** Chaves de [[API - Interface de Programação de Aplicações]], senhas de banco de dados, tokens, etc., que não devem ser expostos no repositório de código (GitHub, etc.).
  
- **Configurar diferentes ambientes:** Permite ter configurações distintas para desenvolvimento (ex: banco de dados local) e produção (ex: banco de dados em nuvem).
  
- **Facilitar o desenvolvimento:** Co-desenvolvedores podem ter suas próprias configurações locais sem afetar o projeto principal. 

Como funciona

1. **Formato:** O arquivo contém pares `CHAVE=VALOR`.
   
2. **Leitura:** Uma biblioteca (ex: `dotenv` para Node.js/Python) lê o arquivo e injeta essas variáveis no ambiente do processo da aplicação (`process.env` no Node.js).
   
3. **Uso no código:** No código, você acessa a variável (ex: `process.env.API_KEY`).
   
4. **Segurança:** O arquivo `.env` **não deve** ser commitado em sistemas de controle de versão, sendo adicionado ao `.gitignore`.