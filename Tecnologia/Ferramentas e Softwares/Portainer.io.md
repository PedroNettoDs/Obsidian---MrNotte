Um software para controle de [[Kubernetes]], [[Docker]] e [[Podman]]

Sua instalação pode ser feita através do próprio [[Docker]]:
```bash
docker run -d -p 9000:9000 --name portainer --restart always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer -H unix:///var/run/docker.sock
```