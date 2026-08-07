---
Blogspot: https://nettotecnologias.blogspot.com/2026/07/tecla-de-atalho-menu-contexto-msi-gk20.html
---
_Préfacio_
Tenho um teclado 'Vigor GK20' da [[MSI]], e nele possui uma tecla de dragão:
![[Criar tecla de atalho - Menu Contexto-teclado.png | 600]]

Quero, que ao pressionar essa tecla + Ctrl, abra o menu de contexto, para deixar mais fluído o controle somente pelo teclado, sem a necessidade de relar no mouse.

---
Como utilizo o [[KDE Plasma]], já possui a ferramenta: [[X Event Viewer]], 
![[Criar tecla de atalho - Menu Contexto-xev.png| 600]]
Entretanto, a tecla 'dragão' não é reconhecida, logo precisaremos utilizar outra ferramenta: [[evtest]]
![[evtest-exemple.png| 600]]

Mas também não foi detectado ao ser pressionado a tecla, logo o teclado 'intercepta' a tecla em seu [[Firmware]], só encaminhando para a máquina quando pressionada a tecla pré-definida (F9 = Voltar musica, F10 = Pausar/Play...)

Logo, torna inviável o projeto prosseguir com essa tecla, para conseguir, seria necessário fazer uma [[Engenharia reversa]], utilizando [[Wireshark]] + [[USBPcap]], entretanto, realmente seria muito trabalho para algo tão pequeno, correndo o risco também de inutilizar o teclado.

Logo o projeto foi um fracasso.
![[Projeto fracassado.png| 600]]