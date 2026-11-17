O conjunto tem três peças: o **[[Claude Code]]** decide, o **[[Herdr]]** orquestra e o **[[Ollama]] do [[Kubuntu]]** executa.

```
Você ──► Claude Code (aqui, Claude da Anthropic)
             │  skill "herdr-local"
             ▼
         herdr-local  ──►  Herdr, sessão "alfred" (serviço systemd)
                               │  um workspace por worker
                               ▼
                         Worker = Claude Code ligado ao Ollama
                               │  ANTHROPIC_BASE_URL=http://BatComputador.local:11434
                               ▼
                         Ollama do ALFRED no Kubuntu (modelo local)
```

## As peças

**1. Herdr.** É como um tmux feito para agents de [[Inteligência Artificial|IA]]: abre terminais (panes) e reconhece o agent que roda em cada um. 
Ele sabe dizer se o [[agent]] está trabalhando, parado ou esperando aprovação. Também aceita comandos via [[Linha de comando|CLI]], como "mande este prompt", "espere terminar" e "leia a saída". É isso que permite um agent controlar outros.

**2. Sessão `alfred`.** 
[[1.0 - Alfred Pennyworth|Alfred]]
É um servidor do Herdr sem interface, que o systemd mantém rodando. Ela fica separada da sua sessão normal, então os workers não aparecem no meio do seu trabalho. Para assistir, use `herdr-local attach`.

**3. Workers locais.** Cada worker é o próprio programa `claude`, mas com variáveis de ambiente que trocam o "cérebro". Em vez de chamar a API da Anthropic, ele chama o Ollama do Kubuntu, que desde a versão 0.14 entende o mesmo formato de API. Ele continua tendo as ferramentas do Claude Code (ler e editar arquivos, rodar comandos), só que quem pensa é o modelo local.

**4. `herdr-local`.** É o atalho que junta tudo:

| Comando                | O que faz                                               |
| ---------------------- | ------------------------------------------------------- |
| `check`                | Testa se o Ollama responde e lista os modelos           |
| `spawn <nome>`         | Cria um workspace e inicia um worker com o modelo local |
| `ask <nome> "..."`     | Envia a tarefa, espera terminar e mostra o resultado    |
| `read <nome>`          | Lê mais da saída do worker                              |
| `list` / `stop <nome>` | Lista e encerra os workers                              |
| `attach`               | Abre a tela do Herdr para você assistir                 |

**5. Skill no Claude Code.** Quando você pede algo como "roda isso localmente" ou "usa o ALFRED", o Claude Code daqui chama o `herdr-local` sozinho. Ele cria o worker, delega a tarefa, lê o resultado, revisa e te responde.

## Um pedido na prática

1. Você diz aqui: _"resume os logs do Linker usando o modelo local"_.
2. O Claude Code roda `herdr-local check` para ver se o Kubuntu está acessível.
3. Ele roda `herdr-local spawn logs --cwd ~/Área de trabalho/Linker`.
4. Ele roda `herdr-local ask logs "Resuma..."`. O worker processa tudo no Ollama, sem gastar API.
5. O Claude Code lê a saída, confere e te entrega o resumo.
6. Ele roda `herdr-local stop logs`.

## Regras de segurança

- Diálogos de confiança e de permissão dos workers **nunca** são aceitos automaticamente. Eles voltam para você decidir.
- Nas tarefas locais, o tráfego vai só para o Kubuntu. A telemetria do worker está desligada.
- Modelos locais são mais fracos que o Claude. Por isso o Claude Code delega tarefas pequenas e objetivas e revisa o resultado.

**Ainda falta:** liberar o Ollama na rede do Kubuntu (`OLLAMA_HOST=0.0.0.0`), como expliquei antes. Hoje o `check` falha porque ele só escuta em `127.0.0.1`.