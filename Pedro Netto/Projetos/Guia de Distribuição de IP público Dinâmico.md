---
Blogspot: https://nettotecnologias.blogspot.com/2026/07/guia-de-distribuicao-de-ip-publico.html
---
### **Usar um serviço de DNS Dinâmico (DDNS)**

- **Ferramentas**: [[ddclient]], [[No-IP]], [[DuckDNS]], ou serviços como **[[Cloudflare]]** (com integração de DNS dinâmico).
- **Funcionamento**: O serviço monitora seu IP público e atualiza automaticamente o registro [[DNS]], garantindo que o domínio aponte para seu IP atual.
- **Exemplo**:  
    Se você usa **DuckDNS**, configura um domínio (ex: `meudominio.duckdns.org`) e o serviço mantém seu IP atualizado.  
    **Vantagem**: Simplicidade e baixa complexidade.

---

### **Configurar um Proxy Reverso (ex: [[Nginx]] ou Apache)**

- **Objetivo**: Redirecionar tráfego para seu IP público (ex: para um servidor local).
- **Passos**:
    
    1. Instale o Nginx no servidor.
    2. Configure um arquivo de configuração (ex: `/etc/nginx/sites-available/meuservidor.conf`) com instruções para encaminhar requisições para seu IP público.
    3. Use `upstream` para definir o IP do servidor local.  
        **Exemplo**:
    
```nginx
upstream backend {
    server 192.168.1.100;  # IP do servidor local
}

server {
    listen 80;
    server_name meudominio.duckdns.org;

    location / {
        proxy_pass http://backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```
    
**Vantagem**: Flexibilidade para encaminhar tráfego para múltiplos servidores ou aplicativos.

---

### **Usar [[SSH Tunneling]] para Exposição de Serviços**

- **Ferramenta**: `ssh -R` (para criar um túnel reverso).
- **Funcionamento**: Redireciona tráfego do servidor remoto para seu IP público.  
    **Exemplo**:  
    Se você tem acesso a um servidor remoto (ex: `servidorremoto.com`), execute:
    
```bash
ssh -R 80:localhost:80 usuario@servidorremoto.com
```
    
Isso faz com que o tráfego na porta 80 do servidor remoto seja encaminhado para sua máquina local (via SSH).  
    **Vantagem**: Segurança, pois o tráfego é criptografado.

---

### **Configurar Port Forwarding no Router**

- **Passos**:
    1. Acesse o painel do seu roteador (ex: `192.168.1.1`).
    2. Configure o **Port Forwarding** para encaminhar tráfego de portas específicas (ex: 80, 443) para a máquina local (ex: `192.168.1.100`).
    3. Combine com um serviço DDNS para acessar seu IP público via domínio.  
        **Vantagem**: Permite acesso direto ao servidor local, mas exige cuidado com a segurança (ex: desativar portas não necessárias).
---
### **Lembre-se: Segurança é Prioritária**

- **Use SSL/TLS**: Certificados gratuitos (ex: Let’s Encrypt) para proteger conexões.
- **Bloqueie portas desnecessárias**: Evite expor servidores sensíveis a tráfego externo.
- **Monitore o tráfego**: Ferramentas como `fail2ban` podem bloquear tentativas de ataque.