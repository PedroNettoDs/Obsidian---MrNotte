---
aliases:
  - AZs
  - Região
  - Zona de Disponibilidade
---
Em um provedor de nuvem ([[Azure]], [[Google Cloud]], [[Amazon Web Services (AWS)|AWS]]), teremos a aplicação do termo: 
### Explicação
Que propriamente dito, se trata da 'Área de cobertura' e dentro dessa região, há **Zonas de disponibilidade**;

Mas para que raios serve isso?
-Vamos supor, que iremos subir uma aplicação em um servidor na *Região de São Paulo*,  logo ele será alocado a um data-center nessa região, porém para garantir que vai continuar funcionando, a provedora, inclui uma 'replica' do seu servidor em outros servidores que estiverem dentro da sua *Zona de disponibilidade*', exemplo:

#### Região:
- Virginia (us-east-1)
#### Zona de disponibilidade:
- Zone A (us-east-1a)
- Zone B (us-east-1b)
- Zone C (us-east-1c)
- Zone D (us-east-1d)
- Zone E (us-east-1e)
- Zone F (us-east-1f)

Logo, fica muito difícil uma região inteira sofrer uma paralisação