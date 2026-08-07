---
Blogspot: https://nettotecnologias.blogspot.com/2026/07/sincronizando-pastas-para-o-googledrive.html
---
Realizei o projeto anterior: [[Conectando o GoogleDrive com Rclone]], entretanto, estou ficando atritado de tentar acessar a pasta e ele demorar para mostrar os arquivos, dessa forma, vamos mudar a estruturação do projeto.

Primeira coisa que fiz, foi baixar os arquivos atuais do meu GoogleDrive e com o .zip prossegui com as ações:

---
### Configuração de sincronização

Criei meu diretório: 
```
mkdir -p ~/Obsidian - MrNotte
```
Assim criando minha pasta na localização:
`/home/usuario/Obsidian - MrNotte/`

Depois prossegui com a criação de um diretório para Scripts (no geral mesmo) e criei o arquivo .sh:
```bash
mkdir -p ~/scripts
nano ~/scripts/rclone-sync.sh
```

e dentro configurei variáveis e depois utilizei o comando do [[rclone]]:
```sh
#!/bin/bash

LOGFILE="$HOME/rclone-sync.log"
LOCAL_DIR="/home/usuario/Obsidian - MrNotte/"
REMOTE_DIR="gdrive:Obsidian - MrNotte"

rclone sync "$LOCAL_DIR" "$REMOTE_DIR" \
    --delete-during \
    --progress \
    --log-file="$LOGFILE" \
    --log-level INFO
```

Dei a permissão de execução:
```bash
sudo chmod +x ~/scripts/rclone-sync.sh
```

E testei o script:
```bash
~/scripts/rclone-sync.sh
```
![[Sincronizando pastas para o GoogleDrive1.png]]
>Achei muito legal ver ele baixando e mostrando o progresso.

---
### Automatização de script:
Primeiro prossegui com a criação de um serviço no [[systemd]]:
```bash
nano ~/.config/systemd/user/rclone-sync.service
```
e preenchi com:
```ini
[Unit]
Description=Sincronizar Google Drive (local → remoto)

[Service]
Type=oneshot
ExecStart=/home/usuario/scripts/rclone-sync.sh
```

Depois prosseguimos com a criação do timer:
```
nano ~/.config/systemd/user/rclone-sync.timer
```
e configurei para executar todo dia 22:00:00 
```
[Unit]
Description=Executar sync do Google Drive diariamente

[Timer]
OnCalendar=*-*-* 22:00:00
Persistent=true

[Install]
WantedBy=timers.target
```
---
Assim ativando o serviço:
```bash
systemctl --user daemon-reload
systemctl --user enable rclone-sync.timer
systemctl --user start rclone-sync.timer
```

---
### Considerações finais
Com essa mudança, eu persisto tendo um 'mount' do Google Drive, porém não utilizo ele diretamente no meu Obsidian, logo não preciso esperar ele baixar todos os arquivos (*obs: isso estava me irritando, mudava de página e demorava tipo 10 segundos para baixar a página*), porém os arquivos markdown ficam na minha máquina e só é mandado pro Drive por segurança.