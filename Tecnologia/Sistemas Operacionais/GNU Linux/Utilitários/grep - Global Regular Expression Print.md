---
aliases:
  - grep
  - Global Regular Expression Print
---
O comando **grep (Global Regular Expression Print)** é uma ferramenta do [[Linux]]/[[Unix|Unix]] usada para pesquisar textos e padrões dentro de arquivos ou fluxos de dados, imprimindo as linhas correspondentes. 

Ele é essencial para analisar logs, filtrar saídas de outros comandos e realizar buscas recursivas rapidamente usando expressões regulares, sendo **[[Case Sensitive]]**

Seguindo a seguinte estrutura:
```bash
grep [opções] padrão [arquivo]
```
com o **padrão de busca (regex)**.
Sendo possível '**destacar**' o alvo, podemos incluir: `--color`, destacando no terminal aonde está o padrão.
### Caso de uso:
- **Busca simples**: pode ser usado para encontrar palavra em arquivos
- **Frases**: para pesquisar *termos compostos* (mais de uma palavra), o padrão deve ser colocado entre aspas.
### Parâmetros/Opções
- `-i`: **Ignora a diferença do [[Case Sensitive]]**
- `-v`: **Pesquisa invertida**
	Exibindo linhas que **Não** tem o padrão.
- `-n`: **Mostra o `número da linha`**
	Onde a ocorrência foi encontrada.
- `-c`: **Conta linhas da ocorrência**
	Exatamente, se tiver 3 linhas com a ocorrência, ele só conta.
- `-l`: **Exibe apenas o nome do arquivo com correspondência**
	O título é a própria explicação :D
- `-w`: **Busque pela palavra exata**
	Exitando correspondência parciais, exemplo:
		aparecer `connect`, sendo que procuro: `reconnect` 
---
### Busca recursiva
- `-r`: **Recursiva**
	Amplia a busca para todo os arquivos e subdiretórios.
- `-R`: **Rastrear**
	Eu que dei esse nome, pois aparentemente é a mesma coisa do Recursiva, porém ele segue [[symlinks]].
---
### Contexto
- `-A` Mostra linhas **após** (After) a correspondência.
- `-B`: Mostra linhas **antes** (Before) a correspondência.
- `-C`: Mostra linhas tanto antes quanto depois da correspondência.
---
Também aceita o uso de [[Glob|Globbing]]