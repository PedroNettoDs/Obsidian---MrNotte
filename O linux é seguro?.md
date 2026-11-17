havia feito esse questionamento para o Claude Code.

E a resposta foi:

> não. O [[Kernel]] [[Linux]] em si (mainline, código do [[Torvalds]]) nunca ganhou telemetria embutida desde a época da estouro da bolha das [[pontocom]] (1999-2001), quando ganhou fama e adoção massiva corporativa. Isso inclui hoje — nenhum commit upstream adiciona coleta de dados/phone-home no kernel.
> 
> O que existe é [[telemetria]] em camadas acima do kernel, opcional:
> - Distros (Ubuntu com ubuntu-report/Canonical Insights, opt-in)
> - Apps como [[Firefox]] (telemetria própria, desativável)
> - Checagens de conectividade/update no boot — não é coleta de dados, só checa internet/relógio/patch
> 
> Linux Foundation tem até política exigindo permissão prévia pra qualquer projeto sob guarda-chuva dela usar telemetria.
> 
> Teus logs locais (kernel update de hoje, versão 7.0.0-42) seguem esse padrão: pacote linux-image-generic sem telemetria, só correção de CVE.
> 
> Sources:
> - Linux Foundation telemetry data policy (https://www.linuxfoundation.org/telemetry-data-policy/)
> - GrapheneOS forum: what telemetry does Linux have by default (https://discuss.grapheneos.org/d/24352-is-qubes-os-really-secure-what-about-windows-security-in-2025/24)
> - Clear Linux telemetry opt-in discussion (https://community.clearlinux.org/t/is-there-telemetry-in-this/724)