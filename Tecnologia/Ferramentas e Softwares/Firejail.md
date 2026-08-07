### Sobre
é um utilitário para [[Linux]], com a opção nativa para cortar a internet de programas, criando um '**Sandbox**'

### Instalação
```sh
sudo apt install firejail
```

### Funcionalidades
- **Separar das pastas do sistema**
	- Se houver, um [[Ransomware]], ele não conseguirá modificar outros arquivos.
- **Separar a rede do sistema**
	- Coloca um IP diferente para o software enjaulado
- **Escolher um DNS**
	- Definimos um DNS específico para o programa utilizar.
- **Subir [[Xorg]] separado**
	Prevenindo certos problemas de segurança.

https://plus.diolinux.com.br/t/firejail-o-que-e-e-como-usar/33387