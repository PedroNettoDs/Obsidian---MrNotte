Maioria das aplicações, precisam '*salvar informações*', e para isso que existe os **[[volumes]]**', sendo necessário que você os crie e os aponte para que o contêiner use:
```yml
volumes:
  - volumenomeado:/localização
```
Esse volume, não estará de fato 'na sua máquina', ele estará dentro do `/var/lib/docker/volumes`.

Sua estrutura seria:
```txt
origem : destino
  ↓          ↓
host     container
```

Se na origem, você nomear, será criado e gerido pelo [[Docker]].
entretanto, alternativamente há como definir: **bind mount**
```
volumes:
  - ./data:/localização 
```
Pasta localmente no seu computador

Diferença:

|              | Volume nomeado         | Bind mount                |
| ------------ | ---------------------- | ------------------------- |
| Localização  | Gerenciado pelo Docker | Pasta que você definiu    |
| Permissões   | Docker resolve         | Precisa ajustar           |
| Visibilidade | `/var/lib/docker/...`  | Direto na pasta informada |

>é um pouco confuso, pois para quem lê (vulgo eu), compreendo que o caminho: `/var/www/html` será o local aonde salvará na minha máquina, mas na máquina, ficará salvo em:
`/var/lib/docker/volumes/nextcloud_data/_data`
porém para o contêiner, esse caminho será: `/var/www/html` (internamente).