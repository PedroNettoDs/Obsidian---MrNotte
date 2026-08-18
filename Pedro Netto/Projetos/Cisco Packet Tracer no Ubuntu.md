
### Prefácio
Pois bem, estudando sobre [[SSL]]/[[TLS]] e [[HTTPS (Hypertext Transfer Protocol Secure)|HTTPS]], percebi que queria muito ver algo 'prático', então lembrei do Cisco Packet Tracer, o programa de simulação da [[Cisco]], mas.. nunca instalei no Linux.

### Instalação
Para conseguir ter acesso ao instalador, precisei me matricular no curso '[Começando com Cisco Packet Tracer](https://www.netacad.com/launch?id=ec0847b7-e6fc-4597-bc31-38ddd6b07a2f&tab=curriculum&view=8e9b3907-d97b-5177-8413-a6725ffcc762)', para assim, conseguir o [Link](https://www.netacad.com/resources/lab-downloads?courseLang=pt-BR) de Download;

Baixei logo a versão de [[Ubuntu]] e seu Download foi de um arquivo '[[deb]]'
![[deb#Como instalar]]

Dessa forma, instalei, entretanto.. surgiu um problema.

### Problema de login
O **Cisco Packet Tracer** possui um sistema de login, aonde você precisa informar suas credenciais de NetAcad, entretanto, essa janela não estava abrindo, pesquisando mais, compreendi que uma das soluções, seria 'desativar a internet', para entrar como usuário 'Convidado', assim, não solicitando Login.
Mas não quero ter que desativar minha interface de Rede toda vez que eu for abrir o programa, então pesquisei um pouco e compreendi que havia uma ferramenta, denominada '[[Firejail]]'

#### Instalando Firejail
Cara, adoro Linux, pois o gerenciador de pacotes `apt` já resolve:
```sh
sudo apt install firejail
```

### Utilizando Firejail no Cisco Packet Tracer
```sh
firejail --net=none packettracer
```