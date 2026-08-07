---
dg-publish: true
---
#### Nota pessoal
Ao pesquisar, sobre formas de barrar meu vício, cheguei a conclusão que estava na hora de aprender mexer no [Firewall](), já havia ouvido falar sobre o [[Cloudflare]] Family (utilizo muito o [[DNS]]: 1.1.1.1 para poder entrar em sites de [[Torrent]])

---
## DNS Filtrado
Bloqueia pornografia por domínio (essencial)

Utilizei o DNS Público:
- 1.1.1.3
- 1.0.0.3

Assim como informado no blog da Cloudflare, bloqueia pornografia + malware.
https://blog.cloudflare.com/introducing-1-1-1-1-for-families/

### Configuração

1) Procurar o nome da conexão através do [[nmcli]]
```bash
nmcli connection show
```
	
2) Desativar o DNS automático do provedor:
```bash
sudo nmcli connection modify "Conexão cabeada 1" ipv4.ignore-auto-dns yes
```
	
3) Definir DNS com filtro
```bash
sudo nmcli connection modify "Conexão cabeada 1" ipv4.dns "1.1.1.3 1.0.0.3"
```
	
4) Reativar a conexão
```bash
sudo nmcli connection down "Conexão cabeada 1"
sudo nmcli connection up "Conexão cabeada 1"
```

> Observação: desativei o IPv6 da máquina.

#### Conferindo configuração:
```bash
nmcli dev show enp4s0 | grep DNS
```

Você deve ver algo como:
```less
IP4.DNS[1]: 1.1.1.3
IP4.DNS[2]: 1.0.0.3
```

---
### [[Firewall]] - [[Uncomplicated Firewall (UFW)]]

1) Ativando o UFW
```bash
sudo ufw enable
sudo ufw default deny incoming
sudo ufw default allow outgoing
```
	
2)  Liberar DNS permitido
```bash
sudo ufw allow out to 1.1.1.3 port 53
sudo ufw allow out to 1.0.0.3 port 53
```
	
3) Bloqueando DNS externo
```bash
sudo ufw deny out 53
```

> Observação: é necessário realizar nessa ordem, para que só negue o 53 após permitir o 1.1.1.3 e 1.0.0.3
#### Conferindo configurações
```
sudo ufw status numbered
```

Você deve ver algo como:
```
Estado: ativo  
  
    Para                       Ação        De  
    ----                       ----        --  
[ 1] 1.1.1.3 53                 ALLOW OUT   Anywhere                   (out)  
[ 2] 1.0.0.3 53                 ALLOW OUT   Anywhere                   (out)  
[ 3] 53                         DENY OUT    Anywhere                   (out)  
[ 4] 53 (v6)                    DENY OUT    Anywhere (v6)              (out)
```