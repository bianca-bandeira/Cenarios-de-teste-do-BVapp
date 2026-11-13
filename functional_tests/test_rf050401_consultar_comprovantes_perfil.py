'''
UC003 - Consultar comprovantes por perfil e proteger o acesso ao arquivo

Objetivo: Garantir que cada perfil visualize somente os comprovantes a que tem
direito e que o acesso ao arquivo exija autenticação e autorização.

Requisitos:
- RF050401
- RF050402 (acesso a comprovantes de outros usuários)

Atores:
- Cooperado
- Tesoureiro
- Técnico

Autor: Bianca Rodrigues Bandeira
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# Pré-condição: "Carlos Mendes" possui 4 comprovantes:
# - Parcela 1: "Em análise"
# - Parcela 2: "Aprovado"
# - Parcela 3: "Rejeitado", motivo "Comprovante ilegível"
# - Parcela 4: removido logicamente
# "Ana Maria" possui 1 comprovante "Em análise".

# O ator "cooperado Carlos Mendes" autentica-se e acessa a listagem dos seus
# comprovantes.

# O sistema exibe somente os 3 comprovantes não removidos de Carlos, cada um
# com o status. [RN1] [RN4]

# O ator verifica que o comprovante "Rejeitado" exibe o motivo "Comprovante
# ilegível" e que os demais não exibem motivo.

# O ator verifica que o comprovante de "Ana Maria" e o comprovante removido
# não aparecem.


# ---------------------------------------------------------------
# 🟠 [A1] - TESOUREIRO VISUALIZA TODOS

# O ator tesoureiro autentica-se e acessa a listagem de comprovantes.

# O sistema exibe os comprovantes de todos os cooperados, identificando a
# parcela, o usuário que enviou cada um e a data de envio. [RN2]

# O ator verifica que os comprovantes de Carlos Mendes e de Ana Maria estão
# na listagem, e que o removido não está. [RN4]


# ---------------------------------------------------------------
# 🟠 [A2] - TÉCNICO TENTA VISUALIZAR COMPROVANTE

# O ator "Técnico" tenta abrir diretamente o endereço do arquivo de
# um comprovante.

# O sistema nega o acesso e não exibe o arquivo. [RN3]


# ---------------------------------------------------------------
# 🟠 [A3] - ACESSO AO ARQUIVO SEM AUTENTICAÇÃO

# Um usuário não autenticado tenta abrir diretamente o endereço do arquivo de
# um comprovante.

# O sistema nega o acesso e não exibe o arquivo. [RN3]


# ---------------------------------------------------------------
# 🟠 [A4] - COOPERADO TENTA ACESSAR COMPROVANTE DE OUTRO COOPERADO

# "Carlos Mendes" tenta abrir, por endereço direto, o comprovante de
# "Ana Maria".

# O sistema nega o acesso. [RN1]


# 🟣 [RN1] O cooperado visualiza apenas os seus comprovantes, com o status de cada um e o motivo da rejeição, quando houver.
# 🟣 [RN2] Tesoureiro visualizam todos os comprovantes, identificando a parcela e o usuário que enviou.
# 🟣 [RN3] O acesso ao arquivo exige autenticação e autorização.
# 🟣 [RN4] Comprovantes removidos (remoção lógica) não aparecem nas listagens.


# [DADOS] DADOS E RESULTADOS ESPERADOS
# ---------------------------------------------------------------

# Resultado esperado:
# - Carlos Mendes: 3 comprovantes (Em análise, Confirmado, Rejeitado com
#   motivo).
# - Tesoureiro: 4 comprovantes (3 de Carlos + 1 de Ana), cada um com parcela e usuário.
# - Sem autenticação/autorização ou de outro cooperado: acesso negado.