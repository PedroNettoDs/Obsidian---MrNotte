---
dg-publish: true
---
### Prefacio
Estava estudando sobre [[Criptografia]] e [[SSL]]/[[TLS]] e acabei compreendendo que eles são fundamentais para que o [[HTTP (Hypertext Transfer Protocol)|HTTP]] tenha o S de Seguro, se tornando assim o [[HTTPS (Hypertext Transfer Protocol Secure)|HTTPS]].
Porém, percebi que eu estava somente no entendimento teórico, queria elaborar algo mais prático, dessa forma, pedi auxilio ao Claude para montar um ambiente de teste.
Para esse experimento, vamos utilizar ferramentas já conhecidas, como [[Wireshark]] e [[TCPdump]] para analisarmos os pacotes passando pela rede, pois bem, para deixar mais visível a comunicação, irei hospedar o site de autenticação em uma [[Máquinas virtuais (VMs)|VM]] através do [[virt-manager]].

---

### Preparando o ambiente
#### Página Web
Para o projeto, solicitei para o Claude Code criar uma página web com [[Flask]], com duas modalidades de login: HTTP e HTTPS.
link do repositório [aqui](https://github.com/PedroNettoDs/lab-http-https)
> **Dica**: baixe o repositório na sua máquina host e transmita a pasta através do comando: `scp ./lab-http-https user@IpVm:/local`  

#### Máquina Virtual
Com a máquina virtual já criada, prossegui com a coleta do IP dela através do comando:
```bash
➜  ~ sudo virsh domifaddr <nome_vm>  
Nome       Endereço MAC        Protocolo     Endereço  
-------------------------------------------------------------------------------  
vnet6      52:54:00:bf:2b:c3    ipv4         192.168.122.145/24
```
Assim, mandei a pasta da página web, através do '[[SCP]]':
```bash
scp -r /home/netto/Dev/lab-http-https netto@192.168.122.145:/home/netto/
```

Conectando na VM, fui até a pasta do projeto e prossegui com a execução do `./setup.sh`, garantindo assim que esteja tudo devidamente instalado:

![[Analisando como funciona a critografia do HTTPS-1.png]]

O próprio setup irá pontuar, se estiver tudo certo para a execução do:
`sudo python3 app.py`, que deixará o servidor Flask rodando:

![[Analisando como funciona a critografia do HTTPS-2.png]]

Com o servidor web online, prosseguimos acessando no navegador do host:
![[Analisando como funciona a critografia do HTTPS-3.png]]
### HTTP (Sem criptografia)
Para testarmos, abriremos o Wireshark e por se tratar de uma VM configurado no modo NAT, a interface que iremos monitorar, será a `vnet`, utilizando o filtro: `tcp.port == 80`.

Com isso configurado, abrimos o navegador, acessamos o site damos login:

![[Analisando como funciona a critografia do HTTPS-4.png]]

Dessa forma o pacote será capturado no Wireshark, aonde poderemos avaliar através do pacote semelhante a esse: 
```
510	761.058179864	192.168.122.1	192.168.122.145	HTTP	554	POST /login-http HTTP/1.1  (application/x-www-form-urlencoded)
```

Que os dados de usuário e senha vão estar abaixo do 'cabeçalho' (informações que ficam acima do conteúdo).
![[Analisando como funciona a critografia do HTTPS-5.png]]
![[Analisando como funciona a critografia do HTTPS-6.png]]

Logo, fica fácil demais um 'man-in-middle' conseguir capturar sua senha.
### HTTPS (Com criptografia)
Com o servidor Flask rodando na VM, seguimos para o host, aonde vamos precisar salvar o `log` para descriptografarmos o HTTPS.
**COMO ASSIM?**, isso foi o que mais me gerou dúvidas, durante o laboratório, mas então compreendi que

Quando você executar esse comando:
```bash
export SSLKEYLOGFILE=~/ssl-keys.log
```
você já precisa saber que, o [[TLS]] escreverá a chave da conexão HTTPS no nessa variável '*SSLKEYLOGFILE*', logo o comando serve para você SALVAR em um arquivo na sua /home, utilizando essa chave para descriptografar o tráfego.

Sofri bastante, mas comando que me ajudou a conseguir esse 'ssl-keys.log' foi no **terminal do HOST**: 
```bash
SSLKEYLOGFILE="$PWD/sslkeys.log" curl -k https://<IpVm>/login-https -d "username=admin&password=123456"
```

Dessa forma, consegui colocar as mãos no `ssl-keys.log` e incluí ele dentro do protocolo TLS *(Edit>Preferences>Protocols>TLS>**(Pre)-Master-"Secret log filename**")*:
![[Pasted image 20260715175746.png]]

Vale avaliar, que sem o `sslkeys.log` o trafego numeral 14, fica descrito, somente como '**Application Data**': 
![[Pasted image 20260715175841.png]]

E quando imposto o `sslkeys.log` podemos ver que ele é traduzido para seu formato real.

![[Pasted image 20260715175407.png]]

Assim, conseguimos concluir nosso laboratório com sucesso

https://unit42.paloaltonetworks.com/wireshark-tutorial-decrypting-https-traffic/