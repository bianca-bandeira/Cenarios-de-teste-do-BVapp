'''
UC001 - Manter cobrança

Objetivo: Permitir que o tesoureiro possa cadastrar, consultar, alterar e excluir cobranças associadas a um cooperado.

Requisitos:
- RF23931
- US - Cadastro de cobrança
- US - Atualizar cobrança
- US - Deletar conta/cobrança (RF25929)

Ator:
- Tesoureiro

Autor: Bianca Rodrigues Bandeira

Observação: cobrança NÃO é parcelável. O parcelamento pertence a contas a
pagar (no banco, cobranças e contas a pagar compartilham a tabela "conta").
Nos cenários, toda cobrança tem 1 parcela.
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# Pré-condição: O tesoureiro está autenticado e existe um cooperado cadastrado.

# O ator acessa a página de cadastro de cobranças. Ele verifica que o 
# título da página é "Cadastro de cobrança". Ele observa que existem os campos:
# - Nome da cobrança
# - Identificador do cooperado
# - Valor total
# - Status
# - Intervalo
# - Juros
# - Tipo de juros
# - Recorrência (recorrente ou única)
# - Descrição
# - Data de lançamento
# - Opções
# -- Botão "Salvar"
# -- Botão "Cancelar"

# O ator preenche os campos obrigatórios e opcionais com os dados da cobrança. [A4] [A5]

# Ao concluir o cadastro, ele seleciona a opção "Salvar". 

# O sistema valida os dados conforme as regras. [RN1] [RN2] [RN3]

# O sistema exibe a página de cadastro de cobranças novamente e exibe uma
# mensagem de sucesso de registro.

# O ator seleciona 'Consultar cobranças' no menu.

# O sistema exibe a página de listagem de cobranças.

# O ator verifica que a cobrança cadastrada para o cooperado está na lista.


# 🟠 [A1] - BUSCAR COBRANÇA
# ---------------------------------------------------------------

# O ator necessita realizar uma busca por cobranças na lista. 
# Ele acessa a página "Listar cobranças".

# O sistema exibe a página de listagem de cobranças.

# O ator seleciona o campo específico para busca e digita o nome da cobrança (ou cooperado).

# O ator seleciona 'Pesquisar'.

# O sistema exibe todas as cobranças que correspondem aos termos que foram digitados.


## 🟠 [A2] EDITAR COBRANÇA
# ---------------------------------------------------------------
# O ator executa [A1].

# O ator seleciona a cobrança na lista e clica no botão para editar.

# O sistema exibe a página de edição de cobranças com os campos 
# preenchidos com os dados atuais.

# O ator altera os campos desejados (ex: nome, valor ou status) e clica no botão 
# para salvar. [A6] [A7]

# O sistema valida os dados alterados e salva a atualização. [RN4]

# O sistema exibe uma mensagem de confirmação.

# O ator consulta a cobrança novamente e verifica que os dados refletem as alterações.


# 🟠 [A3] EXCLUIR COBRANÇA
# ---------------------------------------------------------------

# O ator decide excluir uma cobrança e executa [A1]. 

# Ele visualiza a cobrança e seleciona a opção 'Excluir'.

# O sistema verifica se a cobrança pode ser excluída (Apenas contas/cobranças com status "Aberta" ou "Atrasada" podem ser deletadas). 

# O sistema pergunta se o usuário realmente deseja excluir a cobrança.

# O ator confirma a exclusão.

# O sistema exclui a cobrança de maneira lógica (muda o status para inativo/excluído invisível para o usuário). 

# O ator seleciona 'Listar cobranças' no menu.

# O sistema exibe a lista de cobranças.

# O ator verifica que a cobrança excluída não está mais na lista.


# 🟠 [A4] - CADASTRAR SEM OS CAMPOS OPCIONAIS
# ---------------------------------------------------------------

# No passo de preenchimento do [FP], o ator preenche somente os campos obrigatórios, 
# deixando vazios "Descrição" e "Data de lançamento".

# O sistema registra a cobrança normalmente e exibe a confirmação. [RN2]


# 🟠 [A5] - TENTATIVA DE CADASTRO DUPLICADO
# ---------------------------------------------------------------

# O ator tenta cadastrar uma nova cobrança com os mesmos
# dados identificadores de duplicidade para o mesmo cooperado que já possui uma cobrança ativa.

# O sistema detecta a cobrança ativa existente e impede o cadastro, exibindo mensagem de erro. [RN3]


# 🟠 [A6] - ATUALIZAÇÃO COM DADO INVÁLIDO
# ---------------------------------------------------------------

# O ator, durante a edição [A2], altera o campo de juros para um valor inválido (ex: 150%) 
# ou altera a quantidade de parcelas para 2.

# O sistema impede a atualização, informa o erro e mantém os dados originais.


# 🟠 [A7] - ATUALIZAR O STATUS PARA "CANCELADA"
# ---------------------------------------------------------------

# O ator, durante a edição [A2], altera o status da cobrança para "Cancelada" e salva.

# O sistema salva a atualização e exibe a confirmação sem exigir exclusão.


# 🟣 [RN1] CAMPOS OBRIGATÓRIOS
# ---------------------------------------------------------------
# Nome, identificador do cooperado, valor total, status, quantidade de
# parcelas, intervalo, juros e tipo de juros são obrigatórios.

# 🟣 [RN2] CAMPOS OPCIONAIS E VALORES PADRÃO
# ---------------------------------------------------------------
# Descrição e data de lançamento podem ficar vazios.
# Sem recorrência informada, a cobrança é considerada não recorrente (única).

# 🟣 [RN3] VALIDAÇÃO DE DUPLICIDADE
# ---------------------------------------------------------------
# Não pode haver cobrança ativa do mesmo cooperado com os mesmos dados identificadores de duplicidade.
# Se a cobrança existente estiver com status "Cancelada", o sistema permite o cadastro de uma nova.

# 🟣 [RN4] REGRAS DE ATUALIZAÇÃO
# ---------------------------------------------------------------
# A atualização aplica as mesmas validações de criação (campos obrigatórios, status, tipo de juros, parcelas, juros, recorrência e intervalo). Não é permitido alterar uma cobrança para ter mais de 1 parcela.


# [DADOS] DADOS E RESULTADOS ESPERADOS
# ---------------------------------------------------------------

# Dados de teste (fictícios):
# - Nome: "Mensalidade novembro/2026"; Cooperado: "Carlos Mendes"
# - Valor total: 300,00; Status: Aberta; Parcelas: 1; Intervalo: 30
# - Juros: 2%; Tipo de juros: simples
# - Descrição: "Cobrança de teste"; Data de lançamento: 05/11/2026
#
# Resultado esperado (Cadastro/Edição):
# - Cobrança consultável com os dados informados.
#
# Resultado esperado (Exclusão):
# - Cobrança removida da listagem de visualização do tesoureiro.