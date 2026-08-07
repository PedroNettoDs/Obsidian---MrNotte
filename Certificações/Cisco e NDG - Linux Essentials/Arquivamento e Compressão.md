---
aliases:
  - Arquivamento
  - Archive
---
O **Capitulo 8** do [[Cisco e NDG - Linux Essentials]]

Começa com a explicação do que seria '**Arquivamento**' (Archiving) e '**Compressão**' (Compression)  

Os dois processos, comumente são 'abstraídos e unificados' no [[Windows|Ruindows]], mas é importante diferenciar cada um deles.

- **Arquivamento**
	Combina vários em um só arquivo.
		O utilitário principal para isso é o **[[tar]]** (Tape Archive), arquvos passados por arquivamentos, são denominados 'pacotes' (mais informações do [[tar|tar aqui]])
		Importante destacar que o arquivamento **não reduz o tamanho dos dados**, ele se torna a soma dos arquivos originais.
- **[[Compressão]]**
	Reduz o tamanho dos arquivos.
		Utilizando [^1]algoritimos, que eliminam redundância.
	Ferramentas comuns são: gzip, bzip2, xz, zstd.
---
### Junção dos dois
No Linux eles são processos são '*unificados por fluxos*', ou seja, em uma situação de automação, a boa prática seria a criação dessa '*pipeline*'.

Sendo necessário *primeiro, utilizar o `tar`*, para reunir os diversos arquivos em um único pacote, *em seguida, comprimimos* para redução do tamanho desse pacote com alguma ferramenta, por exemplo `gz`, assim o arquivo final seria:
`arquivo.tar.gz`, simbolizando que é um arquivo, arquivado e comprimido.

Embora a filosofia [[Unix]] pregue a separação, existem ferramentas que fazem a 'abstração' desse processo.

[^1]: ![[Algoritmo]]