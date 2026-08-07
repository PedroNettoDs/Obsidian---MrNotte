---
Blogspot: https://nettotecnologias.blogspot.com/2026/07/implantando-keepassxc-syncthing.html
dg-publish: true
---
### Préfacio
Recentemente vi o [vídeo](https://www.youtube.com/watch?v=grjNrcol0j4) do Sr.Teclas e coincidentemente, começou a brotar notificações de tentativa de acesso no meu Outlook, mudei a senha para mais uma característica de senha minha, porém o invasor conseguiu novamente, portanto, vou prosseguir com a implantação de um cofre de senha self-hosted e que seja sincronizado com meu celular.
Para isso a solução é o [[KeepassXC]] e o [[Syncthing]].


### Instalando KeepassXC
```bash
sudo apt update
sudo apt install keepassxc
```
>Como sempre o gerenciador de pacotes, salvando

Depois, prossegui com a abertura do programa:
![[Pasted image 20260715184536.png]]

Cliquei em 'Criar Banco de Dados', inseri Nome e Descrição:
![[Pasted image 20260715184715.png]]

![[Pasted image 20260715184738.png]]

![[Pasted image 20260715184751.png]]

Depois prossegui com a seleção do caminho do Banco de Dados, `~/KeepassXC/` que sincronizarei no Syncthing.

### Instalando Syncthing
```bash
sudo apt install syncthing
```
#### inicializando e haiblitando
```bash
sudo systemctl enable syncthing@$USER
sudo systemctl start syncthing@$USER
```

Acessando através de `localhost:8384`, utilizamos o usuário e senha da máquina.
![[Pasted image 20260715183715.png]]

Prossegui com a criação de uma pasta `~/KeepassXC/` que guardará o banco.
 ![[Pasted image 20260715184414.png]]

### Utilizando o cofre de senha
![[Pasted image 20260715185016.png]]
Para que assim eu comece a registrar e salvar minhas senhas no banco de dados, assim sincronizando as modificações.