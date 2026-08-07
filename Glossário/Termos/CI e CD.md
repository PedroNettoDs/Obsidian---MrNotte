---
aliases:
  - Integração Contínua
  - Continuous Integration
  - CI/CD
  - Entrega Contínua
  - Continuous Delivery
  - Implantação Contínua
  - Continuous Deployment
  - Integração e Entrega Contínua (CI/CD)
---
### O que é 'CI/CD'?
CI/CD é a sigla para **Integração Contínua (Continuous Integration)** e **Entrega Contínua (Continuous Delivery)** ou **Implantação Contínua (Continuous Deployment)**.

![[CI e CD1.png|600]]
É uma abordagem para **automatizar e acelerar o ciclo de desenvolvimento de software**, garantindo mais qualidade e menos dor de cabeça no deploy.

- **Integração contínua (CI)**
	É a prática de:
	- Integrar mudanças de código **com frequência** (várias vezes ao dia)
	- Automatizar:
	    - Build
	    - Testes
	    - Validações
	        
	Ou seja:  
	Sempre que alguém faz [[commit]], o sistema testa automaticamente.
	
	**Objetivo**: detectar erros cedo.
	**CI NÃO significa enviar para produção automaticamente.**
	
- **Entrega Contínua (Continuous Delivery)**
	Entrega contínua significa que:
	- O código já passou por build e testes automatizados
	- Ele está **sempre pronto para ir para produção**
	- Mas o [[Deploy]] final pode exigir uma aprovação manual
	
- **Implantação Contínua (Continuous Deployment)**
	Aqui temos:
	- [[Deploy]] automático em produção
	- Sem aprovação manual
	- Toda mudança que passa nos testes vai direto para produção

### Resumo
- **CI** → Automatiza integração e testes
- **Continuous Delivery** → Código sempre pronto para produção (deploy manual)
- **Continuous Deployment** → Deploy automático em produção

---

O [[Pipelines]] da CI/CD é essencial para um profissional de [[DevOps]]

---
Fonte:
https://www.redhat.com/pt-br/topics/devops/what-is-ci-cd