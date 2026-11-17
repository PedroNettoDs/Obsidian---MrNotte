### Prefácio 
Possuo um Samsung Galaxy S23 FE (codinome `r11s`, Exynos 2200) e fiquei muito nervoso pois ouviram minhas conversas de novo.

Então decidi tentar mudar o [[Sistema Operacional]], mas o **Galaxy S23 FE** não é compatível com o build oficial do [[LineageOs]] voltado para o S23 padrão (`dm1q`) — o que causaria um *brick* irreversível no aparelho. Portanto, prossegui com a otimização profunda e o endurecimento de privacidade (*hardening*) da própria One UI original. Para isso, conectei via [[USB - Universal Serial Bus|USB]] no meu computador com [[Kubuntu]] e utilizei o [[adb]].

---
### Ativando a Depuração USB e Autorização
No celular, vá em **Configurações → Sobre o telefone → Informações do software** e clique 7 vezes no **Número de compilação** para liberar as *Opções de desenvolvedor*. Lá dentro, ative a **Depuração USB** e certifique-se de que o *Bloqueio automático (Auto Blocker)* está desativado.

Com o [[adb]] instalado no Kubuntu, rode no terminal para reiniciar o servidor e gerar as chaves de segurança:
```bash
adb kill-server && rm -f ~/.android/adbkey ~/.android/adbkey.pub && adb start-server && adb devices

```

Surgirá na tela do celular uma mensagem de permissão. Marque *"Sempre permitir deste computador"* e toque em **Permitir**.

---
### Comandos de Otimização e Privacidade via Terminal

#### 1. Desativação de Telemetria e Escuta de Voz
```bash
adb shell '
settings put system samsung_errorlog_agree 0
settings put system marketing_info_agree 0
settings put global multi_cb 0
settings put secure voice_interaction_service ""
settings put secure assistant ""
for app in com.google.android.googlequicksearchbox com.google.android.gms com.google.android.as com.samsung.android.bixby.agent com.samsung.android.bixby.wakeup com.samsung.android.svoiceime; do
cmd appops set $app RECORD_AUDIO ignore 2>/dev/null
cmd appops set $app PHONE_CALL_MICROPHONE ignore 2>/dev/null
cmd appops set $app RECEIVE_AMBIENT_TRIGGER_AUDIO ignore 2>/dev/null
done
for pkg in com.samsung.android.bixby.wakeup com.samsung.android.bixby.agent com.samsung.android.bixby.service com.samsung.android.visionintelligence com.samsung.android.svoiceime com.samsung.android.rubin.app com.sec.android.diagmonagent com.samsung.android.securitylogagent com.samsung.android.dqagent com.samsung.android.svcagent com.samsung.android.mapsagent com.aura.oobe.samsung com.sec.spp.push com.google.android.as com.google.android.as.oss; do
pm uninstall -k --user 0 $pkg 2>/dev/null
done
' && adb reboot

```

#### 2. Travamento Definitivo do Microfone em Nível de UID (Correção pós-reboot)
Como o Android 14/15 restaura permissões se alteradas apenas no pacote, travamos em nível de UID com a flag `user-fixed` e limpamos o histórico:
```bash
adb shell '
for app in com.google.android.googlequicksearchbox com.google.android.gms; do
pm revoke --user 0 $app android.permission.RECORD_AUDIO 2>/dev/null
pm set-permission-flags --user 0 $app android.permission.RECORD_AUDIO user-fixed 2>/dev/null
cmd appops set --uid $app RECORD_AUDIO ignore
cmd appops set --uid $app PHONE_CALL_MICROPHONE ignore 2>/dev/null
cmd appops set --uid $app RECEIVE_AMBIENT_TRIGGER_AUDIO ignore 2>/dev/null
done
pm clear com.google.android.googlequicksearchbox 2>/dev/null
am force-stop com.google.android.gms
'

```

> **Dica:** Vá em *Opções do desenvolvedor → Blocos de configurações rápidas do desenvolvedor* e ative a chave **Sensores desligados** (*Sensors off*). Isso adiciona um botão físico de corte total de câmera e microfone na sua barra de notificações.

---
#### 3. Otimização de Desempenho e Bateria
Desativa as varreduras ocultas de Wi-Fi/Bluetooth, desliga o **RAM Plus** (`ram_expand_size 0`) para evitar o uso do armazenamento UFS 3.1 como memória virtual lenta — garantindo que o sistema utilize exclusivamente os **8 GB de RAM LPDDR5** nativa e ultrarrápida do S23 FE —, ativa o congelador de apps em cache e acelera as animações para `0.5x`:

```bash
adb shell '
settings put global wifi_scan_always_enabled 0
settings put global ble_scan_always_enabled 0
settings put system nearby_scanning_enabled 0
settings put global ram_expand_size 0
settings put global cached_apps_freezer enabled
settings put global window_animation_scale 0.5
settings put global transition_animation_scale 0.5
settings put global animator_duration_scale 0.5
'

```
#### 4. Remoção de Bloatware e Serviços Ocultos (Meta / Geofence / GOS)
```bash
adb shell '
for pkg in com.facebook.services com.facebook.system com.facebook.appmanager com.samsung.android.ipsgeofence com.samsung.android.beaconmanager com.samsung.android.mcfds com.samsung.android.app.spage com.samsung.android.game.gos com.samsung.android.game.gamehome com.samsung.android.game.gametools com.samsung.android.arzone com.samsung.android.aremoji; do
pm uninstall -k --user 0 $pkg 2>/dev/null
done
'

```
#### 5. Compilação AOT de Aplicativos (ART Speed Profile)
Otimiza todos os aplicativos instalados para reduzir aquecimento e consumo de bateria:
```bash
adb shell cmd package compile -m speed-profile -f -a && adb reboot

```

#### 6. Bloqueio de Atualizações de Sistema (OTA)
```bash
adb shell '
settings put global ota_disable_automatic_update 1
for pkg in com.wssyncmldm com.sec.android.soagent com.samsung.android.app.updatecenter com.samsung.android.app.omcagent; do
pm clear --user 0 $pkg 2>/dev/null
pm disable-user --user 0 $pkg 2>/dev/null
pm uninstall -k --user 0 $pkg 2>/dev/null
done
'

```

---

### Auditoria
Para confirmar se a telemetria, as chaves globais e o microfone (Uid mode: ignore) continuam bloqueados:
```bash
adb shell '
settings get system samsung_errorlog_agree
settings get system marketing_info_agree
settings get global multi_cb
cmd appops get com.google.android.googlequicksearchbox RECORD_AUDIO
cmd appops get com.google.android.gms RECORD_AUDIO
'

```

---

### Reversão (Caso necessário)
**Restaurar Atualizações:**
```bash
adb shell '
settings put global ota_disable_automatic_update 0
for pkg in com.wssyncmldm com.sec.android.soagent com.samsung.android.app.updatecenter com.samsung.android.app.omcagent; do
cmd package install-existing $pkg 2>/dev/null
pm enable --user 0 $pkg 2>/dev/null
done
'

```

**Devolver permissão de microfone para pesquisa da Google:**
```bash
adb shell cmd appops set com.google.android.googlequicksearchbox RECORD_AUDIO allow

```

**Restaurar animações padrão (`1.0x`) e reativar o RAM Plus (`4096` MB):**
```bash
adb shell '
settings put global window_animation_scale 1.0
settings put global transition_animation_scale 1.0
settings put global animator_duration_scale 1.0
settings put global ram_expand_size 4096
'

```
