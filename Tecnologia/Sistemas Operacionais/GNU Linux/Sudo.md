### Sobre 
Sudo é a abreviação de "Superuser do"

### Acrescentar usuários no sudo
Fui para o [[Debian]] e sofri para utilizar o comando `sudo`, precisei incluir meu usuário no arquivo de configuração do sudo.
Para isso, acessei o usuário *root* com o comando `su` e prossegui com o editor nano: `nano /etc/sudoers`
e procurei o `root    ALL=(ALL:ALL) ALL` e inclui abaixo:
```
# User privilege specification
root    ALL=(ALL:ALL) ALL
netto   ALL=(ALL:ALL) ALL
```
sai do usuário *root* com o comando `exit` e validei o funcionamento adequado do sudo no meu usuário.

### Localização
Onde fica a configuração do **sudo** no [[Linux]]?
`/etc/sudoers.d/`
> Não se edita o arquivo sudoers!

`sudo visudo -f /etc/sudoers.d/netto`
ou
`echo "netto ALL=(ALL) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/netto`

-

Para configurar um usuário para poder utilizar o sudo sem necessariamente utilizar o comando e inserir sua senha, podemos seguir com