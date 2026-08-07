---
Blogspot: https://nettotecnologias.blogspot.com/2026/07/conectando-o-googledrive-com-rclone.html
---
### Nota pessoal

Estou utilizando **[[Pop!_OS]] 24.04 + [[KDE Plasma]]** e, para criar notas no **Obsidian**, precisava que elas fossem sincronizadas com o **Google Drive**.

Entretanto, a comunidade do KDE está enfrentando um *bug* conhecido que impede a conexão via **Contas Online** do sistema. Há diversos relatos confirmando o problema:

- Discussão no Reddit: https://www.reddit.com/r/kde/comments/1lsor9n/is_it_really_impossible_to_configure_google_drive/

Em um dos comentários, vi a sugestão de utilizar o **[[rclone]]** como alternativa. A partir disso — e com apoio do ChatGPT — segui o processo abaixo, que se mostrou estável e funcional.

---
## 1) Instalar o rclone
```bash
sudo apt update
sudo apt install rclone -y
```

Confirme a instalação:
```bash
rclone version
```

----
## 2) Configurar o Google Drive no rclone
```bash
rclone config
```

Siga exatamente esta sequência:

1. **`n`** → New remote  
2. **Name**:  
   ```text
   gdrive
   ```
   ⚠️ Este nome é importante, pois será utilizado como identificador (`gdrive:`).
3. **Storage** → escolha:  
   ```text
   drive
   ```
4. **client_id** → pressione **Enter** (padrão)
5. **client_secret** → **Enter**
6. **scope** → escolha:  
   ```text
   1   (Full access)
   ```
7. **root_folder_id** → **Enter**
8. **service_account_file** → **Enter**
9. **Edit advanced config?** → `n`
10. **Use auto config?** →  
    - Em ambiente gráfico (KDE): **`y`**  
    - O navegador será aberto para login e autorização
11. **Configure as a Shared Drive?** → `n`
12. **Yes this is OK** → `y`
13. **`q`** → sair

Teste se a configuração funcionou:

```bash
rclone lsd gdrive:
```

Se suas pastas forem listadas, a conexão está correta.

---
## 3) Criar a pasta de montagem

```bash
mkdir -p ~/GoogleDrive
ls -ld ~/GoogleDrive
```

---
## 4) Teste manual da montagem (antes do systemd)

⚠️ Este passo é importante para garantir que tudo funcione antes da automação.
```bash
rclone mount gdrive: ~/GoogleDrive \
  --vfs-cache-mode full \
  --vfs-cache-max-size 4G \
  --vfs-cache-max-age 2h \
  --dir-cache-time 4h
```

Abra outro terminal e execute:
```bash
ls ~/GoogleDrive
```

Se seus arquivos aparecerem, a montagem está funcionando corretamente.

Para desmontar:
```bash
fusermount -u ~/GoogleDrive
```

---
## 5) Criar o serviço [[systemd]] (modo usuário)

Como a montagem ocorre dentro do *home* do usuário, o serviço deve ser criado como **[[systemd]] de usuário**.
### 5.1 Criar o diretório de serviços

```bash
mkdir -p ~/.config/systemd/user
```
### 5.2 Criar o arquivo do serviço

```bash
nano ~/.config/systemd/user/rclone-gdrive.service
```

Conteúdo do arquivo:

```ini
[Unit]
Description=Montar o Google Drive via rclone
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
ExecStart=/usr/bin/rclone mount gdrive: /home/pedro.netto/GoogleDrive \
    --vfs-cache-mode full \
    --vfs-cache-max-size 4G \
    --vfs-cache-max-age 2h \
    --vfs-read-ahead 256M \
    --dir-cache-time 4h \
    --poll-interval 30s \
    --buffer-size 64M \
    --timeout 2m \
    --umask 002
ExecStop=/bin/fusermount -u /home/pedro.netto/GoogleDrive
Restart=on-failure
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=default.target
```

Salve (`Ctrl+O`, `Enter`, `Ctrl+X`).

---

## 6) Ativar o serviço

Recarregue os serviços do usuário:

```bash
systemctl --user daemon-reload
```

Ative o serviço para iniciar no login:

```bash
systemctl --user enable rclone-gdrive.service
```

Inicie imediatamente:

```bash
systemctl --user start rclone-gdrive.service
```

Verifique o status:

```bash
systemctl --user status rclone-gdrive.service
```

Teste a montagem:

```bash
ls ~/GoogleDrive
```

Se os arquivos estiverem acessíveis, o Google Drive já estará integrado ao sistema de forma estável, sem depender do KIO ou das Contas Online do KDE.

---

Atualizações, após uns três meses usando, é muito irritante, você acessar a pasta e perceber que demora para baixar os arquivos por ser um mount remoto, logo vamos aperfeiçoar esse projeto para '[[Sincronizando pastas para o GoogleDrive]]'