---
tags:
dg-home: true
---
Com o fracasso do [[Tecla de atalho -  Menu contexto - 'MSI GK20']], seguiremos com um plano mais pé no chão.

como utilizo o [[KDE Plasma]], ele possui em configurações a aba 'Atalhos':
![[Tecla de atalho - Menu contexto-1.png]]
Então, prosseguimos para: 
- Abra **Configurações do Sistema → Atalhos → Atalhos Personalizados**
- Clique em **Editar → Novo → Atalho Global → Comando/URL**
Na aba **Ação**, coloque:
```
xdotool key Menu
```
>Claro, precisa que esteja instalado o [[xdotool]], que é uma ferramenta que simula ações de teclado e mouse

E após clicar em 'Aplicar', estará funcional sua tecla de atalho.