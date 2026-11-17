Pois bem, o Android é um sistema com vários termos de uso do Google, logo, sabemos muito bem que eles devem com certeza interferir nos meus dados e sabemos bem de 'telemetria'.

Logo, precisava desativar essas funções, pesquisei e aparentemente, para desativação, precisamos rodar comandos via [[adb]], entretanto, tentei conectar um cabo [[USB - Universal Serial Bus|USB]] e mudar no Android para 'Dispositivo Controlado pelo aparelho conectado' e ficou constando 'falha', ao pesquisar, compreendi que poderia ser **questão de permissões do usuário no sistema Linux** com as regras do `udev`.

Sendo então necessário instalar:
`sudo apt update && sudo apt install android-tools-adb android-tools-fastboot`