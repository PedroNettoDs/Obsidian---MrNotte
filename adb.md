---
aliases:
  - Android Debug Bridge
---
Android Debug Bridge é uma ferramenta de linha de comando que cria um canal de comunicação entre sistema do computador e operacional do aparelho.


### Instalação "Manual"
Para instalar, prosseguiremos com o download da ferramenta: 
https://dl.google.com/android/repository/platform-tools-latest-linux.zip

Depois prosseguimos com a instalação
```bash
mkdir -p ~/.local/share/adb-fastboot
unzip ~/Downloads/platform-tools-latest-linux.zip -d ~/.local/share/adb-fastboot
```

Depois atualizamos o caminho
```bash
if [ -d "$HOME/.local/share/adb-fastboot/platform-tools" ] ; then
    export PATH="$HOME/.local/share/adb-fastboot/platform-tools:$PATH"
fi
```

e atualizamos o source:
`source ~/.profile`

### Instalação via apt
```bash
sudo apt update && sudo apt install android-sdk-platform-tools
```

https://wiki.lineageos.org/adb_fastboot_guide#installing-adb-and-fastboot