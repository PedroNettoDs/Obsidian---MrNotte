Pois esse **Capitulo 9** do [[Cisco e NDG - Linux Essentials]]

 Aonde está abordando sobre o [[Sistema de Arquivos]] das distribuições [[Linux]].
Começando explicando sobre o '[[Case Sensitive]]' e prossegue pontuando sobre o Linux utilizar [[UTF-8]].

---
### **[[Glob|Globbing]]**
Resumindo: '*é parâmetros para selecionar vários arquivos durante a execução de algum script*'

---
### Copiando arquivos
o comando usado para copiar arquivos de uma origem até o destino é o `cp`, sua estrutura deve ser:
```bash
cp origem destino
```
**Exemplo**:
```bash
cp /etc/hosts ~
```
>**Reforçando**: o caractere `~` representa o diretório '*home*'

O comando `cp`, pode **Sobrescrever**, caso já possua um arquivo com o mesmo nome no local de destino, para evitar isso, a orientação seria a inclusão do parâmetro: `-i`, solicitando assim uma autorização para sobrescrever ou não.
**Exemplo**:
```bash
cp -i /etc/hosts example.txt                   
# cp: overwrite `/home/sysadmin/example.txt'? n
```

#### Modo Verboso / Verbose Mode:
Acrescentar o parâmetro: `-v` faz surgir uma 'saída', mostrando justamente a movimentação do arquivo, exemplo:
```bash
cp -v teste.txt ~
#'teste.txt' -> '/home/netto/teste.txt'
```
---
### Copiando Diretórios
Por padrão o comando `cp` não copia diretórios, resultando assim em erro.
```bash
cp pasta/ ~/Dev
# cp: -r não especificado; omitindo o diretório 'pasta/'
```
Mas se você notar, o erro mesmo já deixa claro como corrigir: `-r` **recursivo**, replicando para os subdiretórios.
Semelhante o caso ao tentar apagar o diretório, que resulta em: [[Directory not empty]]

---
### Movendo arquivos
Para mover arquivos, utilizamos o comando: `mv`, seguindo a seguinte estrutura:
```bash
mv origem destino
```
Não há muito o que dizer, a não ser que possa dar 'sem permissão de escrita'.

---
### Renomeando arquivos
Reutilizando o comando: `mv`, seguindo a ideia de que, se você dizer 
'*quero mover o arquivo X.txt para a pasta Y e o nome será Z.txt*', nessa linha de raciocínio, podemos renomear os arquivos ocm base no '*destino*'.
**Exemplo**:
```bash
ls
# saída: origem.txt

mv origem.txt destino.txt
ls
# saída: destino.txt
```
>Dessa forma o arquivo foi renomeado, pois apontamos o arquivo de origem e como ele seria no destino, **OBS**: isso também funciona no *copiar*.

#### Opções adicionais:
assim como pontuado no comando `cp`, no `mv` também possuímos opções: 
- `-i`: Interação (perguntar antes de sobrescrever).
- `-n`: Não sobrescreve conteúdos 
- `-v`: Verbose, mostra o resultado.

---
### Criando arquivos:
Para criar um arquivo, há o comando `touch`, não tenho muito a pontuar sobre ele, pois é bem simples:
```bash
touch teste.txt
ls
# teste.txt
```
---
### Removendo arquivos
Para remover, seria o comando `rm`, abreviação de **Remover**.
```bash
rm teste.txt
rm -i teste.txt #confirma se quer mesmo excluir
```
---
### Criando diretório
Criar diretório é através do comando: `mkdir`, de 'Make Directory', muito criativo.
```bash
mkdir teste
ls
# /test
```

