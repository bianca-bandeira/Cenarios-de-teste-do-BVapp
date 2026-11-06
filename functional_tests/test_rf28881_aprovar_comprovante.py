'''
UC007 - Visualizar e aprovar comprovante

Objetivo: Permitir que o tesoureiro visualize um comprovante e o aprove,
atualizando comprovante, data de pagamento da parcela e status da conta.

Requisitos:
- RF28881
- US - Visualizar comprovante de cobrança

Ator:
- Tesoureiro

Autor: Bianca Rodrigues Bandeira
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# Pré-condição: o tesoureiro está autenticado e existe um comprovante enviado
# por um cooperado (status "pendente").

# O ator acessa a tela de cobranças por cooperado, seleciona uma cobrança com comprovante anexado e solicita a visualização.

# O sistema exibe o comprovante.

# O ator verifica que existem as opções "Confirmar pagamento" e "rejeitado". [RN1]

# O ator seleciona "Confirmar pagamento".

# O sistema atualiza o status do comprovante para "aprovado". [RN2]

# O sistema registra o identificador do tesoureiro e a data e o horário da
# decisão, em UTC. [RN3] 

# O sistema atualiza a data de pagamento da parcela com a data de envio do comprovante.

# O sistema recalcula o status da conta vinculada à parcela. [RN4]

# O ator verifica que o comprovante está "Paga", que a parcela possui a
# data de pagamento igual à data_upload e que o status da conta foi atualizado conforme as regras existentes.


# 🟠 [A1] - PARCELA JÁ POSSUÍA OUTRA DATA DE PAGAMENTO
# ---------------------------------------------------------------

# A parcela já tinha uma data de pagamento diferente da data_upload.

# O sistema não substitui a data de pagamento. 


# 🟠 [A2] - HORÁRIO REGISTRADO EM UTC
# ---------------------------------------------------------------

# O ator executa o FP em um fuso diferente de UTC.

# O sistema registra a data e o horário da decisão em UTC, e não no horário local. [RN3]


# 🟠 [A3] - SAIR SEM DECIDIR
# ---------------------------------------------------------------

# O ator visualiza o comprovante e volta sem escolher uma opção.

# O sistema mantém comprovante, parcela e conta sem alterações.


# 🟣 [RN1] O tesoureiro só pode escolher "aprovado" ou "rejeitado".
# 🟣 [RN2] Aprovação: status do comprovante = "Paga".
# 🟣 [RN3] Registrar tesoureiro responsável e data/hora da decisão em UTC.
# 🟣 [RN4] Recalcular o status da conta após a aprovação.


# [DADOS] DADOS E RESULTADOS ESPERADOS
# ---------------------------------------------------------------

# Dados de teste:
# - Tesoureiro "tesoureiro1"; cooperado A; conta 1; parcela 1 sem data de
#   pagamento; comprovante com data_upload = 05/11/2026.
#
# Resultado esperado:
# - Comprovante: "aprovado".
# - Análise: tesoureiro1 + data/hora UTC.
# - Parcela 1: data de pagamento = 05/11/2026.
# - Conta 1: status recalculado pelas regras existentes.
