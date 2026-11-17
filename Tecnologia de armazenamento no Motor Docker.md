O [[Docker]] conta com o armazenamento de *informações das aplicações* de seus [[Contêineres|Container]], dessa forma, há como 'isolar' esses dados do sistema hospeideiro, havendo muitas formas de configurar essa proteção, mas em contra partida, há também ferramentas, para disponibilizar essas *informações das aplicações* ao host.

Sendo essa disponibilização, denominada como: **Mecanismo de Montagem**

## Mecanismo de Montagem

Para definir a forma desse acoplamento desses mecanismos, podemos utilizar formas, aonde, cada uma tem uma forma de tratar: 
- erros
- segurança no [[Kernel]]
- compatibilidade entre *orquestradores*
#### Sintaxe curta
Baseado na sinalização `-v` ou `--volume`
`origem:destino:opções`
Exemplo:
```yaml
- /path/to/config:/config
```

#### Sintaxe longa
Baseado na sinalização `--mount`
```yaml
- type: bind
source: /path/to/media
target: /media
```

---

### Volumes gerenciados (volumes)


### Acoplamentos temporários em memórias (tmpfs mounts)


### Acoplamentos de imagem (image mounts)


### Acomplamentos de vínculo (bind mounts)
Criação de uma ponte entre o armazenamento interno do container para uma parte 'acessível' do computador.
> ah! mas pedro! o armazenamento do container, já está de certa forma, dentro do computador hur dur!
> - sim, animal, mas! está criptografado, tá todo díficil de fazer acesso

"*Embora apresentem alta eficiência para fluxos específicos*" (Backup das configurações, leitura e modificação de midias ou banco de dados) "*a forte dependência da infraestrutura subjacente do hospedeiro*" (Nessa situação, aonde ser 'acessado', precise 'transitar', pode causar uma lentidão de leitura, ainda mais se houver vários conteiners ao mesmo tempo).

### Comparativos
| Mecanismo de Montagem | Localização Física do Dado                                   | Ciclo de Vida do Dado                                              | Controle de Escrita                        | Caso de Uso Primário                                                |
| --------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------ | ------------------------------------------------------------------- |
| **Volumes**           | Área isolada sob gestão do Docker `/var/lib/docker/volumes/` | Independente do ciclo de vida do contêiner; preservado em exclusão | Leitura e escrita configuráveis            | Bancos de dados e estado corporativo persistente                    |
| **Bind Mounts**       | Caminho para o sistema de arquivos do hospedeiro             | Vinculado ao hospedeiro; sobrevive à remoção do contêiner          | Leitura e escrita bidirecionais por padrão | Compartilhamento de código-fonte em desenvolvimento e configurações |
| **Tmpfs Mounts**      | Memória volátil do sistema hospedeiro (_RAM_)                | Destruído com a interrupção ou remoção do contêiner                | Temporário e de alta velocidade            | Dados sensíveis de curta duração, como chaves de criptografia       |
| **Image Mounts**      | Camadas internas de outra imagem do Docker                   | Vinculado ao ciclo de vida da imagem de origem                     | Estritamente somente-leitura               | Depuração de imagens mínimas e compartilhamento de ativos estáticos |
