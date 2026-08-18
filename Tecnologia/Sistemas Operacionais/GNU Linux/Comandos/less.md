No [[Linux]]/[[Unix]], o comando `less`, é um '[[pager]] aprimorado'.
Criado para resolver a incapacidade do [[more]] de voltar para trás.
Seu nome é um trocadilho, pois é o inverso de `more`.
- **Navegação Bidirecional**
	Oferece movimentação para frente e para trás, usando teclas: 
	- `b` (voltar página)
	- `u` (subir meia tela)
	- `j` (descer linha)
	- `k` (subir linha)
	- `g` (ir ao inicio)
	- 'Shift + G' (ir ao final)
- **Carregamento dinâmico**
	Ao contrário do `more`, o `less` não lê o arquivo inteiro para exibi-lo, *ele carrega apenas a porção visível*, garantindo a abertura instantânea mesmo para arquivos pesados.
- **Eficiência**
	Esse carregamento dinâmico trás consigo um menor consumo de memória RAM.
---
Outras implementações do **less**, seriam os módulos de '**busca avançada**', utilizando:
- `/busca` - para buscar à frente
- `?busca` - para buscar para trás
---
A utilização de `less` é comum para [[Pipelines]] (`|`)
