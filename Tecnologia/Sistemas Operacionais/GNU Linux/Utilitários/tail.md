Um comando do [[Linux]]/[[Unix]];
São utilizados para ler uma **fração final** de um arquivo.
Por padrão exibindo somente **10 linhas do final** (por isso 'Calda').

- **Utilidade**:
	Usada para identificar 'novos registros', localizados no fim de um arquivo, sem necessidade de carregar o arquivo inteiro na memória.
---
### Opções de exibição:
- `-n` : **Número de Linhas**
	Permite ditar a quantidade de linhas a serem mostradas.
- `-n +x`: **Porto de Partida Específico** :
	Função com a capacidade de começar a leitura a partir de uma linha específica, exemplo: `tail -n +15` (começará na linha 15)
- `-c`: **Contagem por Bytes**  
	Em vez de linhas, o usuário pode solicitar a exibição dos primeiros N bytes de um arquivo.
- `-r`: **Inversão**
	Não entendi, muito bem o uso, está sendo descrito como: 'da mais recente, para a mais antiga' (Mas já não deveria ser assim?)
- `-f` e `-F`: **Monitoramento em tempo real**
	- `-f`: **Follow** (Minusculo)
		- Serve para acompanhar atualizações no arquivo, por exemplo, em um arquivo de LOG, que sempre tem atualizaçõees,
	- `-F`: **Follow** (Maiúsculo)
		- Serve assim como o minusculo, para acompanhar atualizações, porém ele 'fixa' no alvo, mesmo se ele alterar de nome/localização ou for recriado., não importa, persiste vendo as atualizações.
- `-q`: **Suspensão de Cabeçalhos**
	Quando executado o comando `tail`, com dois arquivos ou mais, ele insere automaticamente um cabeçalho com o nome de cada arquivo.
- `-v`: **Verbose**
	Mostra mais informações sobre o arquivo 'tailzado'