```bash
sudo nano /etc/sysctl.conf
```

Use o código com cuidado.

2. Adicionar as linhas de bloqueio

Vá até o final do arquivo e adicione as seguintes linhas:

text

```
# Desativar IPv6 em todas as interfaces
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1
net.ipv6.conf.lo.disable_ipv6 = 1
```

Use o código com cuidado.

- Salve o arquivo pressionando `Ctrl + O`, confirme com `Enter` e saia com `Ctrl + X`.

3. Aplicar as alterações imediatamente

Para carregar as novas configurações sem precisar reiniciar o computador, execute:

bash

```
sudo sysctl -p
```

Use o código com cuidado.

---

Como confirmar que o IPv6 foi desativado?

Execute o comando de listagem de IP:

bash

```
ip a show enp1s0f0
```

Use o código com cuidado.