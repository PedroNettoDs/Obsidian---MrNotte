---
aliases:
  - Link Simbolícos
---
é um utilitário [[Unix]]/[[Linux]] que gerencia 'ligações simbólicas'.

o que é ligação simbólica?
é como uma 'placa' que aponta para um local, como se você fosse até um estabelecimento e verifica-se que tem uma placa escrita:
"Mudamos para o endereço X"

Logo, vamos supor que você queria criar **ATALHOS**, toda vez que você abre seu Terminal, está na `/home/netto`, e quer chegar até: `/mnt/HD/Dev/Projeto`, olha quanto texto a escrever..

pois você pode utilizar o symlink:
```bash
ln -s /mnt/HD/Dev/Projetos /home/Projetos-link
# agora ao ir em `cd /home/Projetos-link` já direciona para o caminho.
```

