---
aliases:
  - proxychains-ng
---
O Proxychains4 (ou proxychains-ng) é uma ferramenta de [[Linha de comando]] para sistemas [[Unix]]|[[Linux]] que força a conexão [[TCP]] de um programa a passar por servidores [[Proxy]], como [[SOCKS4]], [[SOCKS5]] ou [[HTTP (Hypertext Transfer Protocol)|HTTP]]

O arquivo de configuração principal fica em `1/etc/proxychains4.conf`.
Edite o arquivo para definir o modo de encadeamento (*strict_chain, dynamic_chain ou random_chain*).

Adicione os seus servidores proxy na seção [ProxyList] no final do arquivo informando o tipo, o [[IP]] e a porta.