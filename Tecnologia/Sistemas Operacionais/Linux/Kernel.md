### Sobre
**kernel** (núcleo) é a parte central e fundamental de um [[Sistema Operacional]].

Atuando como uma **ponte entre o [[Software]]** (aplicativos) **e o [[Hardware]]** (processador, memória, dispositivos) de um computador.

Gerenciando recursos, controlando processos e permitindo a comunicação entre eles para que tudo funcione de forma eficiente e segura. 

Ele gerencia o acesso à [[CPU]], memória [[RAM]], armazenamento e periféricos, e é responsável por tarefas como inicialização, escalonamento de processos e segurança, sendo o "cérebro" que faz o sistema operacional operar. 

![[Kernel.png|500]]
Desenvolvido inicialmente por **Linus Torvalds**, sendo esse projeto hoje, sustentado por centenas de pessoas ao redor do mundo, sobre o controle de versionamento do criador.

Adotando uma tecnologia de kernel [[Aplicações monolíticas e microsserviços|monolítico]], ou seja, um único bloco compilado de todos os serviços.

O usuário interage com o kernel através do [[Shell]].

---
### Subsistemas
O kernel é composto por **subsistemas**, cada um responsável por implementar funções do sistema operacional:

- **Process Management (PM)**
	Controla o acesso dos processos ao **Processador ([[CPU]])**
- **Memory Management (MM)**
	Controla o acesso dos processos à memória
- **Virtual File System (VFS)**
	Fornece uma interface para os dados armazenados nos dispositivos de hardware
- **Networking Layer (NL)**
	Permite a conexão com outros dispositivos da rede
- **Interprocess Communications (IPC)**
	Controla a comunicação entre os processos

![[Kernel - Subsistemas.png]]

---



https://guialinux.uniriotec.br/kernel/