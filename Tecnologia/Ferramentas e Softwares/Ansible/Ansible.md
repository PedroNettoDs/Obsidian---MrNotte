---
aliases:
  - Ansible
---
### Sobre
Bom, buscando mais sobre, compreendi que inicialmente era um termo sci-fi (???), que se referia a um dispositivo que realizava interconexões intergaláticas, superando a velocidade da Luz :D , a palavra é vinda contração da palavra '*answerable*' 
>buscar mais sobre obras da autora: *Ursula K. Le Guin*, parece ser legal ler

Entretanto, Ansible para mim, rapazinho entusiasmado em TI é uma Ferramenta [[Código aberto]], criado pela [[RedHat]].

Sendo uma ferramenta '[^1]Agentless', o que siginfiica que para configurar e implantar aplicações e sistemas, não requer instalação de nenhum software ou "[[Daemon|daemon]]";

Conectando temporariamente via [[SSH]] (Em sistemas [[Linux]]/[[GNU]]) e [[WinRM]] (em [[Windows]])
	![[Ansible.png]]

---

![[1 - Componentes]]
---
## Red Hat Ansible Automation Platform (AAP)
Estudar mais sobre..

---
## Questões
1. Qual porta TCP é utilizada por padrão para a comunicação do '*Receptor*', dentro da malha de automação?
	**R:** 27199
> Porta padrão configurável, utilizada para conexões [[P2P|peer-to-peer]], entre nós na arquitetura de malha de automação


- `role` 
  é uma função (instalar base, configurar samba)
- `heandlers` 
  são disparados caso a estrutura seja modificada 

[^1]:  (sem Agentes), o que siginfiica que para configurar e implantar aplicações e sistemas, não requer instalação de nenhum software ou "[[Daemon|daemon]]";
