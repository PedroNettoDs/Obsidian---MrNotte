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
