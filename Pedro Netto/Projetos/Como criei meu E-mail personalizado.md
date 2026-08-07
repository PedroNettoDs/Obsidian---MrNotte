---
Medium: https://medium.com/@mrpedronetinhu/configura%C3%A7%C3%A3o-de-e-mail-profissional-gratuito-1f504bb5fba7?sharedUserId=mrpedronetinhu
Blogspot: https://nettotecnologias.blogspot.com/2026/07/como-criei-meu-e-mail-personalizado.html
dg-publish: true
---
# Configuração de E-mail Profissional

## Prefácio

Faz bastante tempo, desde meu último projeto, logo, gostaria de prosseguir com uma das minhas vontades, que é possuir um e-mail `contato@nettotech.com.br`, para transmitir mais profissionalismo do que `mrpedronetinhu@gmail.com` _(kkkk sim, netinhu)_

Durante a execução do projeto, tive uma reviravolta.

---
## Sobre

Como todo projeto atual, questionei para a IA **Claude**, como eu poderia transformar meu projeto em realidade, dessa forma, ele fez uma stack do projeto, utilizando a [[Máquinas virtuais (VMs)|VM]] **Free-tier** do [[Oracle]] [[Oracle Cloud (OCI)|Cloud]] e **tunelamento de e-mail** da [[Cloudflare]].

---
## Primeira Ideia

> Desculpa o spoiler, eu venho do futuro, escrever essa etapa e dizer, que acabou não rolando, pois no meio do caminho, aprendi uma nova ferramenta, que deixa a 'stack' menor, mas caso queira aprender como subir uma instância e subir um e-mail 'self-hosted', continuar lendo.
### Criação da Instância
Prosseguir com a criação da instância

![[E-mail personalizado-1.png | 500]] ![[E-mail personalizado-2.png | 500]]

Incluir o nome `mailserver` e selecionar a imagem: `Ubuntu 24.04` Selecionando o modelo: `VM.Standard.E2.1.Micro` (Dentro do free-tier)

![[E-mail personalizado-3.png | 500]]

Pulei a parte de '_Segurança_' e prossegui para '_Networking_', na parte do '_Primary Network_', selecionei a opção: '**Create new virtual cloud network**'

Por estar criando um novo [[VCN]], será criado uma [[subnet]] publica.

Logo os parâmetros abaixo: '_Private IPv4 address assignment_' e '_Public IPv4 address assignment_' ficaram esmaecidos, pois serão criados.

Na parte de '_Add SSH keys_', selecionei '**Upload public key file (.pub)**' e fiz Upload da minha chave `~/.ssh/id_rsa.pub`

No '**Storage**', não modifiquei nada, pois para meu proposito de '**mailserver**' 46gb é mais que suficiente.

![[E-mail personalizado-4.png | 500]]

Prossegui com o '**create**' e aguardei a preparação da instância.

![[E-mail personalizado-5.png | 500]]

E após a preparação, pressionei o botão '**Start**'

![[E-mail personalizado-6.png | 500]]

---

### IP Público

Com a máquina virtual criada, foi criado o IP Privado, mas eu preciso do IP Público, para conseguir acessar via [[SSH]], então precisamos criar ele.

Para isso, acessamos a listagem de instâncias e entramos dentro da VM

![[E-mail personalizado-7.png | 500]]

Depois prosseguimos para dentro da VNIC na sessão '_Attched VNICs_'

![[E-mail personalizado-8.png | 500]]

Ao entrar no VNIC, vamos até o '**IP administration**' e editamos o **IPv4 addresses** criado:

![[E-mail personalizado-9.png | 500]]

Selecionamos o '_Reserved public IP_' e para identificação, coloquei o nome '`mailserver-ip`', ao salvar a edição, conseguiremos um IPv4 público.

![[E-mail personalizado-11.png | 500]]

---

### Configurar o Firewall

Para podermos acessar via SSH (porta 22) e configurar o servidor de e-mail, precisaremos acrescentar na regra do firewall a permissão dessas portas.

O caminho, seria: **Networking > Virtual Cloud Networks**

![[E-mail personalizado-12.png | 500]]

Depois selecione sua VCN e vá a aba '**Security**' e haverá a sessão '_Security Lists_'

![[E-mail personalizado-13.png | 500]] ![[E-mail personalizado-14.png | 500]]

E dentro da **Security List** 'Default', há a aba '_Security rules_', que iremos acrescentar essas regras.

![[E-mail personalizado-15.png | 500]] ![[E-mail personalizado-16.png | 500]]

Seguindo esse acréscimo para todas as subsequentes portas:

| Protocolo | Porta | Descrição             |
| --------- | ----- | --------------------- |
| TCP       | 22    | SSH                   |
| TCP       | 25    | SMTP (receber e-mail) |
| TCP       | 587   | Submission (enviar)   |
| TCP       | 993   | IMAP SSL              |

O '**Source CIDR**' precisa ser `0.0.0.0/0`, para poder aceitar de qualquer IP.

---

### Conectando via SSH

Como eu configurei minha chave SSH e escolhi a imagem Ubuntu, para conectar via SSH o comando será:

```bash
ssh ubuntu@<ip público>
```

> O usuário 'ubuntu' vem por padrão da imagem.

Perfeito, agora reforçando a configuração de Firewall feito na etapa anterior, prosseguimos com a configuração dentro da VM:

```bash
sudo iptables -I INPUT -p tcp --dport 25 -j ACCEPT
sudo iptables -I INPUT -p tcp --dport 587 -j ACCEPT
sudo iptables -I INPUT -p tcp --dport 993 -j ACCEPT

# Salvar regras
sudo apt install iptables-persistent -y
sudo netfilter-persistent save
```

![[E-mail personalizado-17.png | 500]]

---

### 'Abertura da porta 25'

Seguindo a pesquisa, a Oracle, bloqueia a porta 25.

para liberar, precisaremos abrir um ticket, para isso seguimos o caminho: **Support>Create Service Request** na categoria **Networking>Port 25**

o texto criado pelo Claude foi:

```
"I'm requesting the removal of the port 25 block on my tenancy to run a self-hosted mail server for my personal domain nettotech.com.br. I will configure SPF, DKIM, and DMARC records properly."
```

**Nota do autor**: obtive retorno do time de suporte da Oracle, me orientaram a utilizar o [[Oracle Email Delivery]]; Dessa forma, fui atrás de entender mais sobre o serviço e percebi que, **não há necessidade de ter criado a instância para o e-mail 'self-hosted'**.

---

### Configuração de DNS

Para o controle do [[DNS]], utilizaremos o [[Cloudflare]], incluindo no registro:

- **Direcionamento** Apontamento de um subdomínio para o endereço da VM
    - **Tipo**: A
    - **Name**: mail.nettotech.com.br
    - **IP Address**: <Endereço IP Público>
    - **Proxy**: Off
      
- **MX (Mail Exchanger)** Essa configuração, faz com que, ao mandar e-mail para exemplo: 'contato@**nettotech.com.br**', o DNS busque no domínio para onde direcionar, no nosso caso, será para o subdomínio: `mail.nettotech.com.br`
    - **Tipo**: MX
    - **Name**: `nettotech.com.br`
    - **Mail server**: `mail.nettotech.com.br`
    - **Prioridade**: 10
        - Se houver mais de um MX, o remetente tentará o menor valor
    - **Proxy**: Off
        - Pois o tráfego SMTP não faz proxy HTTP/HTTPS, indo direto para o IP da VM
          
- **SPF (Sender Policy Framework)** Lista de quem tem "permissão para mandar em nome do domínio", verificando se o e-mail vem de fato da fonte autorizada, defesa contra spoofing.
    - **Tipo**: TXT
    - **Name**: `nettotech.com.br`
    - **Conteúdo**: `v=spf1 mx ~all`
      
- **DMARC (Domain-based Message Authentication, Reporting & Conformance)** Política que diz o que fazer em caso de falhas do SPF ou DKIM, para mandar relatórios sobre.
    - **Tipo**: TXT
    - **Name**: `_dmarc.nettotech.com.br`
    - **Conteúdo**: `v=DMARC1; p=quarantine; rua=mailto:<e-mail>`
        - **`p=quarantine`**: e-mails devem ir para quarentena (spam)
        - **`rua=mailto:`**: endereço que receberá o relatório.
          
- **DKIM (DomainKeys)** Serve para que o provedor verifique se o e-mail foi enviado pelo proprietário do domínio

---

### Instalando [[Docker]]

```bash
sudo apt update && sudo apt upgrade -y
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker ubuntu
newgrp docker
```

> Primeiro, padrão, atualiza o [[apt - Advanced Package Tool|apt]], depois o comando [[cURL (Client URL)|curl]] busca o arquivo `.sh` de instalação do subdomínio do docker, depois incluí o usuário no grupo de execução do docker.

---
#### Subir o 'docker-mailserver'

Inicialmente, criaremos pastas para o repositório, depois utilizamos o [[wget]] para baixar os arquivos base.

```bash
mkdir ~/mailserver && cd ~/mailserver

# Baixa os arquivos base
wget https://raw.githubusercontent.com/docker-mailserver/docker-mailserver/master/compose.yaml
wget https://raw.githubusercontent.com/docker-mailserver/docker-mailserver/master/mailserver.env
wget https://raw.githubusercontent.com/docker-mailserver/docker-mailserver/master/setup.sh
chmod +x setup.sh
```

---

## Segunda Ideia

Pois bem, após o retorno do suporte na etapa de 'abertura da porta 25', aprendi sobre o '[[Oracle Email Delivery]]'

Logo, remove a necessidade de uma instância criada, docker e direcionamento do subdomínio 'mail.nettotech.com.br'

Para isso, utilizaremos para 
**Envio**: Thunderbird -> [[SMTP]] [[Oracle Email Delivery]] -> Destino. 
**Receber**: Cloudflare E-mail Routing -> Gmail

---

### Cloudflare Email Routing (recebimento)

Para isso, basta acessar: **Email Service > Email Routing** e prosseguir com '**Onboard Domain**'

![[E-mail personalizado2 - 1.png| 550]]

Importante, já ter registrado seu domínio no Cloudflare, para apresentar na listagem da _Zone_ e ele prosseguirá com a criação para os registros automaticamente.

![[E-mail personalizado2 - 2.png | 550]]

Após isso, no campo inferior, há o '_Add address_', preencha o e-mail e adicione.

![[E-mail personalizado2 - 3.png | 550]]

Chegará um e-mail na caixa do destino, importante você aprovar e pronto, direcionamento configurado com sucesso e de forma hiper rápida.

---

### Oracle Email Delivery (envio)

Assim, diante do 'free-tier' oferecer '100 emails por dia' e '3.000 emails por mês', sei que não alcançarei essa meta, nem se eu me candidatar em todas as vagas que ver pela frente, logo, de graça, vou prosseguir com esse serviço.

No painel Oracle -> **Email Delivery** -> **Domínios de E-mail**, prossiga com o botão _Criar Domínio de E-mail_ e insira o seu.

![[E-mail personalizado2 - 4.png | 500]]

Com o domínio de e-mail criado, acesse-o e prossiga com a aba **DKIM**

> **Reforçando**: Serve para que o provedor verifique se o e-mail foi enviado pelo proprietário do domínio

![[E-mail personalizado2 - 5.png |500]] ![[E-mail personalizado2 - 6.png | 500]]

Prossegui com a seleção de '_Adicionar novo DKIM_' e dei próximo. Chegando na etapa de **Seletor DKIM**, pedindo para criar um prefixo, podendo ser qualquer coisa mesmo para você se identificar, então selecionei 'oracle' Ao dar novamente o próximo, chegará na etapa de **Gerar registro e valor de CNAME**.

![[E-mail personalizado2 - 7.png | 500]]

O que for gerado nesse local, você precisará colocar lá no registro [[DNS]]

- **Tipo**: CNAME
	- **Name**: `<prefixo>._domainkey.<seu dominio>.`
	- **Alvo**: `<prefixo>.seudominio>.dkim.gru1.oracleemaildelivery.com`

Importante também modificar/adicionar o **SPF** 
- **Tipo**: TXT 
	- **Name**: nettotech.com.br 
	- **Conteúdo**: `v=spf1 include:rp.oracleemaildelivery.com ~all`

Dessa forma, aguarde até o '_Status DNS do Cliente_' e '_Status de Assinatura do DKIM_' esteja '**Ativo**';

Após estar ativo, prosseguiremos com a aba dentro '**Remetentes Aprovados**' e clicamos no _'Criar Remetente Aprovado_:

![[E-mail personalizado2 - 8.png| 500]]

e assim iremos cadastrar como aparecerá o e-mail, exemplo: `contato@nettotech.com.br` ou `pedro@nettotech.com.br`

![[E-mail personalizado2 - 9.png | 500]]

No menu lateral, vamos em **Configurações** e salvamos as informações que serão usadas no _Thunderbird_: 
**Servidor SMTP**, **Porta** e **Segurança**.

Mas como fazemos para cadastrar Credenciais para esses e-mails?

No canto superior direito (no icone de perfil), acesse seu perfil e procure pela aba '**Senhas salvas**' e na sessão '**Credenciais SMTP**' clique em '_Gerar credenciais_'

![[E-mail personalizado2 - 10.png | 500]] ![[E-mail personalizado2 - 11.png | 500]]

Gerando um usuário e senha gigantescos, salve-os para usar no e-mail

---

## Referências

- [Cloudflare Email Routing Documentation](https://developers.cloudflare.com/email-routing/)
- [Oracle Email Delivery Documentation](https://docs.oracle.com/en-us/iaas/Content/Email/home.htm)
- [Docker Mail Server GitHub](https://github.com/docker-mailserver/docker-mailserver)