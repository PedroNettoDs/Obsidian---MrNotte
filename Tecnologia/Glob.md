---
aliases:
  - Globbing
  - Glob Characters
---
# **Origem**:
O termo vem de '**global**', e permaneceu assim, pois nas primeiras versões do **[[Unix]]**, o [[Shell]] não possuía essa 'funcionalidade' nativamente, sendo necessário do programa, localizado:
`/etc/glob`
# **Sobre**:
O **Globbing** (Expansão de nomes de arquivos), utiliza '*metacaracteres*' para definir 'padrões de chamada' em arquivos e diretórios, substituindo uma 'listagem' de arquivos.

Exemplo: vamos supor que você quer excluir todos os arquivos de textos de uma pasta, para isso, você pode utilizar o comando:
```
rm *.txt
```
Assim, foi definido que todos os arquivos com a terminação '.txt' serão excluídos **sem você precisar listar** todos eles

Foco no 'sem você precisar..' porém o shell transforma o padrão em listagem e passa o comando em cima dos arquivos listados.

---
![[Metacaracteres]]:
