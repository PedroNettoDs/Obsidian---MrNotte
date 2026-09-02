---
aliases:
  - Protocolo de Configuração Dinâmica de Host
  - Dynamic Host Configuration Protocol
Camada OSI: 7 - Aplicação
---
**DHCP** é **Dynamic Host Configuration Protocol** traduzindo **Protocolo de Configuração Dinâmica de Host**, ele é responsável por distribuir as *configurações de rede*: 
- LAN
	- [[IP]]
	- [[Máscara]]
- WAN
	- IP (Dispositivo de redes)
	- Máscara (Rede e Host)
	- [[Gateway]]
	- [[DNS]]

Sendo de três maneiras de configurações do lado do Servidor:
- Aleatório, podemos definir um range de quais IPs pode ser? (entre 192.168.0.100 à 192.168.0.200)
- Preferencial: Marque a máquina X, tem PREFERENCIA a um endereço, mas se não tiver disponível, agregue outro
- Fixo: informa qual o IP será dado para o Mac.

Quando a máquina ciente liga, ele faz um [[broadcast]]

REGRA DA VIDA, TODO SERVIÇO DE REDE, QUE PRECISA SER ENCONTRADO, NECESSARIAMENTE PRECISA TER IP FIXO.
As configurações de FIXO precisa ser para SERVIDOR, BANCO DE DADOS, IMPRESSORA.
DHCP AUTOMATICO, somente nas máquinas HOSTs.



https://www.fortinet.com/br/resources/cyberglossary/dynamic-host-configuration-protocol-dhcp


[[APIPA]]

```ini
ddns-update-style none;
option domain-name "fatec";
option domain-name-servers 192.168.0.1
```

Reservando o endereço IP fixo pelo endereçamento MAC