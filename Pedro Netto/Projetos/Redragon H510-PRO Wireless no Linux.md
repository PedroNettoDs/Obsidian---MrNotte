---
Blogspot: https://nettotecnologias.blogspot.com/2026/07/redragon-h510-pro-wireless-no-linux.html
---
# (PipeWire/ALSA)

Esse headset funciona no [[Linux]], mas o dongle wireless tem alguns bugs no driver `snd_usb_audio`. 
O problema mais comum é o volume: o canal direito zera o fone, e o controle global do [[GNOME]]/[[Pulse]]/ [[PipeWire]] não conversa direito com o mixer interno.
A solução é forçar o uso de mixer em software e configurar manualmente.

# Passo 1 – Instalar [[PipeWire]] + [[WirePlumber]]
No Ubuntu 24.04 já vem quase tudo. Se faltar:
```
sudo apt install pipewire-audio wireplumber pipewire-pulse
```

# Passo 2 – Ajustar pelo ALSA
Abra o mixer:
```
alsamixer
```

- Pressione **F6** e escolha `H510-PRO Wireless`.
    
- Ajuste os dois lados do fone (não deixe o direito em 0, senão ele corta o som).
    
- Para o microfone, use **F4**, escolha o H510 e regule o nível.
    
- Salve:
```
sudo alsactl store
```

# Passo 3 – Corrigir o bug de volume (WirePlumber)

Crie a pasta de configuração:
```
mkdir -p ~/.config/wireplumber/main.lua.d
```

Edite o arquivo:
```
nano ~/.config/wireplumber/main.lua.d/50-h510.lua
```

Cole:
```
rule = {
  matches = {
    {
      { "device.name", "equals", "alsa_card.usb-XiiSound_Technology_Corporation_H510-PRO_Wireless_headset-00" },
    },
  },
  apply_properties = {
    ["api.alsa.soft-mixer"] = true,
    ["api.alsa.ignore-dB"] = true,
  },
}

table.insert(alsa_monitor.rules, rule)
```

Salve e reinicie:
```
systemctl --user restart wireplumber
```

# Resultado

- O volume agora é controlado suavemente pelo GNOME ou pelo `wpctl`, sem matar o canal direito.
    
- O microfone funciona ajustando no `alsamixer`.
    
- Evite usar os botões de volume do headset, pois eles podem bagunçar os níveis internos.