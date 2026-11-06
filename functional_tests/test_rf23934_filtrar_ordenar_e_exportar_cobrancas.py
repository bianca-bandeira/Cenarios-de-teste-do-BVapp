'''
UC010 - Filtrar, ordenar e exportar cobranças do cooperado

Objetivo: Permitir que o tesoureiro filtre as cobranças de um cooperado por
critérios opcionais, ordene os resultados e exporte em PDF e CSV.

Requisitos:
- Feature 05
- CA03, CA04, CA05
- US - Filtragem e Exportação das cobranças do cooperado

Ator:
- Tesoureiro 

Autor: Bianca Rodrigues Bandeira
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# Pré-condição: o ator está autenticado e visualizando as cobranças do
# cooperado carlos Mendes, que possui as cobranças C1, C2 e C3 e uma cobrança
# excluída (ver DADOS).

# O ator verifica que existem os filtros opcionais: nome, descrição, tipo,
# status, intervalo (mín/máx), recorrência, quantidade de parcelas (mín/máx),
# juros (mín/máx), tipo de juros, valor total (mín/máx) e período de
# lançamento. [RN1]

# O ator não informa nenhum filtro.

# O sistema apresenta todas as cobranças não excluídas (C1, C2 e C3).

# O ator informa o filtro status "Aberta".

# O sistema apresenta somente a cobrança C1. [RN1]

# O ator limpa o filtro e escolhe ordenar por "valor total" em ordem decrescente.

# O sistema apresenta C3, C2 e C1, nessa ordem. [RN2]

# O ator seleciona exportar em PDF e depois em CSV.

# O sistema gera os dois arquivos com as cobranças apresentadas.


# 🟠 [A1] - FILTROS COMBINADOS
# ---------------------------------------------------------------

# O ator informa status "Atrasada" e valor total mínimo de 400.

# O sistema apresenta somente C3. [RN1]


# 🟠 [A2] - FILTROS POR FAIXA E PERÍODO
# ---------------------------------------------------------------

# O ator aplica, um por vez:
# - valor total mínimo 200 e máximo 600 => C2 e C3
# - quantidade mínima de parcelas 2 => C2 e C3
# - tipo de juros "composto" => C3
# - período de lançamento 01/10/2026 a 31/10/2026 => C2
# - recorrência "sim" => C1
# - intervalo mínimo 20 e máximo 40 => C1 e C2
# - juros mínimo 1 e máximo 3 => C2

# O sistema apresenta somente as cobranças esperadas em cada caso. [RN1]


# 🟠 [A3] - FILTROS DE TEXTO (NOME E DESCRIÇÃO)
# ---------------------------------------------------------------

# O ator filtra pelo nome "Taxa".

# O sistema apresenta C2. [RN1]


# 🟠 [A4] - ORDEM CRESCENTE
# ---------------------------------------------------------------

# O ator ordena por "valor total" em ordem crescente.

# O sistema apresenta C1, C2 e C3. [RN2]


# 🟠 [A5] - ORDENAÇÃO INVÁLIDA
# ---------------------------------------------------------------

# Uma consulta é feita com campo de ordenação inexistente (ex.: "cor") ou
# direção inválida (ex.: "aleatória").

# O sistema não processa a consulta e informa o parâmetro inválido. [RN3]


# 🟠 [A6] - NENHUM RESULTADO
# ---------------------------------------------------------------

# O ator informa status "Cancelada" para o cooperado Daniel Urtiga.

# O sistema apresenta a listagem vazia.


# 🟠 [A7] - FILTRO NÃO TRAZ COBRANÇA EXCLUÍDA
# ---------------------------------------------------------------

# O ator filtra por status "Aberta" (a cobrança excluída "Antiga" também era "Aberta").

# O sistema não apresenta a cobrança excluída. [RN4]


# 🟣 [RN1] Filtros são opcionais, individuais ou combinados; retornam só registros que atendem a todos os critérios informados.
# 🟣 [RN2] Ordenação por campos definidos, crescente ou decrescente.
# 🟣 [RN3] Somente campos e direções de ordenação permitidos são aceitos.
# 🟣 [RN4] Registros excluídos nunca são exibidos.


# 📦 [DADOS] DADOS E RESULTADOS ESPERADOS
# ---------------------------------------------------------------

# Cobranças do COOP-001 (fictícias):
# | ID | Nome            | Status   | Parc. | Interv. | Recorr. | Juros | Tipo     | Valor | Lançamento |
# |----|-----------------|----------|-------|---------|---------|-------|----------|-------|------------|
# | C1 | Mensalidade nov | Aberta   | 1     | 30      | Sim     | 0     | simples  | 100   | 01/11/2026 |
# | C2 | Taxa manutenção | Paga     | 3     | 30      | Não     | 2     | simples  | 300   | 05/10/2026 |
# | C3 | Multa           | Atrasada | 2     | 15      | Não     | 5     | composto | 500   | 20/09/2026 |
# | C4 | Antiga          | Aberta   | (excluída, nunca exibida)                                  |
#
# Resultado esperado: os resultados descritos em cada fluxo acima; exportação
# em PDF e CSV com as cobranças apresentadas (conteúdo: DÚVIDA D25).
