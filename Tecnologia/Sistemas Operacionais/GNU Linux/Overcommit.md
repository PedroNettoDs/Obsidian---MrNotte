O **Overcommit** é um 'acidente' que pode acontecer no [[Linux]].

Ocorre quando um [[Processo]] pede por [[RAM|Memória Ram]] (`malloc`,`fork`) e o [[Kernel]] não entrega na hora.
Ele entrega um *mapeamento virtual* (pagamento fiado/promessa).

Essa promessa do Kernel, é feita sob a premissa que 'ninguém vai usar tudo ao mesmo tempo e que sobrará um pouco' (e normalmente sobra).

esse comportamento é controlado por `vm.overcommit_memory`, que pode ser configurado em três valores:

| Valor        | Comportamento                                                      |
| ------------ | ------------------------------------------------------------------ |
| `0` (Padrão) | 'Heurístico', o Kernel aceita pedidos razoável e recusa os grandes |
| `1`          | Sempre aceita                                                      |
| `2`          | Recusa acima do [[swap]] + ([[RAM]] x `overcommit_ratio`)          |
