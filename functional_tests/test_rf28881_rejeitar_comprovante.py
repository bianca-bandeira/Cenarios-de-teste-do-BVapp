'''
UC008 - Rejeitar comprovante com motivo (e validações da decisão)

Objetivo: Permitir que o tesoureiro rejeite um comprovante informando o motivo,
com exclusão lógica e remoção da data de pagamento; e garantir que decisões
inválidas ou sem motivo não sejam processadas.

Requisitos:
- RF28881
- US - Visualizar comprovante de cobrança

Ator:
- Tesoureiro

Autor: Bianca Rodrigues Bandeira
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# Pré-condição: o tesoureiro está autenticado e existe um comprovante enviado, ainda não analisado.

# O ator acessa a tela de cobranças por cooperado, seleciona a cobrança com
# comprovante e solicita a visualização.

# O sistema exibe o comprovante e as opções "confirmar pagamento" e "rejeitado".

# O ator seleciona "rejeitado".

# O sistema solicita o motivo da rejeição. [RN5]

# O ator informa o motivo e confirma. [A1] [A2] [A3]

# O sistema atualiza o status do comprovante para "rejeitado" e armazena o
# motivo. [RN1]

# O sistema registra o identificador do tesoureiro e a data e o horário da
# decisão, em UTC. [RN2]

# O sistema marca o comprovante como excluído logicamente, sem excluí-lo fisicamente do banco de dados. [RN3]

# O sistema atribui valor nulo à data de pagamento da parcela. [RN4]

# O ator verifica que o comprovante está "rejeitado" com o motivo, que a
# parcela está sem data de pagamento e que o status da conta foi atualizado.


# 🟠 [A1] - REJEIÇÃO SEM MOTIVO
# ---------------------------------------------------------------

# O ator seleciona "rejeitado" e tenta confirmar SEM informar o motivo.

# O sistema não processa a rejeição e informa que o motivo é obrigatório.
# [RN5]

# O ator verifica que comprovante, parcela e conta não foram alterados.


# 🟠 [A2] - MOTIVO APENAS COM ESPAÇOS EM BRANCO
# ---------------------------------------------------------------

# O ator informa somente espaços como motivo e tenta confirmar.

# O sistema trata como vazio e não processa a rejeição. [RN5]


# 🟠 [A3] - AÇÃO DIFERENTE DE "confirmar pagamento" E "rejeitado"
# ---------------------------------------------------------------

# Uma decisão é enviada com valor diferente (ex.: "pendente", "cancelado") ou vazio.

# O sistema não processa a decisão. [RN6]

# Nenhum dado de comprovante, parcela, conta ou registro de análise muda.


# 🟠 [A4] - REGISTRO FÍSICO PERMANECE NO BANCO
# ---------------------------------------------------------------

# Após a rejeição, verifica-se o banco de dados.

# O comprovante continua existindo, com indicador de exclusão lógica marcado,
# status "rejeitado" e motivo. [RN3]


# 🟠 [A5] - COMPROVANTE REJEITADO SAI DAS PENDÊNCIAS
# ---------------------------------------------------------------

# O ator volta à tela de cobranças por cooperado.

# O sistema não exibe o comprovante rejeitado como pendente de análise.


# 🟣 [RN1] Rejeição: status "rejeitado" + motivo informado.
# 🟣 [RN2] Registrar tesoureiro e data/hora da decisão em UTC.
# 🟣 [RN3] Exclusão lógica: marcar como excluído, sem exclusão física.
# 🟣 [RN4] Data de pagamento da parcela passa a nulo.
# 🟣 [RN5] Motivo de rejeição obrigatório.
# 🟣 [RN6] Somente as ações "confirmar pagamento" e "rejeitado" são aceitas.


# [DADOS] DADOS E RESULTADOS ESPERADOS
# ---------------------------------------------------------------

# Dados de teste:
# - Tesoureiro "tesoureiro1"; conta 1; parcela 1 com data de pagamento
#   05/11/2026; motivo: "Comprovante ilegível".
# - Entradas inválidas: motivo vazio; motivo "   "; ações "pendente", "".
#
# Resultado esperado:
# - Rejeição válida: comprovante "rejeitado" com motivo, excluído logicamente
#   (registro mantido); análise = tesoureiro1 + data/hora UTC; parcela 1 sem
#   data de pagamento; conta 1 com status recalculado.
# - Entradas inválidas: nada é alterado.
