---
aliases:
  - Filesystem Hierarchy Standard
  - FHS
---
É o padrão de [[Sistema de Arquivos]], sendo a estrutura de arquivos e diretórios utilizados pleo [[Linux]]

### /bin

---
### /dev
Local aonde fica representado arquivos referentes as [[Partição|partições]] do dispositivo, seguindo o seguinte padrão:
```bash
/dev/[tipo][ordem][partição]
```
- **Tipo**: `hd` ([[IDE]]) ou `sd` ([[USB - Universal Serial Bus|USB]], SATA, [[SCSI]])
- **Ordem**: Letras sequenciais (a, b, c ...)
- **Partição**: Número (1, 2 ..)
**Exemplo**:
```
/dev/sda   → primeiro disco SATA/USB
/dev/sda1  → primeira partição dele
/dev/sda2  → segunda partição
/dev/sdb   → segundo disco
```
---
### Estrutura de diretórios:

| Diretório        | Descrição                                                                                                                                                                                                                                                                                                   |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| /                | [Diretório raiz](https://pt.wikipedia.org/wiki/Diret%C3%B3rio_raiz "Diretório raiz") de toda a hierarquia do sistema de arquivos.                                                                                                                                                                           |
| /bin/            | Comandos [binários](https://pt.wikipedia.org/wiki/Execut%C3%A1vel "Executável") essenciais para todos os usuários (ex: [cat](https://pt.wikipedia.org/wiki/Cat_\(Unix\) "Cat (Unix)"), [ls](https://pt.wikipedia.org/wiki/Ls "Ls"), [cp](https://pt.wikipedia.org/wiki/Cp_\(Unix\) "Cp (Unix)"))            |
| /boot/           | Arquivos do [**Boot** loader](https://pt.wikipedia.org/wiki/Boot_loader "Boot loader") (ex: [núcleo](https://pt.wikipedia.org/wiki/N%C3%BAcleo_\(inform%C3%A1tica\) "Núcleo (informática)"), [initrd](https://pt.wikipedia.org/wiki/Initrd "Initrd")).                                                      |
| /dev/            | [Dispositivos](https://pt.wikipedia.org/wiki/Arquivo_de_dispositivo "Arquivo de dispositivo") (ex: [/dev/null](https://pt.wikipedia.org/wiki//dev/null "/dev/null")).                                                                                                                                       |
| /etc/            | Arquivos de configuração específicos do computador.                                                                                                                                                                                                                                                         |
| /etc/opt/        | Arquivos de configuração para o /opt/.                                                                                                                                                                                                                                                                      |
| /etc/X11/        | Arquivos de configuração para o [**X** Window System](https://pt.wikipedia.org/wiki/X_Window_System "X Window System"), versão **11**.                                                                                                                                                                      |
| /etc/sgml/       | Arquivos de configuração para **[SGML](https://pt.wikipedia.org/wiki/SGML "SGML")**.                                                                                                                                                                                                                        |
| /etc/xml/        | Arquivos de configuração para **[XML](https://pt.wikipedia.org/wiki/XML "XML")**.                                                                                                                                                                                                                           |
| /home/           | Diretórios de usuários.(Opcional)                                                                                                                                                                                                                                                                           |
| /lib/            | Diretório com as bibliotecas essenciais para os arquivos binários contidos nos diretórios /bin/ e /sbin/.                                                                                                                                                                                                   |
| /mnt/            | Sistemas de arquivos "[montados](https://pt.wikipedia.org/w/index.php?title=Mount_\(Unix\)&action=edit&redlink=1 "Mount (Unix) (página não existe)")" temporariamente.                                                                                                                                      |
| /media/          | Pontos de "montagem" para mídia removível, como [CD-ROMs](https://pt.wikipedia.org/wiki/CD-ROM "CD-ROM") (surgiram na versão 2.3 do FHS).                                                                                                                                                                   |
| /opt/            | Pacotes estáticos de aplicações.                                                                                                                                                                                                                                                                            |
| /proc/           | Sistemas de arquivo virtual, que possui o estado do núcleo e [processos](https://pt.wikipedia.org/wiki/Processo_\(inform%C3%A1tica\) "Processo (informática)") do sistema; a maioria dos arquivos é baseada no formato texto (ex: tempo de execução, rede).                                                 |
| /root/           | Diretório _home_ para o [superusuário](https://pt.wikipedia.org/wiki/Superusu%C3%A1rio "Superusuário") (_root_).(Opcional)                                                                                                                                                                                  |
| /sbin/           | Arquivos binários para propósito de administração do sistema.                                                                                                                                                                                                                                               |
| /tmp/            | Arquivos temporários. (Ver também /var/tmp).                                                                                                                                                                                                                                                                |
| /srv/            | Dados específicos que são [servidos](https://pt.wikipedia.org/wiki/Servidor_\(computa%C3%A7%C3%A3o\) "Servidor (computação)") pelo sistema.                                                                                                                                                                 |
| /usr/            | Hierarquia secundária para dados compartilhados de usuários, cujo acesso é restrito apenas para leitura.                                                                                                                                                                                                    |
| /usr/bin/        | O mesmo que a hierarquia do topo (/bin), mas contém apenas arquivos não essenciais (que não são necessários para que o sistema funcione ou para a sua recuperação).                                                                                                                                         |
| /usr/include/    | Diretório padrão para arquivos do tipo [header](https://pt.wikipedia.org/wiki/Arquivo_de_cabe%C3%A7alho "Arquivo de cabeçalho").                                                                                                                                                                            |
| /usr/lib/        | O mesmo que a hierarquia do topo (/lib).                                                                                                                                                                                                                                                                    |
| /usr/sbin/       | O mesmo que a hierarquia do topo, mas contém apenas arquivos não essenciais (ex: [daemons](https://pt.wikipedia.org/wiki/Daemon_\(computa%C3%A7%C3%A3o\) "Daemon (computação)") e serviços de [rede](https://pt.wikipedia.org/wiki/Rede_de_computadores "Rede de computadores")).                           |
| /usr/share/      | Dados compartilhados que são independentes da arquitetura do computador..                                                                                                                                                                                                                                   |
| /usr/src/        | [Código fonte](https://pt.wikipedia.org/wiki/C%C3%B3digo_fonte "Código fonte") (ex: código fonte do núcleo do sistema)                                                                                                                                                                                      |
| /usr/X11R6/      | [**X** Window System](https://pt.wikipedia.org/wiki/X_Window_System "X Window System"), Versão **11 R6**.                                                                                                                                                                                                   |
| /usr/local/      | Hierarquia terciária com dados locais, específicos deste _[host](https://pt.wikipedia.org/wiki/Host "Host")_.                                                                                                                                                                                               |
| /var/            | Arquivos "variáveis", como [logs](https://pt.wikipedia.org/wiki/Log_de_dados "Log de dados"), [base de dados](https://pt.wikipedia.org/wiki/Banco_de_dados "Banco de dados"), páginas [Web](https://pt.wikipedia.org/wiki/Web "Web") e arquivos de [e-mail](https://pt.wikipedia.org/wiki/E-mail "E-mail"). |
| /var/lock/       | Arquivos de **lock**. Utilizados para manter o controle sobre recursos em uso.                                                                                                                                                                                                                              |
| /var/log/        | Arquivos para **log**. Utilizado para [log de dados](https://pt.wikipedia.org/wiki/Log_de_dados "Log de dados") em geral.                                                                                                                                                                                   |
| /var/mail/       | Caixas de email dos usuários do sistema.                                                                                                                                                                                                                                                                    |
| /var/run/        | Contém informação sobre a execução do sistema desde a sua última inicialização. (ex: usuários e [daemons](https://pt.wikipedia.org/wiki/Daemon_\(computa%C3%A7%C3%A3o\) "Daemon (computação)") em execução).                                                                                                |
| /var/spool/      | **[Spool](https://pt.wikipedia.org/wiki/Spooling "Spooling")** para tarefas em espera para execução. (ex: filas de impressão e emails ainda não lidos).                                                                                                                                                     |
| /var/spool/mail/ | Local para caixas de correio dos usuários. Não deve ser mais utilizada, existe apenas para compatibilidade retroativa.                                                                                                                                                                                      |
| /var/tmp/        | Arquivos temporários. Quando em modo multi-usuário, preferível em relação ao /tmp.                                                                                                                                                                                                                          |
