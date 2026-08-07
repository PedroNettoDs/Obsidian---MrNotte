é um servidor multimídia moderno e de baixa latência que unifica o processamento de áudio e vídeo, substituindo antigos sistemas como [[Pulse|PulseAudio]] e JACK, oferecendo melhor desempenho, suporte a aplicativos [[Flatpak]] sandboxed, e recursos essenciais para compartilhamento de tela no [[Wayland]]. 

Ele gerencia fluxos de áudio e vídeo, atuando como uma camada de compatibilidade para que programas antigos funcionem, enquanto permite um controle mais refinado e seguro para novas aplicações

https://www.youtube.com/watch?v=tIj6sgTkk38

**Principais Funções e Benefícios:**

- **Unificação:** Gerencia áudio (ALSA, PulseAudio, JACK) e vídeo, substituindo múltiplos sistemas.
- **Baixa Latência:** Ideal para produção musical e jogos, com processamento de áudio e vídeo em tempo real.
- **Segurança (Sandbox):** Permite que aplicativos em contêineres (como Flatpaks) acessem áudio/vídeo de forma segura, com permissões controladas.
- **Compartilhamento de Tela:** Essencial para o compositor Wayland, facilitando a captura de tela e área de trabalho remota.
- **Compatibilidade:** Possui módulos para emular PulseAudio e JACK, garantindo que programas legados continuem funcionando.