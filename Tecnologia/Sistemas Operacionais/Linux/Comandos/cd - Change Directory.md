---
aliases:
  - cd
  - Change Directory
---
o comando CD no [[Linux]], é usado para navegar e alterar entre [[Diretórios]], simples assim, porém temos alguns ~~feitiços~~ parâmetros para utilizar

Normalmente, ao utilizar:
```bash
cd nome/do/diretorio
```
faz com que seja navegado até aquele diretório, aparecendo na frente da linha de comando a localização atual: `~nome/do/diretorio$`
> O `~` siginifica que está dentro do 'home/<usuário>'

## Parâmetros:
- `cd ..`
	Volta para o diretório anterior
	
- `cd -`
	Retorna para o último diretório que estava
	
- `cd /`
	Move para o diretório raiz ([[root]]) do sistema