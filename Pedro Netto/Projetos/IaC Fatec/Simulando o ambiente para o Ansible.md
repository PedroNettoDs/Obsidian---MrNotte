Pois bem dei inicio de fato ao projeto, com isso, já montei na sala de pesquisa o computador que será o servidor.

Entretanto, não fiz um teste na minha máquina antes :D (jenio), portanto, estou nesse momento pesquisando como criar VM's de fato no meu Kubuntu.

---
Para isso, o Claude me recomendou a seguinte stack:

[[QEMU|qemu-kvm]]          → O emulador (o motor das VMs)
[[libvirt-daemon]]     → O daemon que gerencia VMs
[[libvirt-clients]]    → Ferramentas (virsh, virt-install)
[[virt-manager]]       → Interface gráfica bonita
[[bridge-utils]]       → Ferramentas para configurar rede bridge

Assim então prossegui com a instalação dessas ferramentas:
```bash
sudo apt install qemu-kvm libvirt-daemon libvirt-clients virt-manager bridge-utils -y
```

Ao instalar o 'virt-manager', pode ocorrer o erro:
![[Simulando o ambiente para o Ansible - erro.png]]
`Permissão negada ao conectar em /var/run/libvirt/libvirt-sock`

podemos checar se o serviço está rodando com:
`systemctl status libvirtd.service`

Porém o erro em questão é sobre não ter permissão de acessa-lo, sendo então necessário incluir o usuário com permissão:
`sudo usermod -aG libvirt <usuário>`

Assim seria necessário fazer logout e login novamente, mas não vou mentir, depois do upgrade de memória RAM, eu tenho salvo muitas páginas no mozila, então não me agrada muito ter que reiniciar e perder (a mas é só apertar CTRL+SHIFT+T).. TÁ! ME CONVENCEU!

Mas eu aprendi que existe um comando [[newgrp]] que permite ativar o grupo especifico ao terminal aberto, assim inicializei o virt-manager: `virt-manager &

Já baixei a imagem do Ubuntu Server, assim esperei o carregamento do 'Gerenciador de máquinas virtuais', prossegui com a criação de uma nova:
![[Pasted image 20260504232519.png]]

Ubuntu Server instalado com sucesso, usuário criado e zas.
Porém agora precisamos garantir que o usuário 'netto' utilize o [[Sudo]] sem precisar da senha para o [[Ansible]].
Para isso, utilizei:
`echo "netto ALL=(ALL) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/netto`

e criei uma chave SSH que direcionei para dentro da VM, através do comando:
`ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa -N ""`
e
`ssh-copy-id -i ~/.ssh/id_rsa.pub netto@192.168.122.145`

dessa forma, atualmente no ambiente de Dev:
```
Seu Kubuntu (Control Node)
    ├─ Ansible instalado aqui
    ├─ Playbooks ficam aqui
    └─ Você roda "ansible-playbook" daqui
        ↓ (SSH sem senha)
        ↓
    VM Ubuntu 192.168.122.145 (Managed Node)
        ├─ Python 3 
        ├─ SSH 
        └─ sudo sem senha 
```