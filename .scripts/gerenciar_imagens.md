# gerenciar_imagens.py

Script para cuidar das imagens de `/midias`: encontrar as que não estão mais
referenciadas em nenhuma nota, e opcionalmente embuti-las como base64 direto
no markdown (em vez de depender do arquivo local ou de um host externo).

Rodar sempre a partir da raiz do vault:

```bash
cd "/home/netto/Documentos/Obsidian - MrNotte"
python3 .scripts/gerenciar_imagens.py <comando> [opções]
```

Requer Python 3 e a biblioteca Pillow (`pip install pillow`) apenas para o
comando `embutir` — o `limpar` não precisa de nada além da stdlib.

## `limpar` — encontrar e mover imagens órfãs

Considera órfã qualquer imagem dentro de `/midias` que não apareça em nenhum
`![[arquivo]]` (ou `![alt](caminho)`) em nenhuma nota `.md` do vault.

```bash
# Só lista as órfãs, não mexe em nada (padrão)
python3 .scripts/gerenciar_imagens.py limpar

# Move de fato as órfãs listadas para midias/_lixeira/
python3 .scripts/gerenciar_imagens.py limpar --apply
```

- **Sem `--apply`**: modo dry-run, só imprime o relatório (quantas imagens,
  quantas referenciadas, quantas órfãs e a lista de caminhos). Não altera
  nada no disco — seguro de rodar quantas vezes quiser.
- **Com `--apply`**: move (não apaga) cada imagem órfã para
  `midias/_lixeira/`. Se já existir um arquivo com o mesmo nome lá dentro,
  o novo ganha um sufixo `(1)`, `(2)` etc. em vez de sobrescrever.
- Esvaziar `midias/_lixeira/` de vez (exclusão definitiva) é manual — o
  script nunca apaga nada, só move para lá.

## `embutir` — comprimir e embutir uma imagem como base64 na nota

Localiza a imagem em `/midias` (por nome, buscando em qualquer subpasta),
comprime para WebP com a Pillow, converte o resultado em base64 e substitui
o `![[arquivo.png]]` (preservando o sufixo de tamanho, tipo `|500`) pela
imagem embutida (`![|500](data:image/webp;base64,...)`) em toda nota que a
referencia.

```bash
# Uma imagem específica (nome basta, não precisa do caminho completo)
python3 .scripts/gerenciar_imagens.py embutir "nome-do-arquivo.png"

# Todas as imagens de /midias que tiverem alguma referência
python3 .scripts/gerenciar_imagens.py embutir --todas

# Ajustando compressão
python3 .scripts/gerenciar_imagens.py embutir "arquivo.png" --qualidade 90
python3 .scripts/gerenciar_imagens.py embutir "arquivo.png" --lossless        # sem perdas, melhor pra texto fino/screenshot
python3 .scripts/gerenciar_imagens.py embutir --todas --largura-maxima 1200  # redimensiona mais agressivo
```

Opções:
- `--todas`: aplica em todas as imagens referenciadas de `/midias`, em vez
  de uma só.
- `--largura-maxima N` (padrão `1600`): redimensiona a imagem se ela for
  mais larga que isso (mantém proporção). Não amplia imagens menores.
- `--qualidade N` (padrão `80`): qualidade do WebP, de 0 a 100.
- `--lossless`: usa WebP sem perdas em vez de comprimir com perdas — evita
  borrar texto fino de screenshots, mas gera um arquivo maior.

Comportamento importante:
- **Nunca mexe no arquivo original em `/midias`** — só reescreve as notas.
  Depois de embutir, o arquivo original passa a aparecer como órfão no
  `limpar` (já que a nota não usa mais `![[...]]` pra ele), e pode ser
  movido pra `_lixeira` normalmente quando quiser.
- Se o resultado em base64 ficar **maior** que o arquivo original (comum em
  imagens já pequenas/simples), a imagem é pulada automaticamente — nenhuma
  nota é alterada nesse caso.
- Se a imagem não for referenciada em nenhuma nota, também é pulada (nada
  para substituir).
- Com `--todas`, o script imprime um resumo no final: quantas notas mudaram,
  tamanho total antes/depois, e a lista de imagens puladas em cada categoria.

## `desconverter` — reverter embeds base64 de volta para arquivo em `/midias`

Varre **todas** as notas do vault procurando embeds no formato que o
`embutir` gera (`![|tamanho](data:image/webp;base64,...)`), decodifica o
base64, converte de WebP para **JPEG** e salva em `/midias` com nome
incremental (`image1.jpg`, `image2.jpg`, `image3.jpg`, ...) — continuando a
numeração a partir do maior `imageN` já existente, pra não sobrescrever
nada. Em seguida reescreve a nota trocando o embed base64 de volta para
`![[imageN.jpg|tamanho]]`.

```bash
python3 .scripts/gerenciar_imagens.py desconverter

# Ajustar qualidade do JPEG gerado (padrão: 90)
python3 .scripts/gerenciar_imagens.py desconverter --qualidade 95
```

**Atenção**: não existe opção pra reverter uma imagem específica — o
comando sempre varre o vault inteiro e reverte **todo** embed base64 que
encontrar. Se só uma parte das notas foi convertida com `embutir`, rodar
`desconverter` reverte todas de uma vez.

Comportamento importante:
- Se a mesma imagem em base64 aparecer em mais de uma nota (era o caso de
  imagens usadas em 2 lugares antes do `embutir`), o script gera **um único
  arquivo** `imageN.jpg` e aponta as duas notas pra ele — não duplica.
- Como WebP com perdas → JPEG é uma segunda camada de compressão com
  perdas, o resultado não é bit-a-bit igual ao PNG original — pra máxima
  fidelidade, seria melhor ter mantido o arquivo original em `_lixeira` em
  vez de já ter apagado.
- Imagens com transparência (RGBA) recebem fundo branco antes de virar
  JPEG, já que esse formato não suporta canal alpha.
- Se alguma imagem falhar ao decodificar/converter, o embed original é
  mantido intacto naquela nota (nada quebra) e a falha aparece no resumo
  final.

## Fluxo recomendado

1. `embutir --todas` (ou por imagem) para embutir o que for necessário.
2. Abrir uma ou duas notas alteradas no Obsidian pra conferir se a imagem
   renderiza bem (se algum texto de screenshot ficar borrado, refaça só
   aquela imagem com `--lossless`).
3. `limpar` (sem `--apply`) pra ver quais originais ficaram órfãos.
4. `limpar --apply` quando estiver satisfeito, para mover os órfãos pra
   `midias/_lixeira/`.
5. Esvaziar `midias/_lixeira/` manualmente quando tiver certeza de que não
   precisa mais dos originais.
