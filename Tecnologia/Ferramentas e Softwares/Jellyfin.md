### Sobre
Jellyfin é uma aplicação que hospeda seus vídeos e distribui para sua rede, te transformando basicamente dono de sua própria Netflix, aonde você decide o que entrará no catálogo ou não.

### Processo de instalação
Para preparar a sua instalação, utilizarei o [^1][[Portainer.io]], e então seguiremos para: **Stack>Create Stack**  

**Nome**: Jellyfin (deeer)
```yaml
services:
	jellyfin:
		image: jellyfin/jellyfin
		container_name: jellyfin
		user 1000:1000
		ports:
			- 8096:8096/tcp
		    - 7359:7359/udp
		volumes:
	      - /home/netto/docker/jellyfin/config:/config
	      - /home/netto/docker/jellyfin/cache:/cache
```

>Obs: criei o diretório antes do docker, mas supostamente, ele criaria. 

**user**:
	Define qual 'usuário' o [[Contêineres|Container]] do [[Docker]] rodará no kernel.
**type: bind**:
	 para mais informações: [[Tecnologia de armazenamento no Motor Docker]]

https://medium.com/@bruno.beltrame/jellyfin-seu-pr%C3%B3prio-servi%C3%A7o-de-streaming-e0b056cd3139

[^1]: Já preparei material sobre essa ferramenta e como instala-la
