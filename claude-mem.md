---
porta: 37776
---
O Claude-mem é um [[plugin]] de [[Código aberto]] criado para o [[Claude Code]] que resolve o problema de 'amnésia da [[Inteligência Artificial]]', permitindo que ele se lembre do contexto e do histórico dos seus projetos.

O **Claude-mem** roda por padrão na porta **37777**
Além de funcionar nos bastidores, essa mesma porta serve uma interface de painel de controle. Se você abrir **`http://localhost:37777`** no seu navegador enquanto o Claude-mem estiver rodando, você terá acesso a uma interface gráfica local onde poderá:

- Ver o histórico de memórias gravadas em tempo real.
    
- Apagar ou editar o que a IA aprendeu.
    
- Alterar as configurações do plugin (como o modelo usado para compressão e os limites de tokens).
---

Sem ele, cada vez que você inicia um novo terminal, o [[Claude]] começa do zero e exige o consumo de milhares de [[tokens]] para recarregar as informações.

- **Captura automática:**
	Ele roda silenciosamente nos bastidores e registra as ações do agente, como decisões de código, ferramentas utilizadas e arquivos alterados
- **Compressão por IA:** 
	Ao invés de salvar textos longos e brutos, ele aciona a IA no final de cada sessão para comprimir os dados em resumos estruturados e fáceis de buscar.
- **Recuperação inteligente:**
	Nas sessões seguintes, ele revela um contexto resumido inicial e fornece ferramentas de busca para que o Claude extraia detalhes específicos apenas quando realmente precisar, economizando custos.

**Por que a instalação local é necessária:** A ferramenta não funciona pela nuvem porque precisa atuar como um [[Processo]] em segundo plano que intercepta os comandos e eventos diretamente do terminal do seu [[Sistema Operacional]].

---

A interação humana com o **Claude-mem** acontece de duas formas: através da conversa natural com o Claude e pelo gerenciamento direto dos arquivos no seu computador. Ele foi desenhado para ser uma ferramenta de bastidores, quase invisível no dia a dia.

**1. Interação via Chat (O uso diário)** Você não abre um aplicativo ou interface gráfica do Claude-mem. Em vez disso, você simplesmente dá ordens ao Claude (no terminal via Claude Code) para que ele interaja com a ferramenta. Exemplos de como você "mexe" nele conversando:

- **Para forçar um salvamento:** "Anote na sua memória que a partir de agora usaremos a porta 8080 para este projeto." ou "Faça um resumo das alterações de hoje e salve no Claude-mem."
    
- **Para resgatar contexto:** "O que nós decidimos sobre a arquitetura de autenticação na semana passada?"
    
- **Para corrigir rotas:** "Apague da sua memória a instrução antiga sobre a API v1. Atualize para a v2."
    

O Claude entende sua intenção em linguagem natural e traduz isso nos comandos técnicos que escrevem ou leem no banco de dados.

**2. Gerenciamento Local (Como administrador)** Se você quiser colocar a mão na massa sem usar a IA, você tem controle total sobre a infraestrutura da ferramenta:

- **Acesso direto aos dados:** As memórias ficam salvas em um arquivo de banco de dados comum (um arquivo `.sqlite`, geralmente na sua pasta de usuário). Você pode abrir esse arquivo com programas gratuitos como o _DB Browser for SQLite_ para ler, apagar ou alterar textos manualmente.
    
- **Configuração via terminal:** A instalação inicial e as atualizações são feitas por você no terminal (usando comandos como `npm` ou `npx`). É você quem edita o arquivo de configuração do Claude (`claude.json`) para dizer a ele onde o plugin do Claude-mem está instalado.
    
- **Auditoria:** Você pode olhar a tela do terminal para monitorar os "logs" e ver exatamente o momento em que o Claude decide acessar a memória, garantindo que ele não está gravando nada sem o seu consentimento.

---

repositório no GitHub detalha dois recursos principais que permitem essa centralização além da sua máquina local:

- **Cloud Sync:** Um recurso nativo que faz o backup automático e sincroniza suas memórias locais diretamente com a plataforma web `cmem.ai` a cada nova gravação realizada pelo processo em segundo plano (worker).
    
- **TeamBrain:** Um módulo de espaço de trabalho compartilhado opcional que unifica as listas de tarefas, o progresso e o histórico de diferentes máquinas ou membros de equipe em uma mesma interface.