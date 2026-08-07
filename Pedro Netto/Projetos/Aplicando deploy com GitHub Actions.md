---
Medium: https://medium.com/@MrNetinhu/aplicando-deploy-com-github-actions-3f6f52cb810e
Linkedin: https://www.linkedin.com/pulse/aplicando-deploy-com-github-actions-pedro-henrique-netto-d1ksf/?trackingId=RJvw70YoRgC5GqiwADfrwg%3D%3D
Blogspot: https://nettotecnologias.blogspot.com/2026/07/aplicando-deploy-com-github-actions.html
---
### _Prefácio_
Pois bem, eu possuo dois repositórios, Nettotech (meu curriculo online) e a wiki.nettotech.com.br (aonde vai parar essas notas que estou criando), porém até agora, eles estão na minha máquina pessoal, ou seja, sempre que ela desliga, tchau tchau site, entretanto, como estou começando a querer aparecer mais midiaticamente, preciso que elas fiquem fulltime online.

Aluguei uma VPS e queria que, sempre que eu desse um commit, subir essa atualização para a VPS, então partiu?

---
### Configurando o deploy no projeto

Bom, primeira coisa que fiz, foi criar no meu projeto/repositório o arquivo no caminho:
`.github/workflows/deploy.yml`

Vibecodando, foi gerado a  seguinte configuração:
```yml
name: Deploy to VPS

on:
  push:
    branches:
      - main
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Deploy via SSH
        uses: appleboy/ssh-action@v1.0.0
        with:
          host: ${{ secrets.VPS_HOST }}
          username: ${{ secrets.VPS_USER }}
          key: ${{ secrets.VPS_SSH_KEY }}
          port: ${{ secrets.VPS_SSH_PORT }}
          script: |
            cd /home/usuario/NettoTech
            git pull origin main
```

>Se fosse para passar meu parecer do código, posso dizer que é bem simples de entender o que está ocorrendo, sendo possível acrescentar muitos passos caso necessário, porém, uma coisa que achei legal de se entender, é que:

O [[GitHub]], oferece dentro do '**Settings**' a aba '**Secrets and variables**'

![[Aplicando deploy com GitHub Actions1.png | 700]]

Sendo dai que será buscado o `${{ secrets.VPS_HOST }}`, o que eu achei muito legal, pois percebi que o GitHub não é só para 'Versionamento' do [[GitHub]] e tenho que aprender muito mais, assuntos como 'PR', GitHub Labs e etc.

Ainda assim, prosseguindo.
### Criação da chave pública SSH
No seu ambiente, é importante criar um par de chaves dedicado para o deploy, então prosseguimos com o comando:
```bash
ssh-keygen -t ed25519 -C "github-deploy" -f ~/.ssh/github_deploy
```
- Quando for solicitado a '**passphrase**', deixe em branco e pressione Enter
	*Para não possuir senha (para a automação)*.
- Copie a chave que aparecerá no:
```
cat ~/.ssh/github_deploy.pub
```

Depois com essa chave criada, prossegui com a criação da pastas e colei dentro do arquivo 'authorized_keys' o que havia copiado anteriormente:
```bash
mkdir -p ~/.ssh
nano ~/.ssh/authorized_keys
```
- Não preciso explicar como salvar né?, bom, é: *Ctrl + O, Enter, Ctrl + X*

Importante, ajustar a permissão da pasta e do arquivo:
```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```

---
### Adicionado os Secrets no GitHub
Bom, primeiro passo é copiar a chave SSH
```bash
cat ~/.ssh/github_deploy
```
Seguindo o arquivo `deploy.yml`, acesse seu repositório pressione o botão: '**New repository secret**':

![[Aplicando deploy com GitHub Actions1.png | 700 ]]

Informe o no '**name**', o que você descreveu, na variável: `${{ secrets.VPS_SSH_KEY }}`
e depois cole dentro do '**Secret**' o que você copiou do comando acima.

![[Aplicando deploy com GitHub Actions2.png]]

Assim prossiga com 'VPS_HOST', 'VPS_USER', 'VPS_SSH_PORT'

---

Dessa forma, qualquer Commit realizado, aparecerá uma 'workflow' dentro de 'Actions'

![[Aplicando deploy com GitHub Actions3.png |700]]

e conseguimos acessar dentro deles, para avaliar como foi o processo:

![[Aplicando deploy com GitHub Actions4.png | 700]]
Com isso, já ganho 1+ na Skilltree de [[DevOps]] [[CI e CD|CI/CD]] :D