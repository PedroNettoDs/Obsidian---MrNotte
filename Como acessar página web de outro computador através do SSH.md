Em muitos momentos, via [[SSH]] executaremos um comand, que iniciará um serviço ou instalador e seria necessário assim, abrir o navegador daquele computador, mas perceba que estamos via SSH, não temos acesso possivelmente a RDP ou visual para abrir o navegador.

Então para isso, utilizaremos o [[SSH Tunneling]]:
```
ssh -L 8080:localhost:8080 usuario@ip_da_maquina_remota
```

- **`-L`**: Diz ao SSH que você quer fazer um redirecionamento local (Local Forwarding).
- **`8080` (o primeiro)**: É a porta que será aberta no **seu computador**.
- **`localhost:8080`**: É o destino final dentro da máquina remota (se o serviço lá estiver rodando na porta 3000, por exemplo, mude para `localhost:3000`).
- **`usuario@ip_da_maquina_remota`**: Seus dados normais de acesso SSH.