
| Arquitetura   | Bits | [[CPU\|Processador]]es típicos | Uso comum                   |
| ------------- | ---- | ------------------------------ | --------------------------- |
| **[[amd64]]** | 64   | Intel / AMD                    | PCs e servidores            |
| **[[arm64]]** | 64   | ARM modernos                   | Celulares, Macs, servidores |
| **[[armhf]]** | 32   | ARM antigos                    | IoT, Raspberry Pi antigos   |

- **PC ou notebook comum:** `amd64`
- **Celular, Raspberry Pi recente, Mac M1+:** `arm64`
- **Dispositivo ARM antigo:** `armhf`

Para verificar sua arquitetura o comando seria:
```bash
uname -m
```

