---
aliases:
  - curl
  - cURL
  - client-URL
---
O `curl` (client-URL) é uma ferramenta de [[Código aberto]] por [[Linha de comando|CLI]], utilizada para **Transferência de dados e arquivos** entre computador cliente e um servidor.

Desenvolvido inicialmente por Daniel Stenberg em 1997, permite utilizar uma vasta gama de protocolos: [[HTTPS (Hypertext Transfer Protocol Secure)|HTTPS]], [[HTTPS (Hypertext Transfer Protocol Secure)|HTTPS]], [[FTP]], [[FTPS]], [[SCP]], [[SFTP]], [[TFTP]], [[LDAP]], [[IMAP]], [[POP3]], [[SMTP]], [[MQTT]].

A estrutura básica do comando é:
```bash
curl [opções] <url>
```
 ---
#### Para que serve o cURL

- **Interação com APIs**: Enviar e receber dados de [[API - Interface de Programação de Aplicações]]s [[RESTful]] (GET, POST, PUT, etc.).
- **Testes de Conectividade**: Verificar se um servidor está respondendo e como.
- **Download de Arquivos**: Baixar arquivos da #web.
- **Automação**: Usado em scripts para transferências de dados.
- **Debugging**
    : Inspecionar cabeçalhos [[HTTP (Hypertext Transfer Protocol)]] para entender respostas de servidores
---
## Parâmetros 
| Opção                  | Descrição                   |
| ---------------------- | --------------------------- |
| `-h, --help`           | Mostra ajuda                |
| `--manual`             | Mostra manual completo      |
| `-V, --version`        | Mostra versão do curl       |
| `-q`                   | Ignora `.curlrc`            |
| `--config <file>`      | Usa arquivo de configuração |
| `--disable`            | Desativa opção              |
| `--enable`             | Ativa opção                 |
| `--libcurl <file>`     | Gera código usando libcurl  |
| `--trace <file>`       | Log completo                |
| `--trace-ascii <file>` | Log em [[ASCII]]            |
| `--trace-time`         | Adiciona timestamp ao trace |
| `--verbose, -v`        | Saída detalhada             |

---
### Controle de saída

| Opção                 | Descrição                          |
| --------------------- | ---------------------------------- |
| `-o, --output <file>` | Salva saída em arquivo             |
| `-O, --remote-name`   | Usa nome do arquivo remoto         |
| `--output-dir <dir>`  | Diretório de saída                 |
| `-s, --silent`        | Modo silencioso                    |
| `-S, --show-error`    | Mostra erro mesmo com `-s`         |
| `-f, --fail`          | Falha silenciosamente em erro HTTP |
| `--fail-with-body`    | Falha mantendo corpo               |
| `--stderr <file>`     | Redireciona erros                  |
| `--no-progress-meter` | Sem barra de progresso             |
| `--progress-bar`      | Barra simples                      |

---
### Redirecionamentos

| Opção                | Descrição                     |
| -------------------- | ----------------------------- |
| `-L, --location`     | Segue redirecionamentos       |
| `--location-trusted` | Envia credenciais em redirect |
| `--max-redirs <num>` | Limite de redirecionamentos   |

---
### [[HTTP (Hypertext Transfer Protocol)|HTTP]] / [[HTTPS (Hypertext Transfer Protocol Secure)]]

| Opção                     | Descrição               |
| ------------------------- | ----------------------- |
| `-X, --request <method>`  | Método HTTP             |
| `-H, --header <header>`   | Cabeçalho customizado   |
| `-I, --head`              | Apenas cabeçalhos       |
| `-d, --data <data>`       | Envia dados POST        |
| `--data-raw`              | Dados sem processamento |
| `--data-binary`           | Dados binários          |
| `--data-urlencode`        | Codifica dados          |
| `-G`                      | Força GET com dados     |
| `-A, --user-agent <ua>`   | User-Agent              |
| `-e, --referer <url>`     | Referer                 |
| `-b, --cookie <data>`     | Envia cookies           |
| `-c, --cookie-jar <file>` | Salva cookies           |
| `--compressed`            | Aceita gzip/br          |
| `--http1.1`               | Força HTTP/1.1          |
| `--http2`                 | Força HTTP/2            |
| `--http3`                 | Força HTTP/3            |

---
### Autenticação

| Opção                  | Descrição           |
| ---------------------- | ------------------- |
| `-u, --user user:pass` | Autenticação básica |
| `--anyauth`            | Auto-detecta auth   |
| `--basic`              | Auth básica         |
| `--digest`             | Digest              |
| `--ntlm`               | NTLM                |
| `--negotiate`          | Kerberos            |
| `--bearer <token>`     | OAuth Bearer        |

---
### [[HTTPS (Hypertext Transfer Protocol Secure)]] / [[SSL]]

| Opção             | Descrição              |
| ----------------- | ---------------------- |
| `-k, --insecure`  | Ignora certificado     |
| `--cacert <file>` | CA customizada         |
| `--capath <dir>`  | Diretório de CAs       |
| `--cert <file>`   | Certificado cliente    |
| `--key <file>`    | Chave privada          |
| `--cert-type`     | Tipo do cert           |
| `--tlsv1.2`       | Força TLS 1.2          |
| `--tlsv1.3`       | Força TLS 1.3          |
| `--ssl-no-revoke` | Não verifica revogação |

---
### Upload / Download

|Opção|Descrição|
|---|---|
|`-T, --upload-file <file>`|Upload|
|`-C, --continue-at <offset>`|Retomar download|
|`--limit-rate <rate>`|Limita velocidade|
|`--range <range>`|Download parcial|

---
### [[FTP]] / [[SFTP]] / [[SCP]]

| Opção               | Descrição       |
| ------------------- | --------------- |
| `--ftp-create-dirs` | Cria diretórios |
| `--ftp-pasv`        | Modo passivo    |
| `--ftp-ssl`         | [[FTP]] com SSL |
| `--sftp`            | Usa SFTP        |
| `--scp`             | Usa SCP         |
| `--key <key>`       | Chave [[SSH]]   |
| `--pubkey <key>`    | Chave pública   |

---
### [[Proxy]]

| Opção                    | Descrição       |
| ------------------------ | --------------- |
| `-x, --proxy <proxy>`    | Proxy           |
| `--proxy-user user:pass` | Auth proxy      |
| `--proxy-anyauth`        | Auto auth proxy |
| `--noproxy <list>`       | Ignora proxy    |

---
### [[DNS]] / Rede

| Opção                     | Descrição         |
| ------------------------- | ----------------- |
| `--resolve host:port:ip`  | DNS manual        |
| `--connect-timeout <sec>` | Timeout conexão   |
| `--max-time <sec>`        | Timeout total     |
| `--retry <num>`           | Repetições        |
| `--retry-delay <sec>`     | Delay             |
| `--retry-max-time <sec>`  | Tempo máximo      |
| `--interface <name>`      | Interface de rede |
| `-4`                      | Força IPv4        |
| `-6`                      | Força IPv6        |

---
### Outros

| Opção                   | Descrição           |
| ----------------------- | ------------------- |
| `--json`                | Envia [[JSON]]      |
| `--etag-save <file>`    | Salva ETag          |
| `--etag-compare <file>` | Usa ETag            |
| `--parallel`            | Downloads paralelos |
| `--parallel-max <num>`  | Limite paralelo     |
