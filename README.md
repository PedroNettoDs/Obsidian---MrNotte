# Obsidian - MrNotte

Vault pessoal do Pedro Netto no [Obsidian](https://obsidian.md), com ~534 notas em português cobrindo principalmente tecnologia, além de certificações, projetos pessoais, diário e outros temas.

## Estrutura

| Pasta | Conteúdo |
|---|---|
| `Tecnologia/` | A maior parte do vault — Linux, redes, criptografia, sistemas numéricos, DevOps, etc. |
| `Certificações/` | Notas de estudo para certificações (AWS Cloud Practitioner, CCNA, ITIL, LPIC-1, Scrum, ...) |
| `Glossário/` | Termos técnicos e empresas, em formato de verbete curto |
| `Pedro Netto/` | Conteúdo pessoal: diário, artigos, projetos (Fatec, Alfred, Fileserver, ...), entretenimento |
| `Religião/` | Mitologia e teologia comparada |
| `Eletrônica/`, `Física/`, `Teorias/` | Pastas menores, temas avulsos |
| `midias/` | Pasta de anexos do Obsidian (imagens, PDFs) referenciados pelas notas |
| `.scripts/` | Scripts utilitários do vault (ver abaixo) |

Notas soltas na raiz cobrem tópicos que ainda não ganharam uma pasta própria (ex.: `Criptografia.md`, `Wayland.md`, `MBR - Master Boot Record.md`).

## Convenções do Obsidian

- Links entre notas e embeds de imagem usam wikilinks (`[[Nota]]`, `![[imagem.png]]`), com `newLinkFormat: shortest` — ou seja, sempre o nome puro do arquivo, sem caminho.
- A pasta de anexos configurada é `/midias`.
- Plugins da comunidade em uso: `obsidian-icon-folder`, `obsidian-kanban` (usado em `Objetivos.md`), `pretty-properties`.
- `Lista - Publicações.base` rastreia quais notas já foram publicadas externamente (Medium, Blogspot, LinkedIn) via propriedades no frontmatter.

## Imagens e `/midias`

Para manter o repositório público enxuto e as notas visualizáveis sem depender de arquivos locais, várias notas têm suas imagens **comprimidas e embutidas como base64** diretamente no markdown (`![](data:image/webp;base64,...)`), em vez de um link para um arquivo em `/midias`. O arquivo original, quando ainda existe, foi movido para descarte depois de embutido.

Isso é feito com `.scripts/gerenciar_imagens.py`, que também sabe:
- encontrar imagens em `/midias` que não são mais referenciadas por nenhuma nota;
- reverter um embed base64 de volta para um arquivo `.jpg` em `/midias` + `![[...]]`.

Uso e detalhes em [.scripts/gerenciar_imagens.md](.scripts/gerenciar_imagens.md).

## Repositório

Hospedado em [github.com/PedroNettoDs/Obsidian---MrNotte](https://github.com/PedroNettoDs/Obsidian---MrNotte).
