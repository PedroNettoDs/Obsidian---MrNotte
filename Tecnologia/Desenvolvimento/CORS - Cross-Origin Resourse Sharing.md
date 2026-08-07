Para permitir que o [[Django]] responda corretamente a requisições vindas de outros domínios

---
Por padrão, **navegadores bloqueiam** requisições feitas por um site para outro domínio diferente, por segurança.

Exemplo clássico:

- Frontend em: `http://localhost:3000` ([[React]], [[Vue]], etc.)
- Backend em: `http://localhost:8000` ([[Django]] API)

Mesmo sendo “seu” projeto, **o navegador considera domínios diferentes** → bloqueia a requisição ❌

---
## O que o `CorsMiddleware` faz?

O `corsheaders.middleware.CorsMiddleware`:

- Intercepta a requisição
- Adiciona **headers HTTP de CORS** na resposta
- Diz ao navegador:  
    👉 _“essa origem pode acessar minha API”_
    
Sem isso, você verá erros como:
```http
Access to fetch at 'http://localhost:8000/api/'
from origin 'http://localhost:3000'
has been blocked by CORS policy
```
----
## Por que ele precisa estar no [[middleware]]?

Porque **CORS é tratado no nível HTTP**, antes da view ser executada.

O middleware:

- Roda no início do ciclo da requisição
    
- Lida com:
    - `OPTIONS` (preflight)
    - Headers como:
        - `Access-Control-Allow-Origin`
        - `Access-Control-Allow-Methods`
        - `Access-Control-Allow-Headers`

Sem middleware → [[Django]] **nem chega a responder corretamente** para o navegador.