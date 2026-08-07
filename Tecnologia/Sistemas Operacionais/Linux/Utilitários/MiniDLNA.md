*O* **MiniDLNA** é um software servidor com o objetivo de ser totalmente compatível com clientes **[[DLNA]]/[[UPnP]]**.

O [[Daemon]] do MiniDLNA disponibiliza arquivos de mídia (músicas, imagens e vídeos) para clientes em uma rede.

Exemplos de clientes incluem aplicativos como **Totem** e **XBMC/Kodi**, além de dispositivos como players de mídia portáteis, smartphones e televisores.

O MiniDLNA é uma alternativa simples e leve ao **MediaTomb**, porém com menos recursos. Ele não possui interface web para administração e deve ser configurado editando um arquivo de texto.

---
## Instalação

```bash
sudo apt update
sudo apt install minidlna
```

> **Nota importante (Pop!_OS 24.04 / Ubuntu 24.04):**
> - O **pacote** se chama `minidlna`.
> - O **daemon/binário** é `minidlnad`.
> - Em alguns sistemas existe `minidlna` apenas como *[[symlink]]* para `minidlnad` (não conte com isso).

---
## Configuração global (para todos os usuários)

O arquivo de configuração é:
- **/etc/minidlna.conf**

Exemplo de parâmetros úteis:
```ini
#network_interface=eth0         #Descoberta automática se comentado (bom com NetworkManager)
media_dir=A,/home/user/Music    #Use A, P e V para o tipo de mídia no diretório
media_dir=P,/home/user/Pictures
media_dir=V,/home/user/Videos
friendly_name=Laptop            #Nome de exibição

db_dir=/var/cache/minidlna      #geralmente já definido, descomente
log_dir=/var/log                #descomente
inotify=yes                     #'no' para menos recursos; reinício necessário p/ novas mídias
```
---
### Reiniciar o serviço para aplicar mudanças
Em sistemas modernos ([[Pop!_OS]]/Ubuntu atuais), prefira **[[systemd]]**:
```bash
sudo systemctl restart minidlna
```

### Forçar reconstrução do [[Banco de dados]] (global)
```bash
sudo systemctl stop minidlna
sudo rm -f /var/cache/minidlna/files.db
sudo systemctl start minidlna
```

> Dica: você também pode acompanhar logs com:
```bash
journalctl -u minidlna -f
```
---
## Configuração local (por usuário)
Esta abordagem faz sentido quando você **não quer** usar o serviço global do sistema.

### 1) Parar e desativar o serviço global
```bash
sudo systemctl stop minidlna
sudo systemctl disable minidlna
```

### 2) Criar diretórios locais e copiar a configuração
```bash
mkdir -p ~/.minidlna/cache
cp /etc/minidlna.conf ~/.minidlna/minidlna.conf
$EDITOR ~/.minidlna/minidlna.conf
```

### 3) Ajustes obrigatórios na configuração local
No arquivo `~/.minidlna/minidlna.conf`, defina **db_dir** e **log_dir** para o seu usuário:
```ini
db_dir=/home/$USER/.minidlna/cache
log_dir=/home/$USER/.minidlna
```
(Adapte também os `media_dir=` para pastas do seu usuário.)

### 4) Iniciar o daemon localmente (recomendado: `minidlnad`)
```bash
minidlnad -f /home/$USER/.minidlna/minidlna.conf \
  -P /home/$USER/.minidlna/minidlna.pid
```

### 5) Parar o daemon local
```bash
xargs kill < /home/$USER/.minidlna/minidlna.pid
```

### 6) Reconstruir banco de dados (local)
```bash
minidlnad -f /home/$USER/.minidlna/minidlna.conf -R
```

---
## Iniciar o MiniDLNA automaticamente ao logar ([[KDE Plasma]]/Plasma)
Crie o arquivo `~/.config/autostart/minidlna.desktop`:

```ini
[Desktop Entry]
Type=Application
Name=MiniDLNA
Comment=Servidor para transmitir mídia pela rede
Exec=minidlnad -f /home/$USER/.minidlna/minidlna.conf -P /home/$USER/.minidlna/minidlna.pid
StartupNotify=false
Terminal=false
Hidden=false
```

> Observação: no Plasma, isso inicia ao **logar no usuário**. Para iniciar antes do login, use o **serviço global** via `systemctl enable --now minidlna`.

---
## Solução de problemas

### Portas no firewall
Se estiver usando firewall, as portas abaixo precisam estar liberadas:
- **[[SSDP]]:** `1900/udp`
- **HTTP do MiniDLNA (trivnet1):** `8200/tcp`

Exemplo (conceitual) de configuração em firewall:
```text
OPEN_TCP="8200"
OPEN_UDP="1900"
```

### Conferir se o serviço está ativo
```bash
systemctl status minidlna
```

### Ver dispositivos clientes descobrindo o servidor
Se o servidor não aparece na TV/celular, verifique:

- Mesma rede/sub-rede (Wi‑Fi “isolado”/AP isolation pode bloquear)
- Firewall liberando `1900/udp`
- Roteador não bloqueando multicast/UPnP

---
## Checagens rápidas (para confirmar os binários no seu sistema)

```bash
command -v minidlnad
command -v minidlna || true
ls -l /usr/sbin/minidlnad /usr/sbin/minidlna 2>/dev/null || true
```

