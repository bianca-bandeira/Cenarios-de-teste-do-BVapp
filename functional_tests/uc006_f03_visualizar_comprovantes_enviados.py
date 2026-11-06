'''
UC006 - Visualizar comprovantes enviados (tesoureiro)

Objetivo: Permitir que o tesoureiro consulte, na área de cobrança por
cooperado, os comprovantes enviados, identificando pagamento, conta e usuário.

Requisitos:
- Feature 03
- CA05, CA09
- US - Visualizar comprovantes de pagamentos de contas e cobranças

Ator:
- Tesoureiro

Autor: Bianca Rodrigues Bandeira
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# Pré-condição: o tesoureiro está autenticado e possui permissão para
# visualizar comprovantes; existem comprovantes enviados por dois
# cooperados (A e B).

# O ator acessa a área de cobrança por cooperado.

# O sistema apresenta os comprovantes disponíveis.

# O ator verifica que cada comprovante identifica:
# - O pagamento
# - A conta
# - O usuário responsável pelo envio

# O ator verifica que o comprovante do cooperado A aparece vinculado ao
# usuário A e ao respectivo pagamento, e o do cooperado B ao usuário B.

# O ator seleciona um comprovante.

# O sistema exibe o arquivo do comprovante para consulta.


# 🟠 [A1] - SEM COMPROVANTES DISPONÍVEIS
# ---------------------------------------------------------------

# O ator acessa a área de cobrança de um cooperado sem comprovantes.

# O sistema não apresenta comprovantes.


# 🟠 [A2] - USUÁRIO SEM PERMISSÃO
# ---------------------------------------------------------------

# Um usuário autenticado sem permissão tenta acessar os comprovantes.

# O sistema não apresenta comprovantes.


# 🟣 [RN1] IDENTIFICAÇÃO NA LISTAGEM
# ---------------------------------------------------------------

# A listagem identifica pagamento, conta e usuário responsável pelo envio.


# 📦 [DADOS] DADOS E RESULTADOS ESPERADOS
# ---------------------------------------------------------------

# Dados de teste:
# - Cooperado A: pagamento 1, comprovante "comprovante_a.pdf"
# - Cooperado B: pagamento 2, comprovante "comprovante_b.png"
#
# Resultado esperado:
# - Dois comprovantes listados, cada um com pagamento, conta e usuário de
#   envio corretos; arquivo exibido ao selecionar.
