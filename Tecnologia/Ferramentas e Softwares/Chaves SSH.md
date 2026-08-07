---
aliases:
  - SSH Key
tags:
  - Criptografia
---
Chaves [[SSH]] são um par de chaves [[Criptografia ]] ([[Chave Pública]] e privada) usadas para autenticar e conectar-se de forma segura a servidores remotos, substituindo senhas tradicionais por um método muito mais seguro e imune a ataques de força bruta.

## Como gerar uma chave SSH?
1. Abra o terminal e rode:
```
ssh-keygen -t ed25519 -C "email@example.com"
```

2. Digite o caminho do arquivo ou pressione "Enter para o padrão"  
    (C: Users\your username\.ssh\id_ed25519)

#### Ver a chave pública

1. Depois de concluído, navegue até o diretório **.ssh** na sua pasta de usuário para localizar as chaves geradas
2. Abra o arquivo **.pub** com um editor de texto e copie o conteúdo
3. Cole a chave no conteúdo da chave SSH
---