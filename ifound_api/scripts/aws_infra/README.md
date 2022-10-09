Para o RDS criar um MariaDB.
- Criar o banco de dados dentro do RDS.
O security group desse RDS precisa apenas:
- Permitir ENTRADA a MARIADB 3306 de qualquer IP.
- Permitir SAIDA a todas as portas e qualquer IP.

Para criar uma EC2 use Ubuntu 20.04, Mariadb não é 100% compatível com AWS Linux.
O security group dessa EC2 precisa apenas:
- Permitir ENTRADA a SSH 22 de qualquer IP.
- Permitir ENTRADA a HTTP 80 de outro security group (que será o do target group)
- Permitir SAIDA a todas as portas e qualquer IP.

Crie um target group apontando para essa EC2:
O security group desse target group precisa apenas:
- Permitir a ENTRADA a HTTP 80 de qualquer IP.
- Permitir SAIDA a todas as portas e qualquer IP.

Crie um elastic load balance do tipo application.
Ele deve ler apenas:
- A porta 80 fazendo redirect para 443 dele mesmo.
- A porta 443 enviado para o target group.
Configure um WAF para este ELB com as proteções que julgar pertinente.

Crie um apontamento do tipo CNAME no Route53, do nome que quiser para o ELB.

Resultado:
A EC2 permite apenas conexão SSH para internet, mas ela consegue acessar RDS e enviar email e se atualizar.
O endpoint do route53 será acessivel apenas por HTTPS e protegido por WAF.

As dependencias para criação da EC2 e scripts estão no run.sh comentados.
Também existem facilitadores comentados para troca de arquivos.