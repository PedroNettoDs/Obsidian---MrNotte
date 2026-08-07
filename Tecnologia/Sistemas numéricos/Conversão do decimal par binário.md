Para a conversão do [[Decimal]] para [[Binário]]
### Decimal
É bem simples, diante que, você precisa pegar o número desejado e prosseguir dividindo por dois. 

![[ConverterDecimalBinario.png]]
Exemplo, convertendo: **25 para binário**
>*25 dividido por 2*, dá **12.5**, com sobra, então é **1**
>>esse 0.5 é uma sobra, logo contará como 1.
>*12 divido por 2*, dá **6**, sem sobra, então colocamos: **0**
 *6 dividido por 2*, dá **3**, sem sobra, então colocamos: **0**
 *3 dividido por 2*, dá **1.5**, com sobra, então é **1**.
 *1 divido por 2*, dá **1**, sem sobra, porém o resultado foi **1**
 
Logo finalizamos nossa conversão, temos os número:
`10011`,  porém precisamos 'inverter' a ordem, então fica: `11001`

---
### Decimal Fracionário
Mas e se houver 'números quebrados'?
*25 + 0.4375 = 25.4375*, já sabemos que **25** é `11001`

para encontrar o `0.4375` que é um *número decimal fracionário (menor que 1)*, *em vez de dividir, dobramos repetidamente a fração* até dar 1

![[Exemplo - Conversão do decimal par binário.png]]
Exemplo, convertendo **0.4375 para binário**
> *0.4375 vezes 2*, dá **0.875**, começa **0**
> *0.875 vezes 2*, dá **1.75**, começa com **1**, então pegamos ele.
> *0.75 vezes 2*, dá **1.5**, começa com **1**, então pegamos ele.
> *0.5 vezes 2*, dá **1.0**, começa com **1**, então pegamos ele.

Finalizamos nossa conversão e temos o número: `0111`, assim fazemos a junção novamente de '*25 + 0.4375 = 25.4375*,' porém dessa vez em binário, ficando: `11001.0111`

---
### Digito mais Significativo
Em números inteiros, o dígito *mais a direita* é dito como "*dígito menos significativo*" (**Least Significant Bit** = **LSBy**).

Logo o dígito '*não nulo*' *mais a esquerda* é o "*dígito mais significativo*" (**Most Significant Bit** = **MSBy**)
 ![[Exemplo - Digito mais Significativo.png]]


https://www.facom.ufu.br/~ronaldooliveira/APC-2018-2/Aula2-SistemasNumericos.pdf