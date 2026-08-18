---
aliases:
  - Network Statistics
  - netstat
---
Ferramenta [[legada]] para monitorar conexões de rede

---
### Flags principais

| Flag | Significado                                |
| ---- | ------------------------------------------ |
| `-t` | Conexões **[[TCP]]**                       |
| `-u` | Conexões **[[UDP]]**                       |
| `-l` | Portas em **listening**                    |
| `-n` | Exibe **números** (sem resolver DNS)       |
| `-p` | Mostra o **processo/PID**                  |
| `-a` | **Todas** as conexões                      |
| `-r` | Tabela de **roteamento**                   |
| `-i` | Estatísticas por **interface** de rede     |
| `-s` | **Resumo** por protocolo                   |
| `-c` | Atualiza **continuamente** (como um watch) |

---

### Combinações mais usadas

bash

````bash
# Portas TCP em listening com processo
sudo netstat -tlnp

# Tudo (TCP + UDP)
sudo netstat -atunp

# Ver tabela de rotas
netstat -rn

# Estatísticas por interface (eth0, wlan0...)
netstat -i

# Monitorar em tempo real
sudo netstat -c

# Filtrar por porta
sudo netstat -tlnp | grep :5432

### Lendo a saída
Proto  Recv-Q  Send-Q  Local Address     Foreign Address   State     PID/Program
tcp    0       0       0.0.0.0:22        0.0.0.0:*         LISTEN    1234/sshd
tcp    0       0       192.168.1.10:22   192.168.1.5:51234 ESTABLISHED 1235/sshd
````

---
### `netstat` vs `ss` — quando usar cada um?

|Situação|Use|
|---|---|
|Sistema moderno (seu caso)|**`ss`** — mais rápido e preciso|
|Scripts legados / compatibilidade|`netstat`|
|Ver tabela de rotas|`netstat -rn` ou `ip route`|
|Ver interfaces de rede|`netstat -i` ou `ip -s link`|

---
### Alternativas modernas equivalentes
```bash
netstat -tlnp   →   ss -tlnp
netstat -rn     →   ip route
netstat -i      →   ip -s link
```