O [[Windows|Ruimdows]] adora colocar travas em você e uma delas é justamente no HD, durante o processo de atualização infinita do Sistema operacional, aonde é implantado cada vez mais [[Bloatwares]], para 'segurança' da atualização, o sistema bloqueia seu HD.

e isso fica visível se você é um usuário de DualBoot, pois eu mesmo, tenho o HD que seria uma espécie de 'Ponte' para eu poder transmitir arquivos entre meus dois sistemas.

Porém, sempre que troco, não tenho permissão sequer de modificar qualquer coisa desse HD, então hoje, para solucionar, fui atrás de mágias e elas seriam:

```bash
sudo ntfsfix -d /dev/sdc1
```

```bash
sudo systemctl restart mnt-hd.mount
```

```bash
ls /mnt/hd
```