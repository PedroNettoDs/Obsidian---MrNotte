### _Préfacio_
No começo do meu quarto semestre da faculdade, recebi a noticia que os e-mails institucionais dos alunos seriam encerrado em conjunto com acessos a 'Teams, Excel, Outlook e OneDrive', possivelmente alguma negociação saiu errado entre o Centro Paula Souza e a [[Microsoft]].

Ainda assim, vi essa situação de Caos e lembrei que recentemente houve uma doação da Receita Federal para a Faculdade, então no laboratório há alguns servidores, antigos, porém a nossa disposição, então conversei com dois professores:
- Paulo
- Torres
Para minha surpresa, quem abraçou a ideia foi o Paulo, com quem já tive algumas discussões e o Torres, uns dos melhores professores que tive, sequer respondeu minha mensagem.

Mas ainda assim, o Paulo pediu para que eu realiza-se os documentos do projeto, e com auxilio do [[Claude]], criei os documentos em anexo.

---
### Documentos
![[Projeto Fileserver - Plano de Implementacao.pdf]]

![[Projeto Fileserver - Documento de Requisitos.pdf]]

---


---
### Solicitação
Diante dessas documentações de projeto, foi conversado e pedido para que somente os professores e diretores possam utilizar o [[Fileserver]] enquanto que os alunos vão somente ler e copiar os arquivos desse fileserver

Logo, decidi utilizar '[[Infraestrutura como Código (IaC)|IaC]]' no [[Bare Metal|Servidor bare-metal]], utilizando [[Ansible]]
Pois se torna mais rápido:
`Você edita um arquivo YAML → roda um comando → o servidor se configura sozinho`

---
### Testes
Sendo minha primeira vez utilizando [[Ansible]], contei com o Claude para me auxiliar, *(entretanto, ele tem alguns 'vícios de I.A' para consumir uso que irritam.)*

![[Estrutura - Fileserver - FATEC.canvas]]


1. Instalação do [[Multipass]]:
	Para não instalar um fileserver na minha máquina, prossegui com a criação deu ma VM para rodar os testes, sendo assim mais fácil de destruir e reconstruir quantas vezes desejar.
```bash
# Instalar via Snap
sudo snap install multipass

# Confirmar instalação
multipass version

# Etapas para configurar o direcionamento de 'qual armazenamento será utilizado'
#1. Parar o Multipass
sudo snap stop multipass
#2. Conectar a interface de mídia removível
sudo snap connect multipass:removable-media
#3. Criar o diretório no HD
sudo mkdir -p {Caminho desejado}
#4. Criar o override de storage via systemd 
sudo mkdir -p /etc/systemd/system/snap.multipass.multipassd.service.d/ sudo tee /etc/systemd/system/snap.multipass.multipassd.service.d/override.conf <<EOF
[Service]
Environment=MULTIPASS_STORAGE={Caminho desejado}
EOF
# 5. Recarregar e subir 
sudo systemctl daemon-reload sudo snap start multipass 
# 6. Criar a VM 
multipass launch 24.04 --name fatec-fileserver --disk 20G --memory 2G
```

Com a VM criada, podemos prosseguir com a coleta de informações da mesma
```bash
multipass info fatec-fileserver
```
Aparecendo semelhante a:
```
pedro.netto@pop-os:~$ multipass info fatec-fileserver  
Name:           fatec-fileserver  
State:          Running  
Snapshots:      0  
IPv4:           10.117.242.138  
Release:        Ubuntu 24.04.4 LTS  
Image hash:     7aa6d9f5e8a3 (Ubuntu 24.04 LTS)  
CPU(s):         1  
Load:           0.15 0.19 0.08  
Disk usage:     2.0GiB out of 19.3GiB  
Memory usage:   335.2MiB out of 1.9GiB  
Mounts:         --
```
Logo vemos o IPv4: 10.117.242.138
Prosseguimos com a configuração de acesso SSH:
```bash
ssh-keygen -t rsa -b 4096
`cat ~/.ssh/id_rsa.pub | multipass exec fatec-fileserver -- bash -c "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"`
```
e prosseguimos com um teste:
```bash
ssh ubuntu@<IP_DA_VM>
```

Assim, entrando na VM com sucesso.
Voltamos para o projeto e então 