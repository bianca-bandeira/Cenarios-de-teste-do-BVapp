'''
UC009 - Consultar histórico de cobranças por cooperado

Objetivo: Permitir que o tesoureiro consulte as cobranças de um cooperado e
que o cooperado consulte seu próprio histórico, sem registros excluídos.

Requisitos:
- RF23934
- US - Visualização de histórico de cobranças de cooperados
- US - Visualização de histórico pessoal de cobranças do cooperado

Atores:
- Tesoureiro
- Cooperado

Autor: Bianca Rodrigues Bandeira
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# Pré-condição: o tesoureiro está autenticado; existem os cooperados A (com
# 3 cobranças, sendo 1 excluída) e B (com 1 cobrança).

# O ator acessa a área de contas por cooperados.

# O sistema exibe os cooperados cadastrados.

# O ator seleciona o cooperado A.

# O sistema verifica que o cooperado existe. [RN1]

# O sistema apresenta as cobranças vinculadas ao cooperado A. [RN2]

# O ator verifica que são exibidas apenas as 2 cobranças não excluídas
# do cooperado A e que a cobrança excluída e as do cooperado B não aparecem.


# 🟠 [A1] - COOPERADO CONSULTA O PRÓPRIO HISTÓRICO
# ---------------------------------------------------------------

# O ator "cooperado B" autentica-se, acessa seu perfil pessoal e seleciona a opção de histórico de cobranças.

# O sistema apresenta somente as cobranças vinculadas ao identificador do cooperado B, sem registros excluídos. [RN2] [RN3]

# O ator verifica que nenhuma cobrança do cooperado A é exibida.


# 🟠 [A2] - COOPERADO NÃO LOCALIZADO
# ---------------------------------------------------------------

# A consulta é feita com o identificador de um cooperado inexistente.

# O sistema não lista cobranças e retorna uma mensagem informando que o cooperado não foi localizado. [RN1]


# 🟠 [A3] - COOPERADO SEM COBRANÇAS
# ---------------------------------------------------------------

# O ator seleciona um cooperado sem cobranças cadastradas.

# O sistema exibe a listagem vazia.


# 🟣 [RN1] O cooperado deve existir; caso contrário, mensagem de "cooperado não localizado".
# 🟣 [RN2] A listagem desconsidera registros marcados como excluídos.
# 🟣 [RN3] O cooperado vê somente as cobranças do seu próprio identificador.


# [DADOS] DADOS E RESULTADOS ESPERADOS
# ---------------------------------------------------------------

# Dados de teste:
# - Cooperado A: cobranças "Mensalidade nov", "Taxa manutenção" e "Antiga"
#   (excluída)
# - Cooperado B: cobrança "Multa"
#
# Resultado esperado:
# - Tesoureiro, cooperado A: 2 cobranças ("Mensalidade nov", "Taxa manutenção").
# - Cooperado B logado: 1 cobrança ("Multa").
# - Cooperado inexistente: mensagem de cooperado não localizado.
