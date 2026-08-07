- **Asterisco** ( `*` ) :
	Corresponde a sequência de caracteres ou nenhuma
	**Exemplo**:
```bash
# exemplo:
~/Documents$ cat red.txt
red
reef
rot
reeed
rd
rod
roof
reed
root
reel
read

sysadmin@localhost:~/Documents$ grep 're*d' red.txt
red
reeed
rd
reed

#lista todos os arquivos com extensão .txt:
ls *.txt

#Lista arquivos que começam com 'relatorio':
ls relatorio*

#lista arquivos que contêm 'backup' em qualquer posiçao:
ls *backup*
```
	
- **Interrogação** (`?`):
	Correspondências exatas a um caractere em posição específica
**Exemplo**:
```bash
# Um único caractere no após o local especificado:
# Aparece: arquivo1.txt, arquivoA.txt, Arquivo_.txt
# Não aparece: arquivo10.txt, arquivo.txt
ls arquivo?.txt

# Qualquer dígito no lugar específico:
# Aparece: log_2022-01.txt, log_2023-01.txt, log_2023-01.txt
ls log_202?-01.txt

# Somente 3 caracteres no nome:
# Aparece: run.sh, fix.sh, apt.sh
# Não aparece: deploy.sh, ok.sh
ls ???.sh
```
	
- **Colchetes** (`[]`):
	Define um conjunto de caracteres permitidos para uma posição específica.
**Exemplo**:
```bash
# exemplo:
~/Documents$ cat profile.txt
Hello my name is Joe.
I am 37 years old.
3121991
My favorite food is avocados.
I have 2 dogs.
123456789101112

~/Documents$ grep '[0-9]' profile.txt
I am 37 years old.
3121991
I have 2 dogs.
123456789101112


# Apenas os dígitos 1, 2 ou 3 naquela posição
# se houver arquivos numerados, 1,2,3,4,5,6... só vai selecionar 1,2 e 3:
ls foto[123].jpg

# Apenas arquivos que começam com vogal minúscula:
# se o arquivo for 'log.txt', não aparece, pois não começa com vogal.
ls [aeiou]*

# Negação da seleção atual:
# se o arquivo for 'log.txt', aparece, pois não começa com vogal :D
ls [!aeiou]*

# Intervalo de conjuntos:
# seleciona somente as fotos 1,2 e 3
ls foto[1-3].jpg
```
	
- **Ponto**  (`.`): 
	Corresponde a qualquer caractere.
```bash
# exemplo:
$ ~/Documents$ cat red.txt
red
reef
rot
reeed
rd
rod
roof
reed
root
reel
read
$ ~/Documents$ grep 'r..f' red.txt
reef
roof

# Corresponde a 'bat', 'cat', 'hat', 'mat', etc.
grep 'b.t' arquivo.txt

# Corresponde a qualquer palavra de 3 letras que termine com 'at':
grep '..t' arquivo.txt
```
	
- **Circunflexo** (`^`): 
	Se for o **primeiro** caractere do padrão, exige que o padrão esteja no **início da linha**:
```bash
# Apenas linhas que começam com 'root':
grep '^root' /etc/passwd

# Linhas que começam com letra maiúscula:
grep '^[A-Z]' arquivo.txt
```

- **Cifrão** (`$`): 
	Se for o **último** caractere do padrão, exige que o padrão esteja no **fim da linha**:
```bash
# Apenas linhas que terminam com 'bash':
grep 'bash$' /etc/passwd

# Linhas vazias (início seguido imediatamente do fim):
grep '^$' arquivo.txt
```