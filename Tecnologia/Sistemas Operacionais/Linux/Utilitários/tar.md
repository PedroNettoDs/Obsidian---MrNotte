---
aliases:
  - Tape Archive
  - Tarball
---
 Utilizado para realização do '**[[Arquivamento e Compressão|Arquivamento]]**' de vários arquivos e [[Diretórios|diretórios]] em um único arquivo.

Arquivamentos feitos com o Tar, são denominados 'Tarball'.

Possuindo três modos importantes:
### **Criar**
Gera um novo arquivo compactado a partir de uma série de arquivos.
```bash
tar -cf  [ARQUIVO DE SAÍDA] [ARQUIVO DE ENTRADA...]
```
A criação de um arquivo com o comando, requer esses dois parâmetros:
- **`-c` Create**
	Cria um arquivo compactado
- **`f ARQUIVO`**
	Utiliza o arquivo específico.
```bash 
# Cria um tarball simples
tar -cf backup.tar arquivo1.txt arquivo2.txt
# criará um 'backup.tar' com os arquivos txt informados dentro.
 
# Criar e já comprimir com gzip
tar -czf backup.tar.gz  /home/pedro/documentos/

# Criar e comprimir com bzip2
tar -cjf backup.tar.bz2 /home/pedro/documentos/
```
>o parâmetro `-z` é por conta do [^1]algorítimo **Lempel-Ziv (LZ77)**, utilizado pelo '**gzip**'.
>o parâmetro `-j` é por conta do [^1]algorítimo **Burrows-Wheeler**, utilizado pelo '**bzip2**'
---
### **Extrair**
Retira um ou mais arquivos de um arquivo compactado.
Para extrair é necessário o parâmetro:
- **`-x` Extrair** 
```bash
# Extrai no diretório atual
tar -xf backup.tar

# Extrai um .tar.gz
tar -xzf backup.tar.gz

# Extrai um diretório específico com -C
tar -xzf backup.tar.gz -C /home/documentos/

# Extrai somente um arquivo selecionado do tarball
tar -xzf backup.tar.gz arquivo.txt
```
> Perceba que assim como no criar, o parâmetro `-z` retorna, é para justamente especificar o algorítimo da compressão.
> Outro detalhe é o parâmetro `-C`, para especificar o **Caminho**, aparentemente ele é utilizado mais no final, para se caso eu queria 'somente um arquivo do tarball' e no final eu especificar aonde. 
### **Listar**
Exibe o tarball conteúdo do arquivo compactado sem extraí-lo.
- **`-t` Listar**
```bash
# Lista conteúdo de tarball simples.
tar -tf backup.tar

# Lista conteúdo de um .tar.gz
tar -tzf backup.tar.gz

# Lista com detalhes (permissões, tamanho, data) usando -v
tar -tvf backup.tar
```
>Reforçando que o parâmetro `-f` é para 'especificar arquivo'
>O parâmetro `-v` Verbose, retorna novamente, ele serve para bastantes detalhes.
---


![[tar - exemplo.png]]
perceba como foi utilizado um [[Glob|metacaractere]]: `*` para selecionar todos os arquivos da pasta que começavam com 'alpha'.

[^1]: ![[Algoritmo]]
