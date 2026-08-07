---
aliases:
  - Redirecionamento de Saída
---
Input/Output (I/O), é o principio de um computador né, convenhamos.

**Alan Turing** inseriu códigos e recebeu a mensagem, assim como o Zézin pegou a calculadora, inseriu números e recebeu o resultado.

Assim, todo programa [[Linux]], opera com **três fluxos** padrão conhecidos como [[Descritores de arquivo]]:
![[Descritores de arquivo]]

Dessa forma, podemos realizar o **[[Input and Output Redirection|Redirecionamento de Saída]]**, ao especificar:
- `>` ou `1>`
	Redireciona a saída padrão para arquivo(substituindo ou criando)
- `>>`
	Semelhante ao `>`, mas anexa informação ao final do arquivo, sem apagar.
- `<`
	Redireciona a entrada, fazendo com que o comando leia os dados de um arquivo, em vez do teclado
- `<<`
	**(HERE Documents)**, dizem que 'incluem entradas na linha de comando', não entendi nada.
- `2>`
	Redireciona especificamente a **saída do erro** (sacou o motivo de ser 2?)
- `2>&1`
	Redireciona o erro para o mesmo 'destino da saída padrão', permitindo salvar erro e sucesso.
- `&>`
	Forma simples para redirecionar, tanto saída padrão e com erro.