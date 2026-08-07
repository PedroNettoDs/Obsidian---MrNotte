### Sobre
[[Dispositivo de armazenamento]] podem ser divididos em **partições**.

que são 'divisões lógicas', permitindo que caso você tenha por exemplo um pendrive de 50Gb, você possa ter em um só dispositivo, duas unidades de armazenamento de 25Gb.
#### Analogia
É como se você tivesse um bolo, mas você quer repartir, para uma fatia você comer e a outra você guardar ou dar para outra pessoa.

---
### Tipo de particionamento
- [[MBR - Master Boot Record]]
	Usada desde o inicio do computador.
	**Ferramentas:**
	- `fdisk`
	- `cfdisk`
	- sfdisk
- [[GPT - GUID Partition Table]]
	Iniciada nos anos 2000, suporta multipartições
	**Ferramentas:**
	- `gdisk`
	- `cgdisk`
	- `sgdisk`
- **Ambos**
	**Ferramentas**
	- `parted`
	- `gparted`
---
### Navegação Linux
![[FHS - Filesystem Hierarchy Standard#/dev|FHS]]