O [[Caminho relativo]], compreende qual é o usuário/pasta que você está no momento então ele 'abrevia' para que não seja preciso mostrar todo o trajeto até ele, ficando por exemplo:
```
~/Downloads
```
Perceba que diferente do Caminho absoluto, ele entende que eu sou o 'netto' (bela afirmação novamente) então ele não mostra que estou dentro do Home e no meu usuário.

Isso não fica limitado apenas a 'terminal', como dei o o spoiler, se for rodar um script, ele vai tomar como base o caminho do arquivo, então vamos supor:

> Tenho uma pasta para meus scripts, que ficam no caminho absoluto: `/home/netto/bin`
> com isso, tenho um script dentro dessa pasta que salva log a cada hora, nele eu marco para salvar em: `/Documentos` naturalmente, ele vai procurar por esse caminho dentro de sua própria pasta, para que ele possa de fato salvar na pasta que desejo: `/home/netto/Documentos` eu preciso especificar o caminho absoluto