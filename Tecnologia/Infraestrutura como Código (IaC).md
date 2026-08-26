---
aliases:
  - IaC
  - Infraestrutura como Código
---
### Resumo

Forma de gerir Servidores, Redes e Bancos de dados, através de arquivos de configurações em vez de processos manuais.

Sendo uma habilidade do cargo de [[DevOps]], que faz com que seja mais fácil replicar ambientes para escalabilidade e autonomizável.

#### Ferramentas:
- [[Terraform]]
* [[Pulumi]]
- [[AWS CloudFormation]]
- Chef
- Puppet
- [[Azure Resource Manager (ARM)]]

---
### Conceitos

> Gerenciamento e provisionamento de recursos de infraestrutura de computação por meio de um arquivo de configuração

Portanto, assim como o nome diz, trata a infraestrutura como um software. :D

- Sendo possível versionar com [[Git]], 
- Garante a [[Idempotência]] e [[Imutabilidade]]
	- Idempotência: não mudará o resultado da criação
	- Imutabildiade: substituição total do serviço, evitando modificações.

Sendo possível seguir com duas abordagens:
- **Declarativa**: pontuando '*o quê*' e a ferramenta, determina os passos ([[Terraform]])
- **Imperativa**: pontuando "*como*", definindo os passos da ferramenta ([[Ansible]])

---
### Linguagens

Para estruturar o código da infraestrutura, os modelos mais adotados seriam:
- [[YAML]]
- [[JSON]]
-  [[HCL]] ([[Terraform]]).

Ferramentas como: [[Pulumi]], permitem a reutilização de linguagens comuns (*Python, TypeScript, Go*).

---
### Práticas recomendadas
- **Automação via [[CI e CD|CI/CD]]**
	Integrar pipelines automatizadas para garantir testes e validações antes da aplicação das mudanças
- **Evitar mudanças manuais**
	Uma vez implantado, qualquer ajuste deve ser feito no código e não manualmente!, para garantir isso, necessário utilizar ferramentas de '**Detecção de desvio (Drift detection**', que alertam sobre alterações fora do template.
- **Monitoramento e Auditoria**
	Necessário manter logs contínuos de toda mudança nos templantes e nos recursos
- **[[Política como Código (PaC)|Política como Código]]**
	Avaliações de segurança validadas no ato de pipelines
	