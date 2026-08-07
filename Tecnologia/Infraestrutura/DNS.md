---
aliases:
  - DNS
  - Domain Name System
  - Sistema de Nomes de Domínio
---
#Protocolos

DNS (*Domain Name System, ou Sistema de Nomes de Domínio*) é a "lista telefônica da internet", convertendo nomes de sites legíveis exemplo 'google.com' em endereços [[IP]].

Até por que, é mais fácil decorarmos o nome do site, do que o seu endereço.

Sendo usado para computadores acharem aonde precisam se conectar

Ele facilita a navegação, eliminando a necessidade de memorizar sequências numéricas complexas. 

**Pontos-chave sobre o DNS:** 
- **Funcionalidade:** Traduz nomes de domínio em endereços IP, permitindo que navegadores carreguem recursos da internet.
- **Importância:** Sem o DNS, seria necessário digitar o endereço IP numérico de cada site para acessá-lo.
- **Funcionamento:**
    
    - Quando um domínio é digitado, o servidor DNS procura o registro correspondente para encontrar o endereço IP correto
	
	- **Segurança e Ameaças:** Vulnerabilidades no servidor DNS podem ser exploradas por ataques como spoofing e envenenamento de cache, que desviam o tráfego para sites falsos.
	
	- **Componentes:** Inclui servidores de nomes autoritativos, resolvers e registros de DNS. 
O sistema funciona de forma hierárquica e distribuída, utilizando servidores de nomes (como TLD e raiz) para gerenciar a vasta rede de domínios.