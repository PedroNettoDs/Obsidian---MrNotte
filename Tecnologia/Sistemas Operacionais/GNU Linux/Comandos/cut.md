O comando `cut` é usado para **extrair colunas de texto** de um arquivo ou da **entrada**.

Como pontuado: '**colunas**', então sabemos que ele é usado para trabalhar com [[Banco de dados]] ou até mesmo por **[[Sorting#^bed6af|delimitadores]]**.

Por padrão, o comando `cut` espera que a entrada seja por um **[^1]caractere de tabulação**, entretanto, podemos especificar o delimitador com o parâmetro: `-d`.

- `-d`: **Delimitador**
	especifica qual é o delimitador, exemplo: `-d:` o `:` será o separador.
- `-f`: **Especifica quais campos exibir**
	exatamente como descrito, podemos especificar os campos, mas o legal é que podemos selecionar vários e usar também [[Glob|Globbing]]:
	`cut -f1,5-7` dessa forma, somente a *primeira, quinta, sexta e sétima coluna*.
- `-c`: **Especifica quais caracteres exibir**
	Diferente do `-f`, esse especifica `qual caractere` vai aparecer, exemplo:
		há um arquivo denominado `ola mundo`, realizo o comando: `ls | cut -c1-3`, a saída será: `ola`, pois eu especifiquei que somente o primeiro ao terceiro caracteres apareceriam. 

[^1]: é o espaço gerado quando você pressiona a tecla **Tab**, ele é representado internamente como `\t`
