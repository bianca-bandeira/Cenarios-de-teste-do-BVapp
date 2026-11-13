'''
UC001 - Manter comprovante de pagamento (anexar, consultar, substituir e remover)

Objetivo: Permitir que o cooperado anexe, consulte, substitua e remova os
comprovantes de pagamento das suas mensalidades, como um fluxo completo.

Requisitos:
- RF050401

Ator:
- Cooperado

Autor: Bianca Rodrigues Bandeira
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# Pré-condição: o cooperado "Carlos Mendes" está autenticado e possui uma conta
# da mensalidade "Mensalidade novembro/2026" com status "Aberta",
# não paga e não removida. O pagamento é feito fora da plataforma.

# O ator acessa a sua conta referente a mensalidade, seleciona a parcela e
# escolhe a opção de anexar comprovante.

# O sistema exibe o formulário com os campos:
# - Parcela (já identificada)
# - Arquivo (obrigatório)
# - Nome do arquivo (obrigatório)
# - Observações (opcional)
# - Opção "Salvar"

# O ator seleciona o arquivo "comprovante_novembro.pdf", informa o nome
# "Comprovante de novembro" e a observação "Pagamento via Pix" e seleciona
# "Salvar". [A1] [A2] [A3]

# O sistema valida os dados e registra o comprovante com o status
# "Em análise". [RN1] [RN3]

# O sistema mantém a parcela com o status "Aberta" e exibe uma mensagem de
# sucesso. [RN3]

# ---------------------------------------------------------------
# 🟠 [A1] - CONSULTAR 
# O ator acessa a conta e visualiza a listagem do[s] seu[s] comprovante[s].

# O sistema exibe o comprovante com o nome, a parcela e o status "Em análise".

# O ator abre o comprovante.

# O sistema exibe o arquivo "comprovante_novembro.pdf".

# ---------------------------------------------------------------
# 🟠 [A2] - EDITAR
# O ator seleciona o comprovante (status "Em análise") e escolhe a opção de
# editar. [RN5]

# O sistema exibe os campos preenchidos com os dados atuais.

# O ator troca o arquivo por "comprovante_novembro_v2.png", altera o nome para
# "Comprovante de novembro (corrigido)" e a observação para
# "Segunda via do Pix" e seleciona "Salvar".

# O sistema valida os dados e salva a alteração, mantendo o status "Em análise".

# O ator consulta novamente o comprovante e verifica que o arquivo, o nome e
# as observações são os novos.

# ---------------------------------------------------------------
# 🟠 [A3] - REMOVER 
# O ator seleciona o comprovante (status "Em análise") e escolhe a opção de
# remover.

# O sistema pede a confirmação da remoção.

# O ator confirma.

# O sistema remove logicamente o comprovante. [RN6]

# O ator acessa a listagem do[s] seu[s] comprovante[s] e verifica que o comprovante
# removido não aparece.

# O ator verifica que a parcela continua com o status "Aberta".


# ---------------------------------------------------------------
# 🟠 [A4] - ANEXAR SEM OBSERVAÇÕES

# O ator preenche somente arquivo e nome, deixando as observações vazias.

# O sistema registra o comprovante normalmente, com o status "Em análise".
# [RN1]


# ---------------------------------------------------------------
# 🟠 [A5] - ANEXAR EM PARCELA ATRASADA

# O ator seleciona uma parcela de mensalidade com o status "Atrasada".

# O sistema registra o comprovante com o status "Em análise" e a parcela
# continua "Atrasada" até a validação do tesoureiro. [RN2] [RN3]


# ---------------------------------------------------------------
# 🟠 [A6] - NOVO ENVIO APÓS REMOÇÃO

# Depois de remover o comprovante (FP), o ator pode anexar um novo comprovante à
# mesma parcela.

# O sistema registra o novo comprovante com o status "Em análise". [RN4]


# ---------------------------------------------------------------
# 🟠 [A7] - ALTERAR OU REMOVER COMPROVANTE APROVADO

# O ator seleciona um comprovante com o status "Aprovado" e tenta editá-lo
# ou removê-lo.

# O sistema não permite a alteração nem a remoção e mantém o comprovante
# inalterado. [RN5] [RN6]


# ---------------------------------------------------------------
# 🟠 [A8] - ALTERAR OU REMOVER COMPROVANTE REJEITADO

# O ator seleciona um comprovante com o status "Rejeitado" e tenta editá-lo
# ou removê-lo.

# O sistema não permite a alteração nem a remoção. [RN5] [RN6]

# O ator anexa um novo comprovante à mesma parcela.

# O sistema registra o novo comprovante com o status "Em análise". [RN7]


# ---------------------------------------------------------------
# 🟠 [A9] - REMOVER COMPROVANTE QUE SUSTENTA PARCELA PAGA

# O ator tenta remover o comprovante de uma parcela com status "Paga".

# O sistema não permite a remoção e mantém o comprovante inalterado. [RN8] 


# ---------------------------------------------------------------
# 🟣 [RN1] CAMPOS DO COMPROVANTE

# Parcela, arquivo e nome do arquivo são obrigatórios; observações é opcional.

# ---------------------------------------------------------------
# 🟣 [RN2] ESCOPO DO COOPERADO

# O cooperado só anexa comprovantes às suas próprias parcelas de mensalidade,
# e somente em parcelas não pagas e não removidas.

# ---------------------------------------------------------------
# 🟣 [RN3] STATUS INICIAL

# O comprovante enviado pelo cooperado nasce "Em análise" e a parcela mantém
# seu status (Aberta ou Atrasada) até a validação do tesoureiro.

# ---------------------------------------------------------------
# 🟣 [RN4] LIMITE POR PARCELA

# Só pode haver um comprovante "Em análise" por parcela por vez.

# ---------------------------------------------------------------
# 🟣 [RN5] EDIÇÃO

# O cooperado pode substituir arquivo, nome e observações apenas enquanto o
# comprovante estiver "Em análise".

# ---------------------------------------------------------------
# 🟣 [RN6] REMOÇÃO

# A remoção é lógica e o comprovante deixa de aparecer nas listagens. O
# cooperado só remove comprovantes "Em análise".

# ---------------------------------------------------------------
# 🟣 [RN7] COMPROVANTE REJEITADO

# Se o comprovante for rejeitado, o cooperado pode enviar um novo.

# ---------------------------------------------------------------
# 🟣 [RN8] PARCELA PAGA

# O comprovante que sustenta uma parcela já paga não pode ser removido.


# [DADOS] DADOS E RESULTADOS ESPERADOS
# ---------------------------------------------------------------

# Dados de teste (fictícios):
# - Cooperado: Carlos Mendes; parcela 1 da "Mensalidade novembro/2026",
#   R$ 300,00, vencimento 10/11/2026, status "Aberta"
# - Arquivos: "comprovante_novembro.pdf" e "comprovante_novembro_v2.png"
# - Data atual considerada no teste: 09/11/2026 (fictícia)
#
# Resultado esperado:
# - Após anexar: comprovante "Em análise"; parcela continua "Aberta".
# - Após substituir: novo arquivo, nome e observações; status "Em análise".
# - Após remover: comprovante não aparece na listagem (remoção lógica);
#   parcela continua "Aberta".
# - Comprovante "Aprovado" ou "Rejeitado": nunca é alterado nem removido
#   pelo cooperado.