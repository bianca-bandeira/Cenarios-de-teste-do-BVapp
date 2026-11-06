'''
UC003 - Manter cobrança (cadastrar, consultar e atualizar)

Objetivo: Permitir que o tesoureiro cadastre uma cobrança, consulte-a e
atualize seus dados, com validações e verificação de duplicidade.

Requisitos:
- Feature 02
- CA10, CA11 (e regras de validação dos CA01 a CA08)
- US - Cadastro de cobrança
- US - Atualizar cobrança

Ator:
- Tesoureiro

Autor: Bianca Rodrigues Bandeira

Observação (parcelas): cobrança NÃO é parcelável. O parcelamento pertence a contas a
pagar (no banco, cobranças e contas a pagar compartilham a tabela "conta").
Nos cenários, toda cobrança tem 1 parcela.

Observação (CRUD): os requisitos descrevem criar, consultar (para selecionar
a cobrança) e atualizar. A EXCLUSÃO de cobrança não tem critério na Feature
02.
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# Pré-condição: o tesoureiro está autenticado.

# [CRIAR] O ator acessa a área de cadastro de cobranças, preenche os campos
# obrigatórios com dados válidos e seleciona a opção para salvar. [A3]

# O sistema registra a cobrança e exibe a confirmação.

# [CONSULTAR] O ator acessa a área de cobranças e localiza a cobrança cadastrada.

# O sistema exibe os dados da cobrança.

# O ator verifica que os dados correspondem aos informados no cadastro.

# [ATUALIZAR] O ator seleciona a cobrança e altera os campos autorizados. [A1] [A2]

# O ator seleciona a opção para salvar.

# O sistema valida os dados alterados [RN2] e salva a atualização.

# O sistema exibe a confirmação da operação.

# [CONSULTAR] O ator consulta a cobrança novamente.

# O ator verifica que os dados refletem as alterações realizadas.


# 🟠 [A1] - ATUALIZAÇÃO COM DADO INVÁLIDO
# ---------------------------------------------------------------

# O ator altera o campo de juros para 150% e tenta salvar.

# O sistema impede a atualização e informa o erro. [RN2]

# O ator consulta a cobrança e verifica que os dados originais foram mantidos.


# 🟠 [A2] - ATUALIZAÇÃO QUE VIOLA REGRA DE RECORRÊNCIA/PARCELAS
# ---------------------------------------------------------------

# O ator altera a cobrança para recorrente e a quantidade de parcelas para 2.
# (Cobrança não é parcelável.)

# O sistema impede a atualização. [RN2]


# 🟠 [A3] - CADASTRO DUPLICADO
# ---------------------------------------------------------------

# Após o [CRIAR] do FP, o ator tenta cadastrar nova cobrança com os mesmos
# dados identificadores de duplicidade para o mesmo cooperado.
# [DÚVIDA D01]

# O sistema detecta a cobrança ativa existente e impede o cadastro. [RN1]

# O ator verifica que existe apenas uma cobrança com esses dados.


# 🟠 [A4] - MESMOS DADOS PARA OUTRO COOPERADO
# ---------------------------------------------------------------

# O ator cadastra os mesmos dados para o cooperado "Ana Maria".

# O sistema registra a cobrança normalmente. [RN1]


# 🟠 [A5] - DUPLICIDADE COM COBRANÇA NÃO ATIVA
# ---------------------------------------------------------------

# A cobrança existente está com status "Cancelada" e o ator cadastra outra
# com os mesmos dados.

# O sistema registra a cobrança normalmente.


# 🟠 [A6] - ATUALIZAR O STATUS PARA "CANCELADA"
# ---------------------------------------------------------------

# O ator altera o status para "Cancelada" (valor permitido) e salva.

# O sistema salva a atualização e exibe a confirmação.


# 🟠 [A7] - EXCLUIR COBRANÇA
# ---------------------------------------------------------------

# Operação não descrita nos requisitos da Feature 02. Aguardando resposta.
# [DÚVIDA D05]


# 🟣 [RN1] Não pode haver cobrança ativa do mesmo cooperado com os mesmos dados identificadores de duplicidade.
# 🟣 [RN2] A atualização aplica as validações correspondentes (campos
#          obrigatórios, status, tipo de juros, parcelas, juros, recorrência e intervalo).


# 📦 [DADOS] DADOS E RESULTADOS ESPERADOS
# ---------------------------------------------------------------

# Cadastro: nome "Taxa de manutenção"; Ana Maria; valor 200,00; status Aberta;
# 1 parcela; intervalo 30; juros 1%; tipo simples.
# Atualização válida: nome "Taxa de manutenção 2026"; valor 250,00.
#
# Resultado esperado:
# - Após criar: cobrança consultável com os dados originais.
# - Após atualizar com dados válidos: dados novos exibidos.
# - Após atualizar com dados inválidos: dados anteriores mantidos.
# - Duplicata para o mesmo cooperado: NÃO registrada.
