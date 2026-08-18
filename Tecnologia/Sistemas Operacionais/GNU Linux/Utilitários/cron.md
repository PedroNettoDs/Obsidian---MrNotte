---
aliases:
  - Crontab
  - Cronjobs
  - Cron
---
### **Sobre**:
O `cron` é um utilitário do [[Linux]] para Agendamento de tarefas, sendo gerenciada pela 'Tabela de cron' `crontab`;
Suas tarefas são denominadas de `cronjobs`.

---
### **Funcionalidade**
```bash
crontab -e                  # Edita o crontab do usuário atual
crontab -l                  # Lista as tarefas do usuário atual
crontab -r                  # Remove o crontab do usuário atual
crontab -ri                 # Remove, mas pede confirmação antes

sudo crontab -u joao -e     # Edita o crontab do usuário "joao"
sudo crontab -u joao -l     # Lista as tarefas do usuário "joao"

# Sintaxe de uma linha dentro do crontab
* * * * * comando
│ │ │ │ │
│ │ │ │ └─ Dia da semana (0-7, sendo 0 e 7 = domingo)
│ │ │ └─── Mês (1-12)
│ │ └───── Dia do mês (1-31)
│ └─────── Hora (0-23)
└───────── Minuto (0-59)

# Exemplo prático:
30 2 * * 1 /scripts/backup.sh   # Toda segunda-feira às 02:30
```
---
Por padrão a tabela de um usuário fica armazenada dentro de: `/var/spool/cron/crontabs`
Enquanto os agendamentos globais, ficam em: `/etc/crontab`

---
### **Controle de usuário**
Para manter o controle de quem pode realizar o [[CRUD]] do Cron.
Há dois arquivos que podem ser configurados:

- `etc/cron.allow`
	Ao inserir o usuário ao arquivo, permite que esse usuário edite o 'crontab'
	
- `etc/cron.deny`
	Ao inserir o usuário ao arquivo, bloqueia e não permite a edição do 'crontab'
---

### **Monitoramento**
Para realizar a verificação dos logs, utilizamos o comando:
```bash
cat /var/log/syslog | grep CRON >> /tmp/cron.log
```
---
#### Dica:
Em sua documentação, muito se diz da importância de sempre deixar a última linha em branco ao incluir um novo agendamento, para evitar bugs.

---
Fonte:
https://medium.com/totvsdevelopers/entendendo-o-crontab-607bc9f00ed3
https://guialinux.uniriotec.br/crontab/