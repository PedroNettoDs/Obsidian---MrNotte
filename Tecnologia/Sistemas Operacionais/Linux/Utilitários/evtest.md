Ferramenta de baixo nível que lê os eventos diretamente do [[Kernel]]
sendo um subsistema de [[evdev]].

```bash
sudo evtest

#Ele lista todos os dispositivos de entrada disponíveis, por exemplo:

/dev/input/event0    AT Translated Set 2 keyboard
/dev/input/event1    MSI Gaming Keyboard
/dev/input/event2    Logitech USB Mouse
...
Select the device [0-9]:

#Você escolhe o número do seu teclado MSI e pressiona Enter. A partir daí, qualquer tecla pressionada gera uma saída como:

Event: time 1234567.89, type 1 (EV_KEY), code 125 (KEY_LEFTMETA), value 1
```

![[evtest-exemple.png]]