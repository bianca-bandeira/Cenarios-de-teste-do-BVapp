'''
# UC005_UC006 - Análise de comprovante de pagamento (confirmação e rejeição)

# Objetivo: Permitir que o tesoureiro visualize os comprovantes pendentes e decida pela aprovação ou rejeição do pagamento, 
# atualizando a parcela, a cobrança, registrando a análise e notificando o cooperado quando aplicável.

# Requisitos:
# - RF050402

# Ator:
# - Tesoureiro

# Autor: Bianca Rodrigues Bandeira 
'''

# 🟢 [FP] - FLUXO PRINCIPAL (APROVAÇÃO)
# ---------------------------------------------------------------

# Pré-condição: o tesoureiro está autenticado. "Carlos Mendes" enviou em 08/11/2026 um comprovante "Em análise" 
# para a parcela da "Mensalidade novembro/2026" (R$ 300,00, vencimento 10/11/2026, status "Aberta").

# O ator acessa a fila de comprovantes pendentes.

# O sistema exibe a fila, mostrando para cada item o nome do cooperado, a
# parcela e o comprovante. [RN1_A]

# O ator verifica que aparece "Carlos Mendes", a parcela da conta "Mensalidade novembro/2026" e o comprovante.

# O ator seleciona o comprovante.

# O sistema exibe o arquivo do comprovante e as opções disponíveis ("Aprovar pagamento" e "Rejeitar").

# O ator seleciona "Aprovar pagamento". [A5_A]

# O sistema altera o status da parcela para "Paga". [RN2_A]

# O sistema define a data de pagamento como a data de envio do comprovante
# (08/11/2026), e não a data da análise. [RN3_A] [A2_A]

# O sistema altera o status do comprovante para "Confirmado". [RN2_A]

# O sistema recalcula o status da cobrança. [RN4_A]

# O sistema registra o tesoureiro responsável e a data e a hora da análise. [RN5_A]

# O ator verifica que o comprovante saiu da fila de pendentes e que a parcela
# está "Paga" com a data de pagamento 08/11/2026.

# ---------------------------------------------------------------
# 🟢 [FP-ALT] - FLUXO PRINCIPAL ALTERNATIVO (REJEIÇÃO)


# Pré-condição: O tesoureiro seleciona um comprovante "Em análise" de "Carlos Mendes" 
# para a parcela da "Mensalidade novembro/2026".

# O ator seleciona "Rejeitar".

# O sistema solicita o motivo da rejeição. [RN1_R]

# O ator informa o motivo "Comprovante ilegível" e confirma. [A3_R] [A4_R]

# O sistema altera o status do comprovante para "Rejeitado", mantendo o
# registro em histórico, sem exclusão física. [RN2_R] [A6_R]

# O sistema faz a parcela voltar ao status correspondente ao vencimento
# ("Aberta" para vencimento futuro ou "Atrasada" para vencimento passado). [RN3_R] [A1_R] [A2_R]

# O sistema recalcula o status da cobrança. [RN4_R]

# O sistema registra o tesoureiro responsável e a data e a hora da análise. [RN5_R]

# O sistema notifica o cooperado do motivo da rejeição. [RN6_R]

# O ator verifica que o comprovante saiu da fila de pendentes.

# ---------------------------------------------------------------
# 🟠 [A1_A] - PARCELA ATRASADA (APROVAÇÃO)

# A parcela tem vencimento 01/11/2026 e status "Atrasada", com comprovante enviado em 08/11/2026.

# O ator confirma o pagamento.

# O sistema altera a parcela para "Paga" com a data de pagamento 08/11/2026. [RN2_A] [RN3_A]

# ---------------------------------------------------------------
# 🟠 [A2_A] - DATA DE PAGAMENTO É A DE ENVIO, NÃO A DA ANÁLISE

# O tesoureiro confirma o comprovante dias depois do envio.

# O sistema define a data de pagamento como a data de envio do comprovante, e não a data da aprovação do comprovante. [RN3_A]

# ---------------------------------------------------------------
# 🟠 [A3_A] - RECALCULAR O STATUS DA COBRANÇA (APROVAÇÃO)

# A cobrança possui duas parcelas e o ator confirma o comprovante de uma delas.

# O sistema recalcula o status da cobrança conforme as regras de atualização existentes. [RN4_A]

# ---------------------------------------------------------------
# 🟠 [A1_R] e [A2_R] - RESTAURAÇÃO DE STATUS POR VENCIMENTO (REJEIÇÃO)

# Parcela A (vencimento posterior à data atual): o sistema deixa o status "Aberta". [RN3_R]

# Parcela B (vencimento anterior à data atual): o sistema deixa o status "Atrasada". [RN3_R]

# ---------------------------------------------------------------
# 🟠 [A3_R] - REJEIÇÃO SEM MOTIVO

# O ator seleciona "Rejeitar" e tenta confirmar sem informar o motivo.

# O sistema não processa a rejeição e informa que o motivo é obrigatório. [RN1_R]

# O ator verifica que comprovante, parcela e cobrança não foram alterados.

# ---------------------------------------------------------------
# 🟠 [A4_R] - MOTIVO SOMENTE COM ESPAÇOS

# O ator informa apenas espaços como motivo e tenta confirmar.

# O sistema trata como motivo vazio e não processa a rejeição. [RN1_R]

# ---------------------------------------------------------------
# 🟠 [A4_A] / [A6_A] / [A5_R] / [A6_R] - PERMISSÕES E HISTÓRICO

# O "cooperado Carlos Mendes" tenta acessar a fila de validação e o sistema nega o acesso;
# o cooperado vê apenas os seus comprovantes. [RN6_A]

# Comprovante de despesa anexado pelo tesoureiro com status "Aprovado" não é exibido na fila de pendentes. (Ver RF050401, UC002.)

# O cooperado acessa a listagem de seus comprovantes, visualiza o "Rejeitado" com o motivo e anexa um novo. [RN6_R]

# Após a rejeição, verifica-se o banco de dados e o comprovante continua existindo com status "Rejeitado" e o motivo. [RN2_R]

# ---------------------------------------------------------------
# 🟠 [A5_A] - SAIR SEM DECIDIR

# O ator visualiza o comprovante e volta à fila sem escolher uma opção.

# O sistema mantém comprovante, parcela e cobrança sem alterações.

# ---------------------------------------------------------------

# 🟣 [RN1_A] A fila de pendentes exibe o nome do cooperado, a parcela e o comprovante.

# 🟣 [RN2_A] Confirmar pagamento: a parcela passa para "Paga" e o comprovante para "Aprovado".

# 🟣 [RN3_A] A data de pagamento é a data de envio do comprovante.

# 🟣 [RN4_A] O status da cobrança é recalculado.

# 🟣 [RN5_A/R] São registrados o tesoureiro responsável, a data e a hora da análise.

# 🟣 [RN6_A] Somente o Tesoureiro visualiza comprovantes de outros usuários; o cooperado vê apenas os seus.

# 🟣 [RN1_R] O motivo da rejeição é obrigatório.

# 🟣 [RN2_R] O comprovante passa para "Rejeitado" e é mantido em histórico, sem exclusão física.

# 🟣 [RN3_R] A parcela volta ao status correspondente ao vencimento (Aberta ou Atrasada).

# 🟣 [RN4_R] O status da cobrança é recalculado.

# 🟣 [RN6_R] O cooperado é notificado do motivo da rejeição.


# [DADOS] DADOS E RESULTADOS ESPERADOS
# ---------------------------------------------------------------

# Dados de teste:

# - Tesoureiro: tesoureiro
# - Data atual considerada no teste: 09/11/2026 (fictícia)
# - Cooperado: Carlos Mendes; parcela 1, R$ 300,00, vencimento 10/11/2026 (ou vencimento passado para cenários de atraso/rejeição)
# - Comprovante enviado em 08/11/2026
# - Parcela A: vencimento futuro, "Aberta"; Parcela B: vencimento passado, "Atrasada"
# - Motivo de rejeição válido: "Comprovante ilegível";


# Resultado esperado (Confirmação):

# - Parcela 1: "Paga"; data de pagamento 08/11/2026.
# - Comprovante: "Confirmado".
# - Cobrança: status recalculado pelas regras existentes.
# - Análise registrada: tesoureiro + data e hora.

# Resultado esperado (Rejeição):

# - Comprovante "Rejeitado" com motivo (registro mantido).
# - Parcela A volta a "Aberta"; parcela B volta a "Atrasada".
# - Cobrança recalculada; análise registrada (tesoureiro, data e hora).
# - Cooperado notificado com o motivo.