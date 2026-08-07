>**Nota 04/06/2026**: Pois bem, agora no inicio do uso de [[Linux]], estou sofrendo muito para apagar as pastas que contém arquivos kkk, sei que o comando é `rmdir` porém, preciso de parâmetros a mais para isso.

A solução seria incluir os seguintes parâmetros:

- `-r`:  recursivo (entra em subdiretórios)
- `-f`: força, sem pedir confirmação

Então pedro! o comando [[Bash]] correto para excluir é:
```bash
sudo rm -rf /pasta
```
> Perceba que não é '`rmdir`' , isso pois esse comando só é para *diretórios vazios*, frescura? sim eu sei.

