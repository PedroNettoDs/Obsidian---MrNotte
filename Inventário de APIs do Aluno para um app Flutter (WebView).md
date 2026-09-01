**Ready for review**

Select text to add comments on the plan

# Inventário de APIs do Aluno para um app Flutter (WebView)

## Context

A pergunta: **quais APIs o sistema oferece hoje** para construir, em Flutter, um app do Aluno baseado em WebView com o mínimo de funções nativas para passar na revisão da Apple.

O deliverable escolhido é o **inventário**, não um plano de implementação — a decisão de stack fica para depois. Duas descobertas condicionam a leitura desse inventário:

1. **A auditoria da API já existe.** `docs/api-aluno-contrato-flutter.md` (468 linhas, commit `6ac1b91`, 18/ago) mapeia todo endpoint aluno-facing a partir do código real — rota, view com arquivo:linha, tipos, códigos de erro e idempotência. Foi escrita explicitamente para um cliente Dart tipado. O que segue é o resumo executivo dela mais o que mudou desde então.
    
2. **O app WebView já existe, pronto, em React Native/Expo.** `react-native/` (`slug: submax-aluno-webview`, bundle `com.submax.aluno`) tem login nativo, biometria, injeção de sessão, push funcionando, notificação de treino com cronômetro e EAS configurado. Nunca foi submetido — só faltam as credenciais Apple no `eas.json`. Um app Flutter WebView reconstruiria isso do zero, no mesmo bundle.
    

---

## Resposta curta

**Base URL:** `https://aluno.submax.com.br` — o nginx serve o site e faz proxy de `/api/` para o backend, então **site e API compartilham origem**. Não há versionamento (`/api/v1/` não existe); tudo é `/api/aluno/...`, mais `/api/feed/` e `/api/arquivos-aluno/`.

**Auth:** JWT próprio do aluno, **não SimpleJWT**. HS256, segredo `ALUNO_JWT_SECRET`, claims `{sub:"aluno", aluno_id, iat, exp}`, header `Authorization: Bearer <token>`. TTL de **7 dias fixos, sem refresh e sem logout server-side** (`aluno_auth/auth.py:17-25`). `request.user` vira uma instância de `Aluno`, não de `User`.

**Contrato formal:** o backend expõe OpenAPI 3 em `/api/schema/` (Swagger em `/api/docs/`), com o esquema de auth do aluno registrado (`aluno_auth/schema.py`). **Mas veja a ressalva no fim** — boa parte dos endpoints do aluno não usa serializer DRF, e o schema os documenta mal.

---

## Inventário por domínio

### Identidade — `/api/aluno/` (`aluno_auth/api/views.py`)

| Método | Rota                      | Nota                                                                                                                                                             |
| ------ | ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| POST   | `/login/`                 | `AllowAny`. `{email, senha}` → `{access, aluno}`. 401 em credencial inválida ou `ativo=False`                                                                    |
| GET    | `/me/`                    | Perfil completo, com `foto_b64` e preferências                                                                                                                   |
| PATCH  | `/perfil/`                | Whitelist: `telefone`, `foto_b64`, `dias_disponiveis`, `horario_preferencia`, `exercicio_preferencia`, `info_adicional`. Outros campos são ignorados em silêncio |
| POST   | `/alterar-senha/`         | `{senha_atual, nova_senha, confirmar_senha}`, mín. 6 chars. Zera `primeiro_acesso`                                                                               |
| POST   | `/reset-senha/solicitar/` | `AllowAny`. Código de 6 dígitos **por WhatsApp**, não e-mail. Sempre 200 (anti-enumeração)                                                                       |
| POST   | `/reset-senha/confirmar/` | `AllowAny`. TTL 10 min, máx. 5 tentativas → 429                                                                                                                  |
| GET    | `/tema/`                  | White-label do personal: cores, `logo_b64`, banner, `whatsapp_url`                                                                                               |
| POST   | `/aceitar-termos/`        | Registra aceite com fingerprint. **Não é enforced no backend** — o bloqueio é client-side                                                                        |
| POST   | `/push-token/`            | Aceita **só `ExponentPushToken[...]`** — ver bloqueadores                                                                                                        |

Senha inicial do aluno é a data de nascimento em `ddmmYYYY` enquanto `senha_hash` for nulo (`alunos/models.py:96-108`); por isso o `primeiro_acesso` força a troca.

### Execução de treino — `/api/aluno/` (`treinos/api/views_execucao_aluno.py`)

O núcleo do produto. Nenhum desses endpoints é paginado.

|Método|Rota|Idempotência|
|---|---|---|
|GET|`/rotinas/` e `/rotinas/{id}/`|leitura|
|POST|`/rotinas/{id}/iniciar-serie/`|201 nova / 200 retomada — mas cria nova execução se a anterior já foi concluída|
|GET|`/rotinas/{id}/execucoes-serie/`|leitura|
|GET|`/rotinas/{id}/ultima-execucao/?semana=&serie=`|pré-preenche cargas, best-effort|
|POST|`/execucoes-serie/{id}/registrar-exercicio/`|**sim** — `update_or_create` por `id_exercicio`|
|POST|`/execucoes-serie/{id}/concluir/`|**sim** — no-op na 2ª chamada; dispara o push|
|POST|`/execucoes-serie/{id}/comentario/`|sim. 400 se a série não foi concluída|
|GET|`/exercicios/{id}/`|leitura. Sem escopo por personal|

`Rotina.estrutura_publicada` é um `JSONField` livre com **três caminhos de escrita divergentes** no backend (editor do personal, geração por IA, endpoint legado). Os tipos de `series`, `repeticoes`, `carga`, `intervalo` e `id_exercicio` variam entre `string` e `number` conforme quem escreveu. O frontend web contorna com union types; Dart não tem união, e é por isso que `submax-mobile` já traz `lib/core/json/converters.dart`.

### Acompanhamento — `/api/aluno/`

`GET /historico-treinos/` (heatmap, 26 semanas), `/rotinas-status/` (progresso + a `semana_atual` calculada no servidor — use essa, não calcule no cliente), `/ranking/` (top 10 do mesmo personal), `/avaliacao/`, `/avaliacoes/`, `/avaliacoes/{id}/`.

Todo decimal de avaliação sai como **string**; `AlunoInfo.plano_valor` sai como **float** enquanto `AlunoServico.valor` — no mesmo payload, um nível abaixo — sai como string.

### Social, arquivos, pagamentos, agenda

- **Feed** `/api/feed/posts/` — o **único endpoint paginado** de todo o domínio (envelope DRF, `page_size=10`). Aceita token de aluno e de personal na mesma rota.
- **Social** `/api/aluno/social/...` — buscar alunos, seguir, competições (criar, aceitar, convidar, ranking).
- **Arquivos** `/api/arquivos-aluno/` — o aluno só lê e baixa; upload e delete são bloqueados.
- **Pagamentos** `/pagamento/chave-pix/`, `/pagamentos/historico/`, `/pagamentos/registros/`.
- **Agenda** `/notificacoes-agenda/` — o aluno só lê e marca como lida.

**Não existe cobrança in-app.** O fluxo é Pix manual: o aluno lê a chave do personal e declara textualmente que pagou (cria uma `Notificacao`, não um `RegistroPagamento`). Nenhum dinheiro se move pela API — o que reduz o risco de a Apple exigir IAP.

**Não existe agenda/aulas para o aluno** — os endpoints de agenda são só do personal. Se o app precisar de calendário, é feature nova.

### O que o WebView cobre

Rotas de `frontend-aluno/src/App.tsx:57-90`: `/` home, `/rotinas`, `/treino`, `/feed`, `/perfil` (+ `/editar`), `/arquivos`, `/alterar-senha`, `/social/competicao/:id`, `/reset-senha`, `/convite/:personalId`. **O produto inteiro do aluno já está no WebView** — o nativo só precisa entregar login, sessão e os itens de valor nativo.

---

## Os dois bloqueadores

### Exclusão de conta — não existe

Nenhum endpoint, nenhuma tela. Busca exaustiva no backend e no `frontend-aluno` retorna zero. É a Guideline 5.1.1(v) da Apple (e a equivalente do Google): apps com criação de conta precisam oferecer exclusão **dentro do app**. É rejeição garantida.

Precisa de algo como `DELETE /api/aluno/conta/` com confirmação de senha, decidindo entre remoção e anonimização em cascata: `ExecucaoSerie`, `Avaliacao`, `Post`, `Comentario`, `Like`, `Amizade`, `ParticipacaoCompeticao`, `AceiteTermosAluno`, `ArquivoAluno`, `RegistroPagamento`. Vale notar que `AceiteTermosAluno` é append-only por design — é evidência jurídica de aceite, e apagá-la tem implicação legal, não só técnica.

### Push FCM/APNs — só bloqueia se a stack for Flutter

`push_service.py:11` posta em `https://exp.host/--/api/v2/push/send` e `Aluno.expo_push_token` (`alunos/models.py:62`) guarda um `ExponentPushToken[...]`, um device por conta. Zero ocorrências de `fcm`, `firebase` ou `messaging` no backend.

**Flutter puro não gera esse token.** Precisaria de `Aluno.fcm_token` + endpoint de registro, e de `notificar_aluno()` escolhendo o transporte pelo token presente — mantendo o Expo vivo enquanto o app RN existir.

Os dois gatilhos de push já funcionam e não mudam: conclusão de série (`views_execucao_aluno.py:270`, payload `{tipo:"treino_feedback", execucao_id}`) e o command `lembrar_avaliacoes_pendentes`, rodado a cada 6h pelo serviço `scheduler`.

---

## O que um WebView Flutter teria de replicar além das APIs

Isto não aparece em nenhum inventário de endpoints, mas é contrato real entre o site e o app — e é o trabalho menos óbvio da migração.

**Injeção de sessão.** O `frontend-aluno` escuta `window.addEventListener("storage")` (`store/auth.ts:144-149`) para reidratar a store Zustand quando o app injeta a sessão. As chaves são `aluno_access` e `aluno_info`. Boa notícia: `SecureSession` do `submax-mobile` já usa exatamente essas chaves (`lib/core/storage/secure_session.dart:35-36`), por decisão deliberada registrada no arquivo.

**A ponte de treino.** `frontend/src/shared/treino-execution/TreinoExecution.tsx:76-84` chama `window.ReactNativeWebView.postMessage(...)` — **o nome do global é hardcoded**. Um WebView Flutter precisa injetar um shim com esse nome, ou o shared precisa ser adaptado (e ele é compartilhado com o portal do personal). Quatro mensagens web→app (`treino-iniciado`, `descanso-iniciado`, `descanso-fim`, `treino-finalizado`) e um evento app→web (`submax:concluir-set-notificacao`).

**A notificação ongoing.** É o que consome essas mensagens: foreground service Android com cronômetro ao vivo e botão "Concluir", via `@notifee/react-native`. Android-only por decisão registrada. Em Flutter seria `flutter_local_notifications` + foreground service.

**Reload na troca de token.** O Android restaura o estado do WebView em vez de recarregar, prendendo a sessão antiga; o app RN compara o token e força `reload()` (`react-native/src/components/about.md`). Um WebView Flutter cai no mesmo problema.

---

## Ressalvas para gerar o client Dart

1. **Não gere os models só do OpenAPI.** `/me/`, as avaliações, `ranking`, `rotinas-status` e os pagamentos montam `dict` à mão nas views — `aluno_auth/api/serializers.py` tem 0 bytes. O drf-spectacular não infere esses payloads. Use `docs/api-aluno-contrato-flutter.md` e o código como fonte.
2. **Parsing defensivo em todo campo da estrutura de rotina** — pelos três caminhos de escrita.
3. **`foto_b64` sem compressão server-side**, embutido em lote em ranking, busca social, seguidores e competições — três desses sem paginação. Pesa em rede móvel.
4. **`registrarExercicio` é fire-and-forget** no web (`.catch(() => {})`). Sem rede, a UI marca concluído e o servidor nunca recebe. Já acontece hoje; os endpoints são idempotentes, então uma fila de retry resolve — mas ela não existe em lugar nenhum.
5. **Sem throttling global no DRF** — rate limit só manual, no reset de senha e no solicitar-notificação.
6. **CORS não está configurado em produção** (`prod.py` só reexporta `base.py`). Não afeta app nativo, que não sofre CORS, nem o WebView, que é same-origin. **Afetaria Flutter Web.**

---

## Comparação dos dois caminhos

||Flutter WebView (`submax-mobile`)|Finalizar o RN (`react-native/`)|
|---|---|---|
|Login nativo, secure storage|Pronto (Fase 1.1)|Pronto|
|WebView + injeção|A construir|Pronto|
|Biometria|A construir|Pronto|
|Ponte de treino + notificação|A construir (shim do global)|Pronto|
|Push|Exige FCM/APNs no backend|Funciona hoje|
|Exclusão de conta|Falta nos dois|Falta nos dois|
|Build iOS|Sem `DEVELOPMENT_TEAM`, sem entitlements|EAS configurado; falta preencher credenciais|
|Android release|**Sem permissão INTERNET no manifest main**, chave de debug|Configurado|

Os dois disputam o bundle `com.submax.aluno` — não coexistem na loja.

---

## Ação proposta

O inventário acima é a resposta. Para deixá-lo utilizável fora desta conversa:

1. **Publicar como Artifact** — uma página navegável com o inventário, os bloqueadores e a comparação, para consulta durante a construção do app.
2. **Atualizar `docs/api-aluno-contrato-flutter.md`** com o que mudou desde 18/ago: o transporte de push confirmado (`push_service.py` posta em `exp.host` — a seção 12 marca isso como não verificado), a existência do app RN completo, e os campos novos de avaliação (`peso_osseo`, `peso_residual`, `peso_muscular_calc`, do commit `c6d25f5`) que **não** estão expostos ao aluno em `_AVALIACAO_RESUMO_FIELDS`.

Nenhuma alteração de código é proposta aqui — a decisão de stack fica em aberto.

## Verificação

Como o deliverable é documental, a verificação é de exatidão do inventário:

- `GET /api/schema/` (Swagger em `/api/docs/`) para conferir as rotas registradas contra a tabela acima — lembrando da ressalva 1 sobre os payloads montados à mão.
- Autenticar com a conta de teste (`netto@hotmail.com`, token via Django shell) e chamar `/api/aluno/me/`, `/rotinas/` e `/rotinas-status/` para confirmar os shapes de resposta.
- `grep -rn "expo_push_token\|exp.host" backend/src` para confirmar que o transporte de push segue Expo-only na data da leitura.

Add Comment