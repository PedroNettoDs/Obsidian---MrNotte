## GUI simples (Python + Qt) — recomendada
Como você usa [[KDE Plasma]], o melhor encaixe é **Qt** (PyQt6 ou PySide6).  
A ideia:

- Campos para:
    - `friendly_name`
    - lista de `media_dir` (música/fotos/vídeos) com botão “Adicionar pasta”
    - `network_interface` (opcional)
    - `inotify` (sim/não)
        
- Botões:
    - **Salvar**
    - **Reiniciar serviço**
    - **Rebuild DB**
        
- Rodar como usuário normal, e quando precisar:
    - salvar em `/etc/minidlna.conf` via `pkexec`/polkit
    - reiniciar via `pkexec systemctl restart minidlna`


## O que faz uma GUI “de verdade” pro [[MiniDLNA]]?
Ela precisa lidar com 4 coisas:

1. **Ler** o arquivo conf (`/etc/minidlna.conf` ou `~/.minidlna/minidlna.conf`)
    
2. **Editar** mantendo comentários/linhas que você não mexeu
    
3. **Salvar com permissão** (quando for `/etc/...`)
    
4. **Aplicar**:
    
    - `systemctl restart minidlna` (global)
        
    - ou reiniciar processo `minidlnad` (modo usuário)
        
    - rebuild DB (global: remover `files.db` e reiniciar / local: `minidlnad -R`)

### Metas
- interface Qt bonitinha
- validação do arquivo
- backup automático `/etc/minidlna.conf.bak`
- detecção se você está usando modo global ou por usuário