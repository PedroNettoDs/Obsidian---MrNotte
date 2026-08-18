Ferramenta que simula ações de teclado e mouse

Entre suas simulações estão:
#### Teclas:
```bash
xdotool key Menu          # Pressiona a tecla Menu
xdotool key ctrl+c        # Simula Ctrl+C (copiar)
xdotool key super         # Pressiona a tecla Windows/Super
xdotool key alt+F4        # Fecha a janela atual
```

#### Digitação:
```bash
xdotool type "Olá mundo"  # Digita o texto
```

#### Mouse
```bash
xdotool mousemove 500 300        # Move o cursor para x=500, y=300
xdotool click 1                  # Clica com botão esquerdo
xdotool click 3                  # Clica com botão direito
xdotool click 2                  # Clica com botão do meio
```

#### Gerenciar janelas
```bash
xdotool getactivewindow          # Retorna o ID da janela ativa
xdotool windowminimize <id>      # Minimiza uma janela
xdotool windowfocus <id>         # Foca em uma janela
```

---
## Instalação:
```bash
sudo apt install xdotool
```