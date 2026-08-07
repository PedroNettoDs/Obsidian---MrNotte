---
tags:
  - virtualização
---
É uma ferramenta da [[Canonical]], para criar [[Máquinas virtuais (VMs)|VM]]s [[Ubuntu]] na sua máquina com comandos.
`Docker, mas para máquinas virtuais completas`

---
#### Como funciona?
```
Sua máquina
└── Multipass
    └── VM: fileserver  ← Ubuntu Server isolado
        ├── IP próprio (ex: 192.168.64.5)
        ├── Disco próprio (20GB)
        └── Samba, quota, rsync instalados pelo Ansible
```

---
#### Como instalar?
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
multipass launch 24.04 --name {nome-vm} --disk 20G --memory 2G
```