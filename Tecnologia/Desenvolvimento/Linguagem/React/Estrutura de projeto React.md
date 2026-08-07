## Estrutura mínima de arquivos (boa prática)
[[React|React]]

Dentro do `frontend/src/`:
```css
src/
  api/
    client.js
    auth.js
  routes/
    AppRoutes.jsx
    ProtectedRoute.jsx
  pages/
    Login.jsx
    Home.jsx
    Treinos.jsx
    Foco.jsx
  App.jsx
  main.jsx

```

#### **src**
Abreviação de: *Source*, serve para todos os arquivos necessários para o sistema.
Sendo possível assim colocar dentro dele: 
- [^1]**Componentes**
- [[Hooks]]
- Contextos
- Páginas
- Serviços
- APIs
- Assets
- Estilos
- Utilitários

[^1]: ![[Componentes]]
