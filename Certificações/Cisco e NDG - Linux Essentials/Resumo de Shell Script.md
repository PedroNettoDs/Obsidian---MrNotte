Um script [[Shell]], é um arquivo de texto que contém comandos executáveis.

Quando executamos esse arquivo script, cada comando é processado, pois o [[Shell]] interpreta todos os códigos e suas lógicas

Exemplo, temos o comando: `echo "Hello, World"`, caso salvemos ele no arquivo: `script.sh`.
Assim, evitamos ter que escrever o comando todo, basta executar o arquivo:
`.script.sh` e a saída será: `Hello, World`.

Para executar, utilizamos o **prefixo**: `./`

---
Ao iniciar um script, há um 'ritual' que se deve fazer, que seria: 
Incluir `#!/bin/bash` em cima.

e o motivo disso, é para especificar qual [[Shell|shell]] estará sendo usado.
Podendo variar:
Há métodos de Shell, entre eles: 
-  [[Zsh]]
-  [[Bash]]
-  [[sh]]

Caso ocorra **Permission denied**, significa que o arquivo não foi marcado como executável com o [[chmod]]

### Variáveis
Variáveis são usadas para armazenar valores. 
Pense nelas como caixas com um nome, onde você guarda alguma coisa.

**Regras básicas:**
- Para **atribuir**: use o nome direto → `ANIMAL="penguin"`
- Para **acessar**: prefixe com `$` → `$ANIMAL`
- **Não use espaços** ao redor do `=`, senão ocorre erro

**Formas de atribuir valor a uma variável:**
```bash
# Valor direto:
ANIMAL="penguin"

# Conteúdo de outra variável:
SOMETHING=$ANIMAL

# Saída de um comando (usando crases):
CURRENT_DIRECTORY=`pwd`

# Input do usuário:
read NAME
```

---
### Condicionais
Assim como outras linguagens, há como definirmos condicionais.

#### If
O `if`, executa um bloco de código, dependendo do resultado.
```bash
if grep -q root /etc/passwd; then
  echo "root existe no arquivo"
else
  echo "root não existe no arquivo"
fi
```

Há um comando de `test` que também é chamado através do `[ ]`
```bash
if test -f /tmp/foo; then
if [ -f /tmp/foo ]; then
```

- `-f`: *Verdadeiro se o arquivo existe*
- `-d`: *Verdadeiro se o diretório existe*
- `1 -eq 1`: *Igualdade numérica*
- `1 -ne 1`: *Diferença numérica*
- `1 -gt 1`: *Maior que (numérico)*
- `"a" = "a"`: *Igualdade de string*
- `"a" != "a"`: *Diferença de string*
- `-O`: *OU Lógico*
- `-a`: *E Lógico*
- `!`: *Negação*

O `then` existe por razões de **sintaxe da linguagem**, ele marca onde termina a condição e onde começa o bloco de comandos a executar. É como dizer:
> "**SE** esta condição for verdadeira, **ENTÃO** execute isto"
---
#### Elif
para múltiplas condições:
```bash
if [ "$1" = "hello" ]; then
  echo "hello yourself"
elif [ "$1" = "goodbye" ]; then
  echo "até mais!"
else
  echo "não entendi"
fi
```
---
#### Case
alternativa mais limpa ao `if/elif` quando há muitas opções:
```bash
case "$1" in
hello|hi)
  echo "hello yourself"
  ;;
goodbye)
  echo "até mais!"
  ;;
*)
  echo "não entendi"
esac
```
- `|`:*OU (múltiplos padrões)*
- `*)`: *equivale ao `else` (captura qualquer valor)*
- `;;` : *encerra cada bloco*
- O processamento para no **primeiro padrão** que corresponder
---
### Loops
Propriamente dito, 'dá um giro' podendo repetir novamente, utilizado para processar vários arquivos um determinada quantidade de vezes.
```bash
OS="ubuntu debian fedora"
for DISTRO in $OS; do
  echo "Instalando pacotes em: $DISTRO"
done
Instalando pacotes em: ubuntu
Instalando pacotes em: debian
Instalando pacotes em: fedora
```

A lista também pode ser passada diretamente, ou usar [[Glob]]:
```bash
# Glob — itera sobre todos os arquivos do diretório atual:
for S in *; do
  echo "Fazendo algo em $S"
done
```
