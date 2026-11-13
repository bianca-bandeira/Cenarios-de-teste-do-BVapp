'''
UC008 - Indicadores de contas e cobranças

Objetivo: Permitir que o tesoureiro veja, no topo das listagens, a quantidade
e o valor total de registros (total, pagos, em aberto, atrasados e canceladas) calculados
sobre o período filtrado.

Requisitos:
- RF050502 (Indicadores de contas e cobranças)

Ator:
- Tesoureiro

Autor: Bianca Rodrigues Bandeira
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# Pré-condição: o tesoureiro está autenticado e existem os registros
# descritos em DADOS (período 01/10/2026 a 30/11/2026).

# O ator acessa a listagem de contas a pagar na página "Contas a Pagar".

# O sistema exibe, no topo, os indicadores, cada um com quantidade e valor
# total: Total, Pagos, Em aberto e Atrasados. [RN1]

# O ator verifica os valores das contas a pagar:
# - Total: 2 registros, R$ 2.000,00
# - Pagos: 0 registros, R$ 0,00
# - Em aberto: 1 registro, R$ 1.200,00
# - Atrasados: 1 registro, R$ 800,00
# - Cancelados: 0 registros, R$ 0,00

# O ator acessa a listagem de contas a receber na página de "Cobranças".

# O ator verifica os valores das cobranças:
# - Total: 2 registros, R$ 450,00
# - Pagos: 1 registro, R$ 150,00
# - Em aberto: 1 registro, R$ 300,00
# - Atrasados: 0 registros, R$ 0,00
# - Cancelados: 0 registros, R$ 0,00

# O ator acessa a visão geral.

# O ator verifica os valores da visão geral:
# - Total: 4 registros, R$ 2.450,00
# - Pagos: 1 registro, R$ 150,00
# - Em aberto: 2 registros, R$ 1.500,00
# - Atrasados: 1 registro, R$ 800,00
# - Cancelados: 0 registros, R$ 0,00

# ---------------------------------------------------------------
# 🟠 [A1] - INDICADORES ACOMPANHAM O PERÍODO FILTRADO


# O ator filtra o período de vencimento de 01/11/2026 a 30/11/2026.

# O sistema recalcula os indicadores apenas com os registros do período:
# - Contas a pagar: Total 1 (R$ 1.200,00); Em aberto 1 (R$ 1.200,00);
#   Pagos 0; Atrasados 0.
# - Cobranças: Total 1 (R$ 300,00); Em aberto 1 (R$ 300,00); Pagos 0;
#   Atrasados 0.
# - Visão geral: Total 2 (R$ 1.500,00). [RN2]


# ---------------------------------------------------------------
# 🟠 [A2] - SEM REGISTROS NO PERÍODO

# O ator filtra um período sem registros (01/01/2025 a 31/01/2025).

# O sistema exibe todos os indicadores zerados (quantidade 0 e valor R$ 0,00).
# [RN3]


# ---------------------------------------------------------------
# 🟠 [A3] - COOPERADO NÃO VISUALIZA OS INDICADORES

# O "cooperado Carlos Mendes" autentica-se e acessa as suas telas.

# O sistema não exibe indicadores. [RN4]


# ---------------------------------------------------------------
# 🟠 [A4] - ADMINISTRADOR NÃO VISUALIZA OS INDICADORES

# O "administrador" autentica-se e acessa a listagem.

# O sistema não exibe os indicadores, pois somente o Tesoureiro os visualiza.
# [RN4]

# ---------------------------------------------------------------

# 🟣 [RN1] Para contas a pagar, contas a receber e visão geral, o sistema exibe quantidade e valor total de registros: total, pagos, em
# aberto, atrasados e cancelados.
# 🟣 [RN2] Os indicadores são calculados sobre o período filtrado.
# 🟣 [RN3] Na ausência de registros, os indicadores aparecem zerados.
# 🟣 [RN4] Somente o Tesoureiro visualiza os indicadores.


# [DADOS] DADOS E RESULTADOS ESPERADOS
# ---------------------------------------------------------------

# Data atual considerada no teste: 09/11/2026 (fictícia).
# Registros do período 01/10/2026 a 30/11/2026:
# - Contas a pagar: Conta de energia (Atrasada, R$ 800, venc. 20/10) e
#   Aluguel da sede (Aberta, R$ 1.200, venc. 25/11)
# - Cobranças: Mensalidade novembro/2026 (Aberta, R$ 300, venc. 10/11) e Taxa
#   manutenção (Paga, R$ 150, venc. 15/10)
#
# Resultado esperado: os indicadores descritos em cada fluxo acima.