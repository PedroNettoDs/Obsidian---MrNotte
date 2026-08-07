---
aliases:
  - Elastic Compute Cloud
  - EC2
tags:
  - Cloud
---
(observação o 2, é por conta dos dois Cʼs)

Compreendendo que esse serviço se consiste na alocação de
uma [[Máquinas virtuais (VMs)|Máquina Virtual]], podemos segregar esse serviços em
diversos tipos para determinadas funções, priorizando o uso
eficiente e econômico para cada usuário, sendo que nessa
separação, há outras separações, partiu ver?

https://aws.amazon.com/pt/ec2/instance-types/

## **Tipos de estâncias**
Há certos tipos de EC2, elas são bem claras para que serve cada uma, porém vale destacar elas:

- **Otimizadas para computação**: 
	Indicadas para aplicações que exigem alto poder de processamento, como processamento em lote, servidores web de alto desempenho, jogos, modelagem científica e inferência de [[Machine Learning|Machine Learning]].
    
- **Otimizadas para memória**: 
	Ideais para trabalhar com grandes volumes de dados que precisam ficar na memória para acesso rápido, como [[Banco de dados|bancos de dados]] e aplicações analíticas.
    
- **Computação acelerada**: 
	Utilizam [[Hardware|Hardware]] especializado (como GPUs e outros aceleradores) para executar tarefas complexas mais rapidamente, como cálculos matemáticos, processamento de imagens e análise de grandes volumes de dados.
		(Obs: [[LLM|LLM]] pode funcionar bem aqui)
    
- **Otimizadas para armazenamento**
	Focadas em alta velocidade de leitura e gravação de dados locais, sendo adequadas para grandes conjuntos de dados e aplicações com muitas operações de I/O.
    
- **Otimizadas para HPC**
	Projetadas para computação de alta performance em larga escala, ideais para simulações complexas, pesquisas científicas e workloads intensivos como aprendizado profundo.
	
	As instâncias de computação de alta performance ([[HPC]]) são projetadas para oferecer a melhor relação custo-benefício para workloads de HPC em grande escala na AWS. 
	São ideais para aplicações que exigem [[CPU|Processador]]es potentes, como simulações complexas e aprendizado profundo.

![[TIpos de Instâncias.canvas]]

---
## **Definição de preço no EC2**
>Entendendo que o lema da AWS é 'Você só paga pelo o que usar', fica mais fácil compreender que o EC2 é como poder alugar por hora, fazer um plano mensal, pegar desconto por fidelidade ou ganhar um super desconto com algo no marketplace do facebook.

- **Sob demanda**
	Instâncias sob demanda não exigem compromisso de longo prazo nem pagamento antecipado. O cliente paga apenas pelo utilizado.
	
	Perfeito para:
	- Projetos curtos    
	- Testes
	- Sistemas que não sabe quanto vão usar    
	*Exemplo:*
		Está elaborando um projeto e não sabe ainda o nível de escalabilidade, então, sem um compromisso de 'pagar por um servidor muito forte e não usar nada', porém é bom para medir a necessidade de algo 'fixo'
		
- **Instâncias reservadas**
	Semelhante a um contrato de locação, aonde pode ser oferecido desconto em conforme o tempo do compromisso.
	
	Aqui você diz:
		“Vou usar esse tipo de instância, nessa região, por 1 ou 3 anos.”
	Em troca disso, a AWS dá desconto.
		
	Existem dois tipos:
	- **Standard Reserved Instances**
		Você escolhe exatamente:
		- Família e tamanho da instância
		- Plataforma (ex: Linux ou Windows)
		- Tenancy
		- [^1]Região
		- Opcionalmente, [[Região e Zonas de Disponibilidade|Região e Zonas de Disponibilidade]]
		
		É como fechar contrato de aluguel de 3 anos:  
		Você paga menos por mês, mas assume compromisso.
		Quanto maior o tempo (3 anos), maior o desconto.
		
	- **Instâncias reservadas conversíveis**
		Você ainda fecha contrato…  porém permite alterar:
		- Tipo de instância
		- Família
		- [^1]Região (em alguns casos)
		    
		Oferecem maior flexibilidade, porém com desconto menor em comparação às Standard Reserved Instances.
		
		São adequadas para ambientes em que se espera evolução da arquitetura ao longo do tempo.
		
-  **Savings Plans**
	*tipo plano de fidelidade*
	Diferentemente das instâncias reservadas, o compromisso não está necessariamente atrelado a um tipo específico de instância, mas a um valor mínimo de consumo por hora.
	
	Tipo:
		AWS, vou gastar pelo menos X dólares por hora por 1 ou 3 anos.”
	Em troca, ganha desconto (até 72% comparado ao sob demanda).
	
	Obs: É como plano de celular:  
	Você se compromete com um valor mensal e paga menos por minuto usado.
	
	É ótimo para quem:
	- Ambientes com uso contínuo
	- Quer desconto
	- Organizações que precisam de flexibilidade para alterar tipos e tamanhos de instância
	    
	Se passar do valor combinado, paga o excedente como sob demanda.
		
-  **Instâncias Spot** 
	(tipo pagar barato por um produto prestes a estragar no mercado Pão de Açucar, não me pergunte como eu sei..) há relatos que há descontos de até 90%.
	
	Mas tem um detalhe importante:
	Pode ser interrompida a qualquer momento.
	A AWS usa capacidade ociosa e oferece barato.  
	Se precisar da máquina de volta… ela tira de você.
	
	Exemplo:  
		É como ir na casa de um amigo para passar o ano novo enchendo a cara e de repente os pais dele chegam, você precisa sair para eles dormirem, não me pergunte novamente como eu sei.
	
	Boa para:
	- Processamento em lote
	- Treinamento de modelos
	- Tarefas que podem reiniciar
	    
	Ruim para:
	- Produção crítica
	- Sistemas que não podem parar
		
- **Hosts Dedicados** 
	Aqui você não divide o servidor físico com ninguém, É 100% seu.
	Hosts dedicados são servidores físicos exclusivos para um único cliente.
	
	Ideal para:
	- Empresas que precisam usar suas próprias licenças
	- Exigências de compliance
	- Controle total de hardware
	
	Podem ser contratados sob demanda ou com reserva, mas já aviso:  
	É a opção mais cara do EC2 💸.

![[Definição de preço.canvas]]

---
## **Scaling do Amazon EC2**
Vamos supor que você começou a infraestrutura com tudo que era necessário para funcionar, entretanto, seu SaaS bombou na net e tem +1.000 pessoas conectadas.
Com isso o você pode aumentar os recursos de hardware do seu servidor para comportar, ai vamos supor, deu a noite e o pessoal parou de usar, agora só tem 100 pessoas conectadas, você diminuí os recursos.

Existem duas maneiras de lidar com o aumento da demanda:  
- **aumentar verticalmente** (scale up)
	dar mais potência a uma máquina;  
	- Mais CPU.  
	- Mais memória.  
	- Mais capacidade.
	
	Funciona bem até certo ponto. Mas há limites:
	- Existe um teto físico para o tamanho da instância.
	- Se a máquina falhar, tudo para.
		
-  **aumentar a quantidade** (scale out) 
	Em vez de deixar uma máquina mais forte, você adiciona mais máquinas.
	Embora aumentar a potência funcione às vezes, não resolve tudo.  
	- Distribui a carga entre várias instâncias.
	- Ganha resiliência.
	- Reduz ponto único de falha.
	Esse modelo é a base da maioria das arquiteturas modernas em nuvem.

![[Escalabilidade.canvas]]
### **Amazon EC2 Auto Scaling** 
O Amazon EC2 Auto Scaling ajusta automaticamente a quantidade de instâncias EC2 conforme a demanda da aplicação aumenta ou diminui, garantindo maior disponibilidade. 
Ele funciona como uma cafeteria que adiciona mais baristas quando há mais clientes, evitando longas esperas.

Se o tráfego aumenta:
- Ele cria novas instâncias.
Se o tráfego diminui:
- Ele encerra instâncias ociosas.


Existem duas abordagens no Auto Scaling:
- **Scaling dinâmico**: 
	Reage a métricas em tempo real.
	Exemplos de métricas comuns:
	- Uso de CPU
	- Número de requisições
	- Latência
	- Métricas customizadas
	    
	Se a CPU ultrapassar, por exemplo, 70% por alguns minutos, novas instâncias são adicionadas.  
	Se cair consistentemente, instâncias são removidas.

- **Scaling preditivo**: 
	ajusta o número de instâncias com base em previsões de demanda futura, antecipando a necessidade de mais ou menos recursos.
	
	Se sua aplicação sempre tem pico às 20h:
	- O Auto Scaling já aumenta a capacidade antes das 20h.
	    
	É útil para ambientes com uso contínuo e comportamento previsível, como:
	- E-commerces com horários de pico
	- Sistemas corporativos com carga comercial
    
- Plataformas educacionais com horários fixos
> Para dimensionar mais rapidamente, você pode combinar o scaling dinâmico e preditivo.

[^1]:  **Região e Zona de Disponibilidade**
	Uma Região é composta por três ou mais [[Região e Zonas de Disponibilidade|Região e Zonas de Disponibilidade]] (AZs).
	
	Por exemplo, a Região América do Sul (São Paulo) é identificada como `sa-east-1` e possui as zonas:
	
	- `sa-east-1a`
	- `sa-east-1b`
	- `sa-east-1c`
	
	A escolha da região e, em alguns casos, da zona específica, impacta disponibilidade, latência e custos.
