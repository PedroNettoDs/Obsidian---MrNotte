---
tags:
  - virtualização
---
Nativamente o [[Linux]] não possui compatibilidade do pacote adobe

- Objetivo: **Windows rodando Adobe (Photoshop, Premiere, etc.) com desempenho real**
    
> Importante  
> Para **Adobe rodar bem**, **GPU passthrough é praticamente obrigatório**. Sem isso, Photoshop até abre, mas Premiere/After Effects ficam limitados ou instáveis.

---
## VISÃO GERAL DO QUE VAMOS FAZER

1. Verificar se **virtualização e IOMMU** estão ativos
    
2. Instalar **[[QEMU]] + [[kvm]] + [[libvirt]] + [[virt-manager]]**
    
3. Ativar **[[IOMMU - Input-Output Memory Management Unit]] no [[Pop!_OS]] (kernelstub)**
    
4. Preparar **[[VFIO]]**
    
5. Isolar a **RTX 3060 do host**
    
6. Criar [[Máquinas virtuais (VMs)|VM]] Windows (UEFI + Q35)
    
7. Instalar drivers NVIDIA no Windows
    
8. Ajustes para **evitar Error 43**
    
9. Instalar Adobe no Windows

---

Para virtualização, é necessário ter habilitado na BIOS recusos denominados:
IOMMU e também a 'virtualização da CPU' para os [[CPU|Processador]]:

Para Intel: `$ dmesg | grep VT-d`  
Para AMD: `$ dmesg | grep AMD-Vi`

Depois de inicializar no host, certifique-se de que o IOMMU está ativado: `$ dmesg | grep IOMMU`

Você deve ver algo tipo:
```
AMD IOMMU detected
```

Caso esteja desativado, usamos [[kernelstub]]

`sudo kernelstub -a "amd_iommu=on kvm.ignore_msrs=1"`


---

### Instalar o QEMU + KVM + vir-manager

No **Pop!_OS 24.04**:
```bash
sudo apt update sudo apt install -y \ qemu-kvm \ libvirt-daemon-system \ libvirt-clients \ virt-manager \ ovmf
```

Ativar [[libvirt]]:
```
sudo systemctl enable --now libvirtd
```

Adicionar teu usuário ao grupo:
```
sudo usermod -aG libvirt,kvm $USER
```

👉 **Reinicia o sistema** depois disso.

---

### Carregar módulos VFIO no boot

Cria o arquivo:
```bash
sudo nano /etc/initramfs-tools/modules
```

Adiciona:
```
vfio
vfio_iommu_type1
vfio_pci
vfio_virqfd
```

Atualiza:
```
sudo update-initramfs -u
```

--

# INACABADO