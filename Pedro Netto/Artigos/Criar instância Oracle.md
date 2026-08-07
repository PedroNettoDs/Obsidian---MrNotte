### Prefácio
Inicialmente, estava focado no projeto de 'E-mail personalizado'

### Roteiro
Acessando o **[[Oracle]]** (cloud.oracle.com).

#### Criação da instância
Prosseguir com a criação da instância
![[E-mail personalizado-1.png]]
 ![[E-mail personalizado-2.png]]
Incluir o nome `mailserver` e selecionar a imagem: `Ubuntu 24.04` 
Selecionando o modelo: `VM.Standard.E2.1.Micro` (Dentro do free-tier)
	![[E-mail personalizado-3.png]]

Pulei a parte de '**Security**' e prossegui para '**Networking**', 
	na parte do '*Primary Network*', selecionei a opção: '**Create new virtual cloud network**'
		
Por estar criando um novo [[VCN]], será criado uma [[subnet]] publica.
		
Logo os parâmetros abaixo: 
'*Private IPv4 address assignment*' e '*Public IPv4 address assignment*' ficaram esmaecidos, pois serão criados.

Na parte de '*Add SSH keys*', selecionei  '**Upload public key file (.pub)**' e fiz Upload da minha chave `~/.ssh/id_rsa.pub`

No '**Storage**', não modifiquei nada, pois para meu proposito de '**mailserver**' 46gb é mais que suficiente.
	![[E-mail personalizado-4.png]]
Prossegui com o '**create**' e aguardei a preparação da instância. 
	![[E-mail personalizado-5.png]]
E após a preparação, pressionei o botão '**Start**	
	![[E-mail personalizado-6.png]]

---
#### IP Público
Com a máquina virtual criada, foi criado o IP Privado, mas eu preciso do IP Público, para conseguir acessar via [[SSH]], então precisamos criar ele.

Para isso, acessamos a listagem de instâncias e entramos dentro da VM
	![[E-mail personalizado-7.png]]

Depois prosseguimos para dentro da VNIC na sessão '*Attched VNICs*'
	**![[E-mail personalizado-8.png]]**

Ao entrar no VNIC, vamos até o '**IP administration**' e editamos o **IPv4 addresses** criado:
	![[E-mail personalizado-9.png]]

Selecionamos o '*Reserved public IP*' e para identificação, coloquei o nome '`mailserver-ip`', ao salvar a edição, conseguiremos um IPv4 público.
	![[E-mail personalizado-11.png]]

---
#### Configurar o Firewall
Para podermos acessar via SSH (porta 22) e configurar o servidor de e-mail, precisaremos acrescentar na regra do firewall a permissão dessas portas.

O caminho, seria: **Networking > Virtual Cloud Networks**
	![[E-mail personalizado-12.png]]
Depois selecione sua VCN e vá a aba '**Security**' e haverá a sessão '*Security Lists*'
	![[E-mail personalizado-13.png]]
	![[E-mail personalizado-14.png]]

E dentro da **Security List** 'Default', há a aba '*Security rules*', que iremos acrescentar essas regras.
	![[E-mail personalizado-15.png]]
	![[E-mail personalizado-16.png]]

Seguindo esse acréscimo para todas as subsequentes portas:

| Protocolo | Porta | Descrição             |
| --------- | ----- | --------------------- |
| TCP       | 22    | SSH                   |
| TCP       | 25    | SMTP (receber e-mail) |
| TCP       | 587   | Submission (enviar)   |
| TCP       | 993   | IMAP SSL              |
O '**Source CIDR**' precisa ser `0.0.0.0/0`, para poder aceitar de qualquer IP.

---
#### Conectando via SSH
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
![[E-mail personalizado-17.png]]
