---
aliases:
  - Advanced Package Tool
  - apt
---
O comando `apt`  (Advanced Package Tool), é um [[Gerenciador de Pacotes]] padrão para [[Distribuição Linux]] baseadas em [[Debian]], como: [[Ubuntu]] e [[Linux Mint]].

Ferramenta principal para:
- Instalar
- Atualizar
- Remover
- Gerenciar programas

Lidando automaticamente com [[Dependências]], buscando pacotes em servidores onlines, chamados '[[Repositórios]]', que ficam salvos em seu armazenamento:
`/etc/apt/sources.lis`

https://www.debian.org/distrib/packages
https://packages.ubuntu.com/
---
### Comandos
- `sudo apt update`
	- Sincroniza a lista de pacotes do seu sistema com [[Repositórios]] oficiais
- `sudo apt upgrade`
	- Instala as versões mais recentes de todos os pacotes já instalado no sistema
- `sudo apt install <nome>`
	- Baixa e instala um novo programa e suas [[Dependências]]
- `sudo apt remove <nome>`
	- Remove o programa, mas mantem o arquivo de configuração
- `sudo apt purge`
	- Remove o program e também o arquivo de configuração
- `sudo apt autoremove`
	- Remove pacotes que foram instalados automaticamente na 'resolução de [[Dependências|dependência]]'
#### Buscas e informações
- `apt search <palavra-chave>`
	- Procura por pacotes disponíveis no repositório.
- `apt show <nome>`
	- Exibe detalhes sobre um pacote específico
- `apt list --installed`
	- Lista todos os programas que estão instalados no sistema


---
### Diferença entre *apt* e *apt-get*
Há uma diferença entre o comando `apt` e o `apt-get`, como explica esse [artigo](https://aws.amazon.com/pt/compare/the-difference-between-apt-and-apt-get/);

**Resumidamente**:
- o `apt` é mais atualizado (*lançado em 2014*) e projetado para ser 'mais fácil' que o `apt-get` (*lançado em 1998*)
- **Recurso de pesquisa**
	- `apt search <nome>` fornece descrição detalhada do software da `<nome>`
	- enquanto no `apt-get`, precisava-se utilizar o comando `apt-cache`
- Resolução de [[Dependências|dependência]]
	- Os dois resolvem e instalam os 'subprogramas' necessários, entretanto o `apt` faz isso 'na ordem correta'
- Enquanto o `apt` gerencia os pacotes o `apt-get` é baixo nível e comunica com processos do [[Linux]]