---
aliases:
  - AWS Elastic Load Balancer
---
[[Load Balancer|Load Balancer]] da [[Amazon Web Services (AWS)|AWS]]

**Elastic Load Balancing** é um serviço que distribui o tráfego de uma aplicação entre várias instâncias do [[EC2 - Elastic Compute Cloud|EC2]].

Ele recebe o tráfego web e direcionada de forma 'proporcional' para o 'balanceador de carga' entre as instâncias, evitando sobrecarregamento em uma só.

Embora sejam serviços diferentes, o **Elastic Load Balancing** e o Amazon [^1]**EC2 Auto Scaling** trabalham juntos para garantir que as aplicações tenham bom desempenho e alta disponibilidade.

![[Exemplo Load Balancing.png]]
## **Alta demanda**
à medida que o número de visitantes de um site aumenta, o site ativa mais instâncias do Amazon EC2 para atendê-los.
Ai que entra o [[Load Balancer|Balanceamento de Carga]], direcionado as solicitações dos usuários para as instâncias disponíveis, garantindo que a carga seja distribuída uniformemente entre elas..

## **Baixa demanda**
Diante da diminuição do tráfego, por não ser mais necessário é muitas das vezes reduzida ou encerrada a instância.

![[Elastic Load Balancing.canvas]]

---

[^1]: **Amazon EC2 Auto Scaling** 
	O Amazon EC2 Auto Scaling ajusta automaticamente a quantidade de instâncias EC2 conforme a demanda da aplicação aumenta ou diminui, garantindo maior disponibilidade. 
	Ele funciona como uma cafeteria que adiciona mais baristas quando há mais clientes, evitando longas esperas.
	Se o tráfego aumenta:
	- Ele cria novas instâncias.
	Se o tráfego diminui:
	- Ele encerra instâncias ociosas.
	
