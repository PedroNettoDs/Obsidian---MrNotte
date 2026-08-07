https://github.com/ddclient/ddclient
### Sobre:
um software em [[Perl]], projetado para atualizar automaticamente registros de [[DNS Dinâmico (DDNS)]], ou seja, se o seu IP de rede mudar, ele registra a mudança.

Existem integrações com [[Cloudflare]], Google Domanins e Namecheap.

Permite com que 'servidores domésticos' permaneçam acessíveis.

---
### Configuração
sua configuração fica inteiramente dentro do `ddclient.conf`, aonde é definido: Protocolos, Credenciais e métodos para detectar o IP

---

- **DDClient como “ponte”**:
    
    - O **DDClient** (ou `ddclient`) é configurado para:
        - Verificar seu IP público (via API do DuckDNS).
        - Atualizar o registro do domínio `nettotech.duckdns.org` com o novo IP.
    - **O domínio não precisa ser modificado**: apenas precisa estar associado ao DuckDNS.
---

**Melhor para**: Usos técnicos, integração com servidores e controle total.  
**Prós**:

- **Ferramenta open-source**: 100% livre e gratuita.
- **Suporta múltiplos serviços**: Pode ser configurado para trabalhar com **No-IP**, **DuckDNS**, **DynDNS**, etc.
- **Personalização total**: Permite definir regras de atualização, frequência e até scripts personalizados.
- **Ideal para servidores**: Perfeito para quem gerencia servidores locais ou em nuvem.

**Contras**:

- **Requer configuração manual**: Não é tão intuitivo para usuários que não têm experiência com scripts ou servidores.
- **Depende de um servidor**: Precisa de um servidor ou script para rodar o `ddclient`.
- **Não é uma solução “turn-key”**: Requer mais trabalho de configuração.

**Recomendação**: Se quiser **total controle e personalização**, DDClient é a melhor escolha, mas exige mais conhecimento técnico.
