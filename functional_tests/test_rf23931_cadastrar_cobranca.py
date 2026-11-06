'''
UC001 - Cadastrar cobrança com dados válidos

Objetivo: Permitir que o tesoureiro cadastre uma nova cobrança associada a um
cooperado, com campos obrigatórios e opcionais, recebendo uma confirmação.

Requisitos:
- RF23931
- US - Cadastro de cobrança

Ator:
- Tesoureiro

Autor: Bianca Rodrigues Bandeira

Observação: cobrança NÃO é parcelável. O parcelamento pertence a contas a
pagar (no banco, cobranças e contas a pagar compartilham a tabela "conta").
Nos cenários, toda cobrança tem 1 parcela.
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# Pré-condição: o tesoureiro está autenticado e existe um cooperado cadastrado.

# O ator acessa a área de cadastro de cobranças.

# O ator observa que o formulário possui os campos:
# - Nome da cobrança (obrigatório)
# - Identificador do cooperado (obrigatório)
# - Valor total (obrigatório)
# - Status (obrigatório)
# - Quantidade de parcelas (obrigatório)
# - Intervalo (obrigatório)
# - Juros (obrigatório)
# - Tipo de juros (obrigatório)
# - Recorrência (obrigatório) (recorrente ou única)
# - Descrição (opcional)
# - Data de lançamento (opcional)
# - Opções: botão para salvar

# O ator preenche todos os campos obrigatórios e os opcionais com dados válidos. [A1] [A2]

# O ator seleciona a opção para salvar.

# O sistema valida os dados conforme as regras. [RN1] [RN2]

# O sistema registra a cobrança e exibe uma mensagem de confirmação.

# O ator verifica que a cobrança foi registrada para o cooperado informado.


# 🟠 [A1] - CADASTRAR SEM OS CAMPOS OPCIONAIS
# ---------------------------------------------------------------

# O ator preenche somente os campos obrigatórios, deixando vazios descrição e data de lançamento.

# O sistema registra a cobrança normalmente e exibe a confirmação. [RN2]


# 🟠 [A2] - COBRANÇA RECORRENTE VÁLIDA
# ---------------------------------------------------------------

# O ator marca a cobrança como recorrente, informa 1 parcela e intervalo diferente de zero.

# O sistema registra a cobrança e exibe a confirmação.


# 🟣 [RN1] CAMPOS OBRIGATÓRIOS
# ---------------------------------------------------------------

# Nome, identificador do cooperado, valor total, status, quantidade de
# parcelas, intervalo, juros e tipo de juros são obrigatórios.

# 🟣 [RN2] CAMPOS OPCIONAIS
# ---------------------------------------------------------------

# Descrição e data de lançamento podem ficar vazios.

# 🟣 [RN3] VALOR PADRÃO DA RECORRÊNCIA
# ---------------------------------------------------------------

# Sem recorrência informada, a cobrança é considerada não recorrente (única).


# [DADOS] DADOS E RESULTADOS ESPERADOS
# ---------------------------------------------------------------

# Dados de teste (fictícios):
# - Nome: "Mensalidade novembro/2026"; Cooperado: "Carlos Mendes"
# - Valor total: 300,00; Status: Aberta; Parcelas: 1; Intervalo: 30
# - Juros: 2%; Tipo de juros: simples
# - Descrição: "Cobrança de teste"; Data de lançamento: 05/11/2026
#
# Resultado esperado:
# - Cobrança registrada para Carlos Mendes, com os dados informados.
# - Mensagem de confirmação exibida.
