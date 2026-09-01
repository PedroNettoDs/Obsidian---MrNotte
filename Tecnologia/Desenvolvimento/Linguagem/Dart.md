# Sobre
Linguagem de programaçãoao criada pelo [[Google]] em 2011, com o intuito de criar aplicativos para celulares e computadores.
Hoje ela é muito famosa por ser a 'base do [[Flutter]]', 
$ sudo apt-get remove -y dart


## Dart: criando e manipulando variáveis e listas

### Funções iniciais

#### void main(){}
- `void`
	vazio, não retorna nada;
- `()`
	recebe argumentos de fora;
- `{}`
	Nosso código fica aqui dentro.
---
#### print();
- `print`
	Função que imprime informações no console;
- `()`
	Recebe a informação;
- `;`
	Necessário para terminar a frase.
---
### Tipos de variáveis

#### Numbers
Quantificar objetos e criar valores numéricos.
Necessários para quantificar;
**Tipos:**
- `init;`
	Aceita números inteiros;
- `double;`
	Aceita números fracionados;

****
#### Boolean
Valor simples de verdadeiro ou falso
**Tipos:**
- `true`
	Verdadeiro / Sim
- `false`
	Falso / Não
Comparações resultam em bool;
	Cinco é menor que 10? (Sim)
	`(5<10) == true;`

---
#### String
Criar e escrever frases inteiras.
- Necessário estar entre aspas: `''`
	Podemos usar Aspas duplas `""`
- Podemos receber informações de objetos criados
	'Eu tenho `$idade` anos de idade'
- É possível **concatenar** (juntar frases):
	'Eu amo ' + 'Dart'

---
#### Listas Únicas
Ideal para manipular vários objetos iguais juntos.
`List<String> nomes = [];`
- `List`
	Comando para definir o objeto;
- `<string>`
	Define o tipo de valor;
- `nomes`
	Identificação da Lista
- `[]`
	Lista vazia.
	
`List<String> nomes = ['Kako','Ricarth','Natália'];`

---
#### Listas Dinâmicas
Listas que aceitam objetos diferentes entre si.

`List<dynamic> personas = [];`
	`List`
		Comando para definir o objeto
	`<dynamic>`
		Tipo dinâmico (Variável)
	`personas`
		Identificação da Lista
	 `[]`
		Lista vazia
`List<dynamic> personas = ['kako',27,true];`

---
#### Var, Const e Final
Definir se o objeto pode mudar ou ficar fixo
-  **Var - Tipo variável:**
	O Dart defino o tipo;
	usar quando não souber o tipo do objeto.
	
- **Const - Define como constante:**
	O Dart bloqueia o objeto de qualquer alteração;
	melhora a perfomace do código
	
- **Final - Variáveis não iniciadas e constantes**
	Não sabe o valor inicial do objeto
	uma vez que souber, impede mudanças
---
### Condicionais

#### If / Else
Condição de escolha baseada em booleanos
`if(){} else {}
- `if`
	Comando que inicia a condição
- `()`
	Comparação com resultado [[booleano]]
- `{}`
	Ação tomada caso valor verdadeiro
- `else`
	Comando para indicar ação caso falso
- `{}`
	Ação tomada caso valor seja falso.
	
`if(idade>=18){“maior de idade”}else{“menor de idade”}`
**Preview**:
```dart
if(idade>=18){
	print("Maior de idade");
}else{
	print("Menor de idade");
}
```
---
#### For
Criação de loops de repetição simples
`for(int i=0; i<10;i++){}`
- `for`
	Comando que inicia o loop
- `(int i=0;i<10;i++)`
	Argumento de condição
- `int i=0`
	Iniciar objeto de comparação
- `i<10`
	Comparação para condição
- `i++`
	Ação pós-loop
	
`for(int a=0;a>=6;a=a+2){print(“ Repetição $a”);}`
**Preview**:
```dart
for(int a=0;a>=6;a=a+2){
print(“Repetição $a”);
}
```
---
#### While / Do
Loops de repetição sem limites definidos
`while(){}`
- `while`
	Comando para iniciar a repetição;
- `()`
	Condição;
- `{}`
	Ação tomada caso verdadeiro.

`do{}while()`
- `do`
	Comando para iniciar ação;
- `{}`
	Ação;
- `while()`
	Comando para verificar repeti;'ao.

---
### Cometários
Importantes para guiar quem vai ler o código
-  `\\ ou /**/`
	Comentários simples e cinzas, ideais para não poluir o código;
- `/// ou /*****/`
	Comentários de Docuemntação, verdes e podem poluir o código;

---


## Ferramentas
Documentação do DART:
https://dart.dev/tools

Para aprender Dart, há o 'https://dartpad.dev/'

[[SDK]] do Dart

