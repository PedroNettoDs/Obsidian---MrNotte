---
tags:
  - Linguagem
---
é um **Conceito** de um intérprete de comandos que oferece uma [[Linha de comando|Command Line Interface]] para interagir com o [[Sistema Operacional]] [[Linux]].

Sendo também considerado uma Linguagem de programação

Traduzindo os comandos digitados pelo usuário (como `ls`, `cd`, `mkdir`) em ações para o [[Kernel]].

---

Há métodos de Shell, entre eles: 
-  [[Zsh]]
-  [[Bash]]
- [[sh]]
Para descobrir qual é o tipo de shell:
`echo $SHELL`

---
### `$?`
é uma **variável especial**, que guarda o *código de retorno ([[exit code]])* do último comando executado
![[Descritores de arquivo]]

Ou por exemplo:

| Comando                        | Exit Code | Significa                |
| ------------------------------ | --------- | ------------------------ |
| `ls` - em arquivo que existe   | `0`       | Sucesso                  |
| `grep` - que não encontra nada | `1`       | "Não achei o padrão"     |
| Comando não existe             | `127`     | "Comando não encontrado" |
| `exit 42` (forçado)            | 42        |                          |

---
### `$(( $i + 1 ))`
- `$(( ... ))`
	Diz ao [[Bash]] 'calcule isso'.
- `$i`
	Pega o valor atual da variável
- `+ 1`
	Soma 1 a esse valor