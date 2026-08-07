Pois bem, descobri que o ZIP não é uma sigla e sim, vem do 'zipper', justamente para fechar.
Sendo um modelo de compactação, desenvolvido por uma empresa denominada 'PKZIP';

Ele é muito famoso em sistemas operacionais Ruindows, porém também está disponível nos [[Linux]]/[[Unix]].
```bash
zip [OPÇÕES] [Nomenclatura zip (teste.zip) [alvo]]
```

### Compactar
**Exemplo** de criação do .zip:
```bash
zip compacto.zip alpha*
```
![[zip com glob.png|650]]

Para zipar, uma pasta inteira e suas subpastas, é utilizado: `-r` **Recursivo**
```bash
zip -r School.zip School
```
![[zip -r school.png]]

---
### Decompactar
**Exemplo** de descompactar:
```bash
unzip -l School.zip
```
> Perceba o parâmetro `-l` de '**listar**'.
![[unzip -l.png]]


https://pt.wikipedia.org/wiki/ZIP