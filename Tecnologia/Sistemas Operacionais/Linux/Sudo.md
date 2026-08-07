"Superuser do"

Onde fica a configuração do **sudo** no [[Linux]]?
`/etc/sudoers.d/`
> Não se edita o arquivo sudoers!

`sudo visudo -f /etc/sudoers.d/netto`
ou
`echo "netto ALL=(ALL) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/netto`

Para configurar um usuário para poder utilizar o sudo sem necessariamente utilizar o comando e inserir sua senha, podemos seguir com 