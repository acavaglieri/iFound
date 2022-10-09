---------------------
---------------------
App Python / FastAPI
---------------------
---------------------

---------------------
0.0.8 - x/Jul/2022
---------------------
    StarkBank:
        - Correção para criação de workspaces únicas no momento do cadastro do usuário
    Monitoramento:
        - Adição do elastic search
    Pagamentos:
        - Refatoração na listagem
        - Início de implementação de rotina para automatizar pagamentos agendados
        - Adicionada flag 'pay_on_schedule' na tabela 'payments' para filtrar pagamentos já pagos de forma instantânea dos agendados
    Usuário:
        - Adicionado campo de complemento de endereço
    Tasks:
        - Finalização task para realizar pagamentos agendados
    Migrations:
        - Merge de todas as migrations em uma só
        - Adicionada seed para usuário com a workspace padrão
    README:
        - Adicionada doc de novos campos obrigatórios no arquivo .env

---------------------
0.0.7 - 25/Jan/2022
---------------------
  Bugs:
   Corrigido bugs de query inconsistente e autenticação inválida surgidos com a implementação do JWT.

---------------------
0.0.6 - 18/Jan/2022
---------------------
  Segurança:
   Inserido controle por JWT.

---------------------
0.0.5 - 07/Dez/2021
---------------------
   Fluxo de Pagamento por PIX:
      - Verificação de saldo adicionada
      - Resolvido bug de realizar pagamento para si mesmo

---------------------
0.0.4 - 22/Nov/2021
---------------------
   Blockchain:
      - Funcionando para invoices e transactions ao pagar
      - 422 ao receber webhook do StarkBank corrigido

---------------------
0.0.3 - 08/Nov/2021
---------------------
   Rotas de Integração com APIs de Bancos Criadas:
      - Criação de contas
      - Autenticação
      - Buscando saldo da conta
      - Realizando cobranças e transações
      - Obtendo histórico de transações

   Fluxo de Users:
      - Export XLSX

   Rake para export/import PIX

---------------------
0.0.2 - 22/Out/2021
---------------------
   Schemas:
      - Fluxo de PIX Completo
      - Rakes para testes com APIs de Bancos
      - Integração com Rotas Básicas do StarkBank

---------------------
0.0.1 - 19/Out/2021
---------------------
   Versão inicial
      - CRUD Users completo
      - Alembic e Alchemy
      - Models: Users
