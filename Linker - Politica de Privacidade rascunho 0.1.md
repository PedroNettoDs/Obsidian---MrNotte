1. **Dados e campos em aberto**
    - **Identificação corporativa:** Preencher as informações e sedes da empresa nos Estados Unidos (`[EMPRESA_EUA]`, `[ENDEREÇO_EUA]`) e no Brasil (`[EMPRESA_BR]`, `[CNPJ]`, `[ENDEREÇO_BR]`).
    - **Contatos e Encarregado:** Definir o e-mail de privacidade (`[E-MAIL_PRIVACIDADE]`), o nome do Encarregado de Dados (`[NOME_ENCARREGADO]`) e os canais de atendimento (`[E-MAIL_ATENDIMENTO]`).
    - **Prazos regulatórios e operacionais:** Inserir os prazos de prova de acordos (`[PRAZO_DE_PROVA]`), retenção de posições de deslocamento (`[PRAZO_DA_POSIÇÃO]`), rotação de backups (`[PRAZO_DE_BACKUP]`), prazo de recurso nos EUA (`[PRAZO_DO_RECURSO]`) e os destinos regulatórios pendentes (`[DESTINO_DAS_MENSAGENS]`, `[DESTINO_DO_REGISTRO]`).
    - **Metadados:** Atualizar a data de publicação (`[DATA DE PUBLICAÇÃO]`) e a versão (`[1.0]`).
    - **Parceiros e fornecedores (Seção 8.2):**Preencher todos os provedores listados como **[A IMPLEMENTAR]** (hospedagem, e-mail, monitoramento, pagamento e tradução).
2. **Alinhamentos práticos (funcionalidades marcadas como [A IMPLEMENTAR])**
    - **Módulo de avaliações:** Garantir que o sistema consiga coletar notas/comentários e aplicar a regra de anonimização do autor ("Usuário anterior") em caso de encerramento de conta.
    - **Registros de acesso (Marco Civil):** Validar se a infraestrutura do app realmente armazena de forma sigilosa e segura o IP, data e hora de cada acesso pelo período legal de 6 meses (seção 15.8).
    - **Encerramento de conta autônomo:** Disponibilizar a interface para que o usuário possa encerrar a conta diretamente pelo aplicativo.
    - **Provedores de tradução:** Assegurar que os dados enviados à DeepL e ao Google Cloud Translation limitem-se estritamente ao texto e idioma, sem reuso para treinamento de IA.
    - **Canais de suporte:** Confirmar a efetiva operação dos canais de atendimento e e-mails de privacidade informados.
3. **Riscos e pontos de atenção para análise jurídica**
    - **Retenção de dados a longo prazo:** A política prevê que o Linker não apaga registros para manter o histórico de serviços e acordos rastreável (seção 10.1). É preciso validar se essa retenção perpétua (mesmo com anonimização parcial) atende aos princípios de minimização da LGPD e da CCPA.
    - **Manutenção de mensagens após o encerramento:** O texto indica que as mensagens enviadas continuam visíveis para os destinatários após o encerramento da conta remetente (seção 10.3). Deve-se avaliar o risco de exposição continuada de dados pessoais eventualmente inseridos no corpo das conversas.
    - **Autodeclaração de documentos:** O app coleta uma declaração de documentos para prestadores nos EUA, mas isenta-se expressamente de armazenar status migratório ou documentos de identidade (seção 2.1b, 2.4). Cabe à jurídica avaliar a robustez dessa abordagem frente às normas trabalhistas e de compliance locais.
    - **Auditoria de SDKs:** Embora o documento garanta a ausência total de ferramentas de rastreamento ou publicidade de terceiros, é imprescindível realizar uma checagem técnica no código do aplicativo para mitigar o risco de conformidade com SDKs oculto