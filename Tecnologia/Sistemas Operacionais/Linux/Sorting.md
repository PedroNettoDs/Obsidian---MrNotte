---
aliases:
  - Sort
---
A tradução disso, acaba sendo '**Classificando**', mas também é um verbo: "**ordenar**".
![[Sorting-example.png|500]]

No [[Linux]], há o comando `sort`, utilizado para reorganizar as linhas de arquivos ou entradas, em ordem **alfabética** (*Abecedário, tlg né?*) ou **numérica**

**Exemplo**: 
`head -5 /etc/passwd > mypasswd`, o que o comando faz?
ele vai **redirecionar a saída** para o arquivo 'mypasswd' ([[Input and Output Redirection|Explicação]]), o arquivo em si, ficaria:
```cat mypasswd
root:x:0:0:root:/root:/bin/bash daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin bin:x:2:2:bin:/bin:/usr/sbin/nologin sys:x:3:3:sys:/dev:/usr/sbin/nologin sync:x:4:65534:sync:/bin:/bin/sync
```
Agora, rodando o comando: `sort`
```sort mypasswd
bin:x:2:2:bin:/bin:/usr/sbin/nologin daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin root:x:0:0:root:/root:/bin/bash sync:x:4:65534:sync:/bin:/bin/sync sys:x:3:3:sys:/dev:/usr/sbin/nologin
```
Perceba que ele ordenou em ordem alfabética

Podemos utilizar alguns parâmetros para esse comando:
- `-t`: **Delimitador**
	Podemos especificar um delimitador para a organização, no exemplo anterior, o delimitador foi `:`, para especificarmos, utilizamos: `-t:`. ^bed6af
- `-k`: **Número do campo**
	Depois do delimitador, precisamos especificar, qual é o campo que será ordenado.
		**Exemplo**: quero ver o **quart campo**:
		root:x:0:0:**root**:/root:/bin/bash
		Então o comando seria:
		`sort -t: -k3`
- `-n`: **Ordenação com número**
	Não tem muito a dizer, é isso mesmo.
- `-r`: **Ordenação inversa**
	Rapaz, se eu tiver que explicar o título, acho que é um problema..
	exatamente, ordena ao contrário, o que era do A ao Z, vira do Z ao A