---
aliases:
  - wc
  - Word Count
---
**wc** = **W**ord **C**ount = Contagem de palavras
Para ver estatísticas como '**números de linhas, palavras e bytes**', de um arquivo há o comando `wc`

Que pode trazer informações de até 3 arquivos ao mesmo tempo e no final somar.

Exemplo:
```bash
wc /etc/passwd /etc/passwd-
  35   56 1710 /etc/passwd
  34   55 1665 /etc/passwd-
  69  111 3375 total
```
A saída do exemplo anterior possui quatro colunas:
1. Número de linhas (`-l`)
2. Número de palavras (`-w`)
3. Número de bytes (`-c`)
4. Nome do arquivo

Como pode ver, as três linhas, possuem um parâmetro na frente.
Resumindo, ao rodar o comando `wc`, você pode escolher o que quer exibir:
```bash
ls /etc/ | wc -l
142
```
Nesse caso, só exibiu o números de linhas.