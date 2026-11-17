com um [[Terminal]] aberto, você pode suspender ele para trás e começar a fazer um novo processo no mesmo terminal.

o atalho para isso é o `Ctrl+Z`, que normalmente é associado a 'desfazer' (foi assim que eu descobri, um engano).
Faz o processo ser suspendido (pausado).

Criando assim várias instâncias do programa, para trazer o programa de volta, é necessário utilizar o comando `fg` que significa foreground, trazendo assim a que estava pausada.

se quiser selecionar alguma instância específica, pode ser utilizando o comando `fg %1` ou `fg %2`

