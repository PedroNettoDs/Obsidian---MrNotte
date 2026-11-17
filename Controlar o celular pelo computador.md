Eu estava pensando seriamente que gostaria de mexer em algumas coisas do meu celular, utilizando meu computador, até mesmo instalar o [[Termux]] ou desativar de alguma forma suas telemetrias, sem contar que estou utilizando o [[BixBy]] da [[Samsung]] e estou gostando da ideia de falar com um assistente virtual para marcas e me lembrar de coisas que devo fazer, em fim, vou prosseguir com a proposta.

---

Primeiramente, no Celular (Android), precisamos primeiro **Ativar as Opções do Desenvolvedor** e prosseguir com:
```
Configurações > Sobre o telefone > (toque 7 vezes em Número da versão)
```
Ativando assim então, o **Depuração USB**

---

No computador, prosseguir com a instalação do **scrcpy**:
```bash
# Linux (Debian/Ubuntu) — a versão do repositório pode estar defasada
sudo apt install scrcpy
# Arch
sudo pacman -S scrcpy
# Windows
winget install --exact Genymobile.scrcpy
# macOS
brew install scrcpy
```