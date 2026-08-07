O comando do ecossistemas [[Linux]]/[[Unix]];
São utilizados para ler apenas uma **fração inicial** de um arquivo.
Por padrão exibindo somente 10 linhas (Por isso se chama 'Head').

- **Utilidade**:
	Usada para identificar 'versões'/'cabeçalhos' localizados no começo de um arquivo, sem necessidade de carregar o arquivo inteiro na memória.
---
#### Opções de exibição:
- `-n`: **Número de Linhas**
	Permite ditar a quantidade de linhas mostradas.
	*Exemplo*: `head -n 20`, exibindo as 20 primeiras linhas.
- `-c`: **Contagem por Bytes**
	Em vez de linhas, o usuário pode solicitar a exibição dos primeiros N bytes de um arquivo.