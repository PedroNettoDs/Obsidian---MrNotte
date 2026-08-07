---
icon: FabDocker
---
é um sistema de #virtualização que cria '[[Contêineres]]', sendo 'isolados' da sua máquina (caso não configurar).

---
#### Comandos úteis:
Remover Volumes orfãos:
```bash
docker volume prune -f
```
## Instalação:

#### Configuração de certificado e chaves.
1. Atualizações do '**apt update**'
```bash
sudo apt update
```
	
2.  instalar o [[ca-certificates]]:
```bash
sudo apt install ca-certificates curl
```
	
3. configuração do [[keyrings]]:
```bash
sudo install -m 0755 -d /etc/apt/keyrings
```
> `-m 0755` -  Define permissões do diretório:
> `-d /etc/apt/keyrings` - o `-d` faz o 'install' criar um diretório 
> *Esse caminho é usado pelo APT para armazenar **chaves GPG de repositórios**, seguindo práticas mais modernas*
	
4. Baixar conteúdo via [[cURL (Client URL)]]
```bash
sudo curl -L https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
```
> `-L` (location): Segue redirecionamentos HTTP automaticamente.
> `-o <file>` (output): Salva saída em arquivo
> *O comando baixa e armazena a [[Chave GPG (GNU Privacy Guard)]] do Docker, permitindo que o APT confie no repositório Docker seguindo o padrão moderno de segurança.*
	
5. Alterar as permissões de acesso do arquivo:
```bash
sudo chmod a+r /etc/apt/keyrings/docker.asc
```

#### Adicionando repositório do Docker
1. Criar o .sources do Docker
```bash
sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Signed-By: /etc/apt/keyrings/docker.asc
EOF
```
> `tee <caminho>`: lê a entrada padrão (a saída de outro comando)
> `<<EOF` (here-document): Isso inicia um **here-document** (_[[heredoc]]_), até encontrar uma linha contendo **apenas**: `EOF`
	
2. Aplicar esse novo source no apt
```bash
sudo apt update
```

#### Instalando os pacotes Docker
1. Realize a instalações dos pacotes via `apt install`
```bash
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
> Assim que instalado, o serviço do Docker inicia automaticamente.
	
2. Checagem de funcionamento:
```bash
sudo systemctl status docker
```
> caso esteja 'disabled' utilize o comando: `sudo systemctl start docker`
	
3. 'Hello World' com Docker
	Para testar, tentaremos baixar a imagem de um conteiner que retorna 'Olá Mundo':
```bash
sudo docker run hello-world
```

---
## Desinstalação:
para desinstalar o Docker, siga:

1. Remover o Docker Engine, CLI, Containerd e pacotes de composição:
```bash
sudo apt purge docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin docker-ce-rootless-extras
```
	
2. Remover imagens, containers, volumes e arquivos de configuração:
```bash
sudo rm -rf /var/lib/docker
sudo rm -rf /var/lib/containerd
```
	
3. Remova o source list e keyrings:
```bash
sudo rm /etc/apt/sources.list.d/docker.sources
sudo rm /etc/apt/keyrings/docker.asc
```

#### Referência:
https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository