são conjuntos de computadores independentes conectados por rede que funcionam como uma única unidade coerente para o usuário final. 

Eles compartilham recursos, processos e dados entre nós ([[Hardware]] ou software) para aumentar o desempenho, escalabilidade e tolerância a falhas, superando limitações de uma máquina única. 

## Principais Características:
- **Concorrência**:
	Múltiplos componentes realizam tarefas simultaneamente.
* **Tolerância a Falhas**:
	O sistema continua operando mesmo se um dos computadores falhar.
- **Transparência**: 
	A complexidade da rede é escondida; o usuário percebe o sistema como um ambiente único e integrado.
- **Escalabilidade**: 
	Capacidade de aumentar recursos (nós) para lidar com cargas maiores. 

- **Web (WWW):** Acessa informações em servidores dispersos.
- **Computação em Nuvem ([[Cloud Computing]]):** [[Amazon Web Services (AWS)]], [[Azure]], [[Google Cloud]].
- **Bancos de Dados Distribuídos:** Armazenamento distribuído (ex: Apache Cassandra).
- **Sistemas de Arquivos Distribuídos:** HDFS (Hadoop). 

## **Desafios:**
- **Complexidade de Gerenciamento:** Coordenação entre múltiplos nós.
- **Consistência de Dados:** Garantir que todos os nós tenham os mesmos dados ao mesmo tempo.
- **Segurança:** Aumenta a superfície de ataque devido à rede. 

A arquitetura geralmente utiliza _[[middleware]]_ para viabilizar a comunicação e colaboração entre os componentes.