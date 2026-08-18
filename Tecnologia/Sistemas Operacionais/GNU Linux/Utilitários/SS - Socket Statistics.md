---
aliases:
  - ss
  - Socket Statistics
---
ferramenta moderna para **inspecionar conexões de rede e sockets** no [[Linux]]. Substitui o antigo [[netstat - Network Statistics]]

---
### Flags mais úteis

|Flag|Significado|
|---|---|
|`-t`|Conexões **TCP**|
|`-u`|Conexões **UDP**|
|`-l`|Apenas portas em **modo listening**|
|`-n`|Exibe **números** (sem resolver hostnames)|
|`-p`|Mostra o **processo** que usa a porta|
|`-a`|**Todas** as conexões (listening + estabelecidas)|
|`-4`|Apenas **IPv4**|
|`-6`|Apenas **IPv6**|
|`-s`|**Resumo estatístico** geral|

---

### Combinações mais usadas no dia a dia

bash

````bash
# Portas TCP abertas com processo
sudo ss -tlnp

# Tudo (TCP + UDP, todas as conexões)
sudo ss -atunp

# Ver se uma porta específica está em uso
ss -tlnp | grep :8080

# Conexões estabelecidas no momento
ss -tnp | grep ESTAB

# Resumo geral da rede
ss -s
```

---

### Lendo a saída
```
Netid  State    Recv-Q  Send-Q  Local Address:Port   Peer Address:Port  Process
tcp    LISTEN   0       128     0.0.0.0:22            0.0.0.0:*         sshd
tcp    ESTAB    0       0       192.168.1.10:22       192.168.1.5:54321  sshd
````

|Campo|O que é|
|---|---|
|`State`|`LISTEN` = aguardando conexão / `ESTAB` = conectado|
|`Local Address:Port`|IP e porta **do seu computador**|
|`Peer Address:Port`|IP e porta **do outro lado**|
|`Process`|Programa responsável|

---

### Dica para seus projetos

Quando um serviço **não sobe** ou dá erro de porta em uso:

bash

```bash
# Descobrir quem está ocupando a porta (ex: 3000)
sudo ss -tlnp | grep :3000

# Matar o processo pelo PID encontrado
kill -9 <PID>
```