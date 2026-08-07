---
tags:
  - Cloud
---
DevOps é uma **cultura profissional**, que tem como objetivo:
Integrar e automatizar os processos entre as equipes de: **Desenvolvimento de Software (Dev)** e de **Operações de TI (Ops)**.

O termo surgiu em 2009 por Patrick Debois, que estava enfrentando dificuldades entre a colaboração entre essas áreas, logo o DevOps deve ser focado em 'comunicação, colaboração e [[CI e CD|Integração Contínua]]'

![[DevOps1.png]]

### O que um **DevOps** faz?
 Estabelece um ambiente onde a construção, teste e 'liberação do software', ocorra de forma rápida, frequente e confiável;
 Suas funções incluem:
 - **Redução do Ciclo de Desenvolvimento**:
	Encurta o tempo entre o desenvolvimento para a produção (time-to-market)
- **Automação de Processos**:
	Automatiza tarefas repetitivas e fluxos para evitar erros (exemplo: no Django, ter que rodar `python manage.py migrate`)
- **Melhoria da qualidade**:
	Utiliza práticas como [[CI e CD|Integração Contínua]] (CI) e [[CI e CD|Entrega Contínua]] (CD) para garantir que o software seja testado e validado.
- **Estabilidade e Segurança**:
	Reduz a taxa de falhas em mudanças e melhora o tempo de recuperação em caso de incidentes
---
Para atuar como DevOps é necessário dominar a cadeia de ferramentas ([[toolchain]]):
- **Controle de versionamento** ([[Git]]):
	Utilizar [[GitHub]], [[GitLab]] e [[BitBucket]] para hospedar e colaborar.
	
- **Integração e Entrega Contínua ([[CI e CD|CI/CD]])**:
	Ferramentas que automatizam o pipeline de build e deploy como:
	[[Jenkins]], [[GitHub Actions]], [[GitLab CI]] e [[CircleCI]].
	
- **[[Contêineres]] e Orquestração de [[Docker]]**:
	Empacotar aplicações isolada e [[Kubernetes]]
	
- **Infraestrutura como Código ([[Infraestrutura como Código (IaC)|IaC]])**:
	Ferramentas que permitem gerenciar servidores via código, como:
	[[Terraform]], [[Ansible]], Pulumi e Crossplane.
	
- **Monitoramento e Observabilidade**:
	Para acompanhamento e avisos, ferramentas que se destacam:
	[[Prometheus]], [[Grafana]], [[Datadog]], [[New Relic]] e o [[ELK Stack]]
	
- **Segurança ([[DevSecOps]])**:
	Automação de testes de segurança:
	- **Análise de código**:  [[SonarQube]]
	- **Vulnerabilidades**: [[Trivy]] ou [[Snyk]] 
	- **Gestão de secret**: [[HashCorp Vault]]
	  
- **Testes Automatizados**:
	Ferramentas como [[Selenium]], [[Cypress]] e [[Playwright]] para simulação de uso real do sistema e garantir que não quebre

---
Fonte
https://community.revelo.com.br/introducao-ao-devops-conceitos-basicos-e-principios/