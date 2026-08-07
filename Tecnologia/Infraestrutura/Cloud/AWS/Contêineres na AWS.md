[[Contêineres]] na [[Amazon Web Services (AWS)|AWS]]

Esse serviço, oferecem a gestão completa dos contêiners, possibilitando empacotar 'códigos, aplicações, bibliotecas e variáveis de ambiente'
Garantindo que a aplicação possa ser 'replicada' e funcional em todos os ambientes.
Existindo controles de acessos e limitando acessos entre aplicações.

---

## Um host com vários contêineres
Quando múltiplos contêineres são executados em um único host:
- Cada aplicação roda iso]ladamente.
- O ambiente permanece consistente.
- Evita-se o problema clássico de “funciona na minha máquina”.
    
Isso elimina diferenças entre o ambiente do desenvolvedor e o ambiente de produção, reduzindo falhas causadas por incompatibilidades de versão ou configuração.

---

## Dezenas de hosts com centenas de contêineres
Em ambientes de larga escala, com múltiplos servidores e centenas ou milhares de contêineres, o gerenciamento manual se torna inviável.

É necessário controlar:
- Uso de CPU e memória
- Segurança
- Rede
- Logs
- Escalabilidade
- Alta disponibilidade
	
Para resolver essa complexidade, utilizam-se ferramentas de **orquestração de contêineres**.