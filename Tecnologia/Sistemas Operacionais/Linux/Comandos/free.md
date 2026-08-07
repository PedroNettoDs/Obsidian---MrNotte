### Sobre
o comando `free`, do [[Linux]]/[[Unix]], serve para trazer informações do arquivo: `/proc/meminfo`
>Que pasta é essa `/proc/`?
>Para isso, recomendo a leitura do [[FHS - Filesystem Hierarchy Standard|FHS]], mas resumindo, armazena arquivos gerados dinamicamente pelo kernel, informando estado de núcleos e processos.
---
### Parâmetros
Ao utilizar o comando sem nenhum parâmetro, as informações serão exibidas em [[kilobytes]], logo, os parâmetros do comando, são para definir a unidade de medida do arquivo.

- `-m`
	Exibirá o valor em [[Megabytes]]
- `-g`
	Exibirá o valor em [[Gigabytes]]
- `-h`
	Exibirá o valor 'humano' (???) 
![[comando free - exemplo.png]]

Vamos agora entender o que é cada coluna.
- **Total**, há realmente necessidade de explicar?
- **Usada**, é.. isso ae
- **Livre**, adivinha?
- **Compartilhada**, tá agora sim.
	Aplicações podem acessar o '*mesmo espaço de memória*', comumente aplicações que utilizam [[tmpfs - Temporary File System]] ou ambiente de [[Máquinas virtuais (VMs)|Virtualização]].
	https://en.wikipedia.org/wiki/Shared_memory
- [[Buffer]]
	Espaço de memória usado pelo [[Kernel]].
- [[Cache]]
	Tem o mesmo conceito dos Buffers, salvando informações de dados na memória RAM, pois é mais rápida que o disco.

https://linuxsemfronteiras.com.br/entendendo-o-comando-free/