---
aliases:
  - Message Queuing Telemetry Transport
---
crProtocolo de comunicação máquina para máquina (M2M - Machine to Machine) com foco em [[IoT]] (Internet das coisas), tendo como base o protocolo [[TCP|TCP/IP]], utilizado pelo [[Mosquitto]] para realização de 'Post' e 'Get', sendo considerado um protocolo simples e de baixo consumo de dados além de possibilitar a comunicação bilateral.

![[MQTT.png]]

Criado pela [[IBM]], utilizando microcontroladores para comunicar várias máquinas entre si.

Mas antes, importante compreender o padrão de funcionamento do MQTT:
### Publish-subscribe
Ciente que existe o '[[Request-Response]]', aonde o servidor fica o tempo todo ouvindo requisições, fazendo com que o cliente estabeleça conexões temporárias, obtendo suas respostas.
e o **Observer**, que é uma conexão baseada em observação, aonde o servidor recebe uma lista de inscrição de observadores (cliente), que se interessam em saber de qualquer mudança, o **sujeito** (servidor), ao notar mudança, dispara as informações para a lista.

Agora chegamos em fim no '**Publish-subscribe**', que é muito parecido com o '*Observer*', porém com uma diferença, o '**Broker**' que é uma espécie de 'filtro e direcionamento' das mensagens, para seu lugar apropriado, se acordo com '*inscrição do tópico*' (Temperatura sala C)


https ://www.gta.ufrj.br/ensino/eel878/redes1-2019-1/vf/mqtt/