---
aliases:
  - Load Balance
  - Balanceamento de Carga
  - load balancing
  - Load Balancer
tags:
  - web
---
### **Sobre**

Serviço que distribui tráfego web entre vários servidores, aumentando a escalabilidade, velocidade e confiabilidade da aplicação.

Ele atua como um "gerente de tráfego" inteligente, podendo processar várias  conexões simultâneas e direcionando as requisições para o servidor menos ocupado, evitando sobrecargas

Normalmente fica rodando na [[Porta 80]]

![[Exemplo Load Balancing.png]]

---
### **Tipos de balanceamento**:
Existem tipos de balanceamento, mas os mais comuns são:
- **Round Robin**
	 'mais simples', distribui as requisições entre os servidores de forma 'circular', ou seja, *a primeira requisição vai para o servidor 1, depois para o 2 e assim por diante*
	
- **Least Connections**:
	 Distribui as requisições as requisições analisando o números de conexões ativas em cada servidor, ou seja, *se o servidor 1 tem 10 conexões ativas e o servidor 2 tem 5, a próxima vai para o servidor 2*
	
- **Least Reponse Time**:
	  Realiza o direcionamento de acordo com o tempo de resposta, ou seja, *se o servidor 1 tem um tempo de 100ms e o servidor 2 tem 50ms, será direcionado para o servidor 2*
	
- **Hash**:
	 Segue um 'padrão' do hash gerado da requisição, exemplo, *se foi configurado para analisar o TOKEN, o valor HASH dele será sempre o mesmo e a requisição vai para o mesmo servidor*.
	
- **IP Hash**:
	 Assim como o anterior, é definido um 'padrão', dessa vez do IP do cliente, ou seja, *todas as requisições que vierem do mesmo IP, vão para o mesmo servidor.*
---

### **Serviços de Balanceamento de carga**
Existem vários, mas o mais conhecidos são:
- [[Nginx]]
- [[HAProxy]]
- [[Apache]]
- [[Elastic Load Balancing|AWS Elastic Load Balancer]]
- [[Google Cloud Load Balancing]]
- [[Azure Load Balancer]]
---
#### Fonte
https://medium.com/@sschonss/load-balancer-50398b45d227