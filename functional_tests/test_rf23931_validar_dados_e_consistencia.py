'''
UC002 - Validar dados e regras de consistência no cadastro de cobrança

Objetivo: Garantir que o sistema bloqueie o cadastro quando houver campos
obrigatórios vazios, valores fora do permitido ou inconsistência entre
recorrência, parcelas e intervalo.

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

# Pré-condição: o tesoureiro está autenticado.

# O ator acessa a área de cadastro de cobranças.

# O ator preenche todos os campos com dados válidos, exceto UM campo
# obrigatório, que deixa em branco. Repete o procedimento para cada campo:
# nome, identificador do cooperado, valor total, status, quantidade de
# parcelas, intervalo, juros e tipo de juros. [RN1]

# A cada tentativa, o ator seleciona a opção para salvar.

# O sistema não registra a cobrança e informa que o campo obrigatório em branco precisa ser preenchido.

# O ator verifica que nenhuma cobrança foi registrada.


# 🟠 [A1] - STATUS FORA DAS OPÇÕES PERMITIDAS
# ---------------------------------------------------------------

# O ator tenta cadastrar com um status diferente das opções (ex.: "Pendente").

# O sistema impede o cadastro. [RN2]


# 🟠 [A2] - STATUS PERMITIDOS
# ---------------------------------------------------------------

# O ator cadastra uma cobrança para cada status: Aberta, Parcial, Paga e Cancelada.

# O sistema registra todas. [RN2]


# 🟠 [A3] - TIPO DE JUROS FORA DAS OPÇÕES
# ---------------------------------------------------------------

# O ator tenta cadastrar com tipo de juros diferente de "simples" e "composto" (ex.: "fixo").

# O sistema impede o cadastro. [RN3]


# 🟠 [A4] - QUANTIDADE DE PARCELAS NEGATIVA
# ---------------------------------------------------------------

# O ator informa quantidade de parcelas igual a -1.

# O sistema impede o cadastro. [RN4]


# 🟠 [A5] - JUROS NEGATIVO OU ACIMA DE 100%
# ---------------------------------------------------------------

# O ator informa juros de -1% e depois de 101%.

# O sistema impede o cadastro nas duas tentativas. [RN5]


# 🟠 [A6] - JUROS NOS LIMITES (0% E 100%)
# ---------------------------------------------------------------

# O ator informa juros de 0% e depois de 100%, com os demais dados válidos.

# O sistema registra a cobrança nas duas tentativas. [RN5]


# 🟠 [A7] - RECORRENTE COM MAIS DE UMA PARCELA
# ---------------------------------------------------------------

# O ator marca a cobrança como recorrente e informa 2 parcelas.

# O sistema impede o cadastro. [RN6]


# 🟠 [A8] - RECORRENTE COM INTERVALO ZERO
# ---------------------------------------------------------------

# O ator marca a cobrança como recorrente, 1 parcela e intervalo 0.

# O sistema impede o cadastro e exige intervalo diferente de zero. [RN6]


# 🟠 [A9] - COBRANÇA COM MAIS DE UMA PARCELA (NÃO RECORRENTE)
# ---------------------------------------------------------------

# O ator informa 3 parcelas, não recorrente, intervalo 30.

# O sistema não registra cobrança parcelada, pois o parcelamento pertence a
# contas a pagar. [RN7]


# 🟣 [RN1] Os 8 campos obrigatórios devem ser preenchidos.
# 🟣 [RN2] Status: somente Aberta, Parcial, Paga, Atrasada e Cancelada.
# 🟣 [RN3] Tipo de juros: somente simples ou composto.
# 🟣 [RN4] Quantidade de parcelas não pode ser inferior a zero.
# 🟣 [RN5] Juros entre 0% e 100%, inclusive os limites.
# 🟣 [RN6] Recorrente: no máximo 1 parcela e intervalo maior que zero.
# 🟣 [RN7] Cobrança não é parcelável: mais de 1 parcela não é aceita (o parcelamento pertence a contas a pagar).
# 🟣 [RN8] Recorrência não informada = não recorrente.


# [DADOS] DADOS E RESULTADOS ESPERADOS
# ---------------------------------------------------------------

# Valores de borda: juros -1, 0, 100, 101; parcelas -1.
#
# | Recorrente | Parcelas | Intervalo | Resultado esperado          |
# |------------|----------|-----------|-----------------------------|
# | Sim        | 1        | 30        | Cadastrada                  |
# | Sim        | 2        | 30        | Impedida                    |
# | Sim        | 1        | 0         | Impedida                    |
# | Não        | 3        | 30        | Impedida                    |
# | Não        | 1        | 30        | Cadastrada (única)          |
#
# Entradas inválidas: cobrança NÃO registrada, com aviso ao usuário.
