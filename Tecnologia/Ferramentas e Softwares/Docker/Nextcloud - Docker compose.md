Pois bem, decidi rodar o '[[Nextcloud]]' localmente com [[Docker]] e aprender mais sobre como funciona e suas funcionalidades.

Assim então solicitei a criação de um '*docker-compose.yml*' para o Claude e vamos estudar o que cada linha significa.

#### Código final:
```yml
services:
  nextcloud:
    image: nextcloud:latest
    container_name: nextcloud
    restart: unless-stopped
    ports:
      - "8080:80"
    volumes:
      - nextcloud_data:/var/www/html
    environment:
      - MYSQL_HOST=db
      - MYSQL_DATABASE=nextcloud
      - MYSQL_USER=nextcloud
      - MYSQL_PASSWORD=senha123
    depends_on:
      - db

  db:
    image: mysql:8.0
    container_name: nextcloud_db
    restart: unless-stopped
    volumes:
      - db_data:/var/lib/mysql
    environment:
      - MYSQL_ROOT_PASSWORD=root123
      - MYSQL_DATABASE=nextcloud
      - MYSQL_USER=nextcloud
      - MYSQL_PASSWORD=senha123

volumes:
  nextcloud_data:
  db_data:
```
---
#### Estrutura:
`services` - Serviço, propriamente dito, é o que ficará rodando.

`image:` você precisa pontuar qual imagem você usará, para isso, há duas alternativas:
1. você pontuar exatamente qual é a imagem, aonde ele buscará no [Docker Hub](https://hub.docker.com/) no momento que subir o '**docker compose up**'
2. realizar antes o "**docker pull 'nome'**" que também buscará no [Docker Hub](https://hub.docker.com/).
Pois em nosso caso, iremos pontuar a imagem: `nextcloud:latest` para seleção do [[Nextcloud]] mais atualizado.

`container_name:` definimos como vai aparecer o nome do contêiner: `nextcloud`.

`restart: unless-stopped` define para reiniciar o contêiner toda vez que o computador reiniciar/desligar, para parar com isso, precisa do `docker stop`.

`ports:` - Propriamente dito, configura as portas que o contêiner irá usar, nesse caso Nextcloud utiliza: `"8080:80"` 

agora prosseguimos com a criação de '**[[volumes]]**' que esse contêiner usará.
```yml
volumes:
  - nextcloud_data:/var/www/html
```
Dessa forma o [[Nextcloud]], criará internamento no contêiner:
```
/var/www/html/
├── config/        # configurações (database, domínio, etc.)
├── data/          # arquivos dos usuários
├── apps/          # aplicativos instalados
├── themes/        # temas
└── index.php      # entrada da aplicação
```

```txt
origem : destino
  ↓          ↓
host     container
```
>é um pouco confuso, pois para quem lê (vulgo eu), compreendo que o caminho: `/var/www/html` será o local aonde salvará na minha máquina, mas na máquina, ficará salvo em:
`/var/lib/docker/volumes/nextcloud_data/_data`
porém para o contêiner, esse caminho será: `/var/www/html` (internamente).

Como o [[Nextcloud]] utiliza o banco de dados  [[MySQL]], precisamos definimos os [^1]environment.
```yml
environment:
  - MYSQL_HOST=db
  - MYSQL_DATABASE=nextcloud
  - MYSQL_USER=nextcloud
  - MYSQL_PASSWORD=senha123
```
Assim, informamos o nome do **host do banco de dados** `MYSQL_HOST=db`;
o **nome do banco de dados**: `MYSQL_DATABASE=nextcloud`;
**criamos um usuário** e **sua senha**: `MYSQL_USER=nextcloud` e `MYSQL_PASSWORD=senha123`.

`depends_on:`, basicamente diz que 'só suba a imagem após esse estiver pronto', no nosso caso `- db`, pois só subirá a aplicação se tiver o banco de dados.

Agora definimos justamente o serviço do **banco de dados**, novamente prosseguimos com a especificação do nome do serviço e a imagem
```yml
db:
    image: mysql:8.0
```
obs: ainda estamos dentro da **[^2][[indentação]]** do '`services`'

especificamos o local que ficará salvo 'internamente':
```yml
volumes:
  - db_data:/var/lib/mysql
```
> O [[Docker]] cria e gerencia esse **[[volumes]]** automaticamente em: `/var/lib/docker/volumes/nextcloud_data/_data`
---

Com base nisso, montamos o `docker-compose.yml` e prosseguimos com o comando:
```bash
docker compose up
```


[^1]: ![[environment]]

[^2]: ![[indentação]]
