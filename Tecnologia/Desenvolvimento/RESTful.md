RESTful descreve uma [[API - Interface de Programação de Aplicações]] que segue os princípios do estilo arquitetural [[REST - Representational State Transfer]], utilizando [[HTTP (Hypertext Transfer Protocol)|HTTP]] para comunicação, com foco em recursos, comunicação sem estado (stateless), interface uniforme, e sendo independente de cliente e servidor para troca de informações eficientes. 

Essencialmente, uma API é RESTful quando adere rigorosamente às diretrizes REST, permitindo que diferentes sistemas se comuniquem de forma padronizada, como em logins de redes sociais,.
Princípios-chave de uma API RESTful:

- **Cliente-Servidor**: Separação clara entre cliente (interface) e servidor (dados e lógica).
- **Stateless** (Sem Estado): Cada requisição do cliente ao servidor deve conter toda a informação necessária; o servidor não armazena o estado da sessão.
- **Cacheable** (Armazenável em Cache): Respostas podem ser cacheadas para melhorar desempenho.
- **Interface Uniforme**: Uso de HTTP verbs (GET, POST, PUT, DELETE) e URIs para identificar e manipular recursos de forma consistente.
- **Camadas (Layered System):** A arquitetura pode ser composta por múltiplas camadas, sem que o cliente saiba.
- **HATEOAS (Hypermedia as the Engine of Application State):** A API fornece links (hipertexto) para que o cliente descubra mais ações e recursos dinamicamente. 

Em resumo:
REST é o estilo arquitetural, enquanto RESTful indica que uma API segue fielmente todas as regras desse estilo, tornando-a robusta, escalável e eficiente para a integração de sistemas modernos, como em microserviços e aplicações web e mobile.