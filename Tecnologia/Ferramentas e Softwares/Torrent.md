**Sobre o Torrent e o Protocolo BitTorrent**
O Torrent, ou 'BitTorrent', é um protocolo online de compartilhamento e download de arquivos baseado na arquitetura P2P (_peer-to-peer_ ou ponto-a-ponto), criado pelo programador Bram Cohen em 2001.

Diferente do modelo tradicional de download via cliente-servidor em que todos baixam de uma única fonte, o Torrent permite que o mesmo arquivo seja baixado a partir de vários distribuidores simultaneamente. No sistema P2P, cada dispositivo (computador ou smartphone) funciona como servidor e cliente ao mesmo tempo.
Dessa forma, ao baixar um arquivo, o usuário passa automaticamente a atuar como servidor desse mesmo conteúdo para outras pessoas.

**Como funciona na prática: O Enxame (_Swarm_)**

No modelo cliente-servidor, baixar um arquivo hospedado em um servidor distante, como na Oceania, poderia causar lentidão, indisponibilidade de link ou perda de pacotes devido a problemas de taxa de transferência, com o BitTorrent resolve essa questão.

Se o servidor da Oceania disponibilizar o arquivo no formato '.torrent', a outra máquina utilizando o Torrent, ele começa a "semear" (fazer o _upload_) do conteúdo.
Quando um usuário de outra região, por exemplo, nos Estados Unidos, consegue esse '.torrent' e assim começa a fazer o download, ele é tratado como um _Leecher_ (sanguessuga), pois está se 'aproveitando da rede', após ou durante o processo de download a máquina começa a compartilhar as partes já baixadas, tornando-se um _Seeder_ (semeador).

Isso cria uma rede de distribuição contínua, quanto mais usuários baixam o arquivo, mais pontos de disponibilização surgem para os próximos interessados.
Essa colaboração torna o download cada vez mais rápido, formando uma rede descentralizada de distribuição chamada de "Enxame" (_Swarm_) assim, quanto mais o arquivo é semeado, menor é a parcela de dados que precisa ser transferida de um único computador.

Para coordenar tudo isso, garantir a veracidade dos arquivos e atestar que não foram corrompidos ou modificados, existem os Rastreadores (_Trackers_).
Eles identificam o _Swarm_ de computadores que possuem o arquivo e controlam qual máquina enviará qual pedaço de arquivo para os novos clientes (_Leechers_).

![[Pasted image 20260824110019.png]]  _(Legenda: O cliente original do BitTorrent era bem simples - Crédito: Reprodução/Rainberry, Inc.)_

**Resiliência e Acesso**

Essa descentralização e disponibilização comunitária tornam a rede extremamente resistente, pois ela não depende de um servidor central. 
O acesso aos arquivos ocorre de duas maneiras: através de um pequeno arquivo ".torrent" (facilmente transferido entre os usuários) ou de um "Link Magnético" (_Magnet Link_), que funciona de maneira similar a uma URL.

Logo, o protocolo se mostrou altamente eficiente para o compartilhamento de arquivos grandes (como filmes, músicas e jogos), pois divide esses arquivos em pequenos pedaços, baixando-os de múltiplos usuários simultaneamente e economizando os altos custos de banda servidores, no entanto, pelo fato de o acesso aos downloads ser gratuito, o protocolo passou a ser comumente associado à pirataria.

**O início e a "evangelização" da tecnologia**

O trabalho de divulgação (ou "evangelização") do BitTorrent começou com Bram Cohen na DefCon, um evento voltado para hackers existente desde 1996.
Na edição que ocorreu até 16 de julho de 2001, Cohen apresentou sua ideia ao público.
Ele disponibilizou as primeiras versões do programa em seu próprio site: `[http://bitconjurer.org/](http://bitconjurer.org/)`.

![[Pasted image 20260824173501.png]]

O objetivo principal do protocolo era resolver a clássica lentidão causada quando vários usuários solicitavam o mesmo arquivo de um único servidor. Para popularizar a ferramenta e atrair os primeiros usuários, Cohen começou a divulgar o BitTorrent nas comunidades do Yahoo.

![[Pasted image 20260824173759.png]] 
_(Legenda: Print de 2008 da postagem de Bram Cohen no Yahoo WayBackMachine)_

**Precursores e o Diferencial do BitTorrent**
Apesar de revolucionária, essa filosofia de transferência ponto-a-ponto descentralizada e fatiar arquivos grandes não nasceu apenas com o BitTorrent.
Existiu também por exemplo o 'Mojo Nation, eMule, Kazaa e entre outros', com tecnologias que possuíam o mesmo princípio _peer-to-peer_, mas o problema é que os semeadores eram um único usuário, com isso, um download poderia demorar muito e precisava ter uma conexão ou todo o arquivo era perdido/corrompido.
O BitTorrent, ao oferecer uma solução aberta e eficiente visando a diminuição de custos de banda larga, se tornou a forma como compartilhamos arquivos peer-to-peer na internet. 

**Funcionamento**
O software busca coletar fragmentos de um arquivo de vários computadores que estejam semeando, para que possa ser direcionado ao cliente para montar o arquivo completo.
Para garantir que a integridade desse arquivo, utilizamos o arquivo com a extensão '.torrent', arquivo esse que contém informações como: endereço do **servidor tracker**, nome, tamanho e hash de um arquivo.
O [[Hash]] é um código matemático que transforma dados e seus tamanhos em sequência de números, garantindo que o arquivo não foi modificado, exemplo, caso alguém contamine o arquivo, seu tamanho será diferente do que registrado no .torrent e no hash, logo, é descartado de ser compartilhado

**Comunidade e pirataria**

O que acontece se eu criar dois .torrents com o mesmo hash?


_(Referências: Diolinux / MeioBit)_

https://diolinux.com.br/tecnologia/o-que-e-torrent-e-sua-importancia.html#

https://meiobit.com/467895/bittorrent-25-anos-historia/