'''
UC002 - Manter comprovante de despesa da cooperativa (anexar, consultar, substituir e remover)

Objetivo: Permitir que o tesoureiro anexe, consulte, substitua e remova os
comprovantes das despesas da cooperativa (contas a pagar), como um fluxo
completo.

Requisitos:
- RF050401

Ator:
- Tesoureiro

Autor: Bianca Rodrigues Bandeira
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# Pré-condição: o tesoureiro está autenticado e existe a conta a pagar
# "Conta de energia da sede", parcela 1, não removida nem cancelada. O
# pagamento da despesa é feito fora da plataforma.

# O ator acessa a parcela 1 da conta a pagar e escolhe a opção de anexar
# comprovante.

# O sistema exibe o formulário com os campos:
# - Parcela (já identificada)
# - Arquivo (obrigatório)
# - Nome do arquivo (obrigatório)
# - Observações (opcional)
# - Opção "Salvar"

# O ator seleciona o arquivo "fatura_energia.pdf", informa o nome "Fatura de
# energia - novembro" e a observação "Pago via boleto" e seleciona "Salvar".
# [A2] [A3]

# O sistema valida os dados e registra o comprovante com o status
# "Aprovado", sem passar por análise. [RN2]

# O sistema registra o comprovante como sustentação do pagamento. [RN3]

# O sistema atualiza a parcela com o status "Paga" e exibe uma mensagem de
# sucesso.

# ---------------------------------------------------------------
# 🟠 [A1] - CONSULTAR 
# O ator acessa a conta e visualiza a listagem de comprovantes.

# O sistema exibe o comprovante, identificando a parcela e a data de envio, com o status "Aprovado".

# O ator abre o comprovante e o sistema exibe o arquivo.

# ---------------------------------------------------------------
# 🟠 [A2] - SUBSTITUIR 
# O ator seleciona o comprovante e escolhe a opção de substituir.

# O ator troca o arquivo por "fatura_energia_v2.pdf" e altera o nome e as
# observações e seleciona "Salvar".

# O sistema valida e salva a alteração.

# O ator consulta o comprovante e verifica os novos dados.

# ---------------------------------------------------------------
# 🟠 [A3] - REMOVER 
# O ator solicita a remoção do comprovante que sustenta o pagamento da
# despesa.

# O sistema pede a confirmação da remoção.

# O ator confirma.

# O sistema remove logicamente o comprovante. [RN4]

# O ator acessa a listagem e verifica que o comprovante não aparece.


# ---------------------------------------------------------------
# 🟠 [A4] - PARCELA REMOVIDA OU CANCELADA

# O ator tenta anexar um comprovante a uma parcela de conta a pagar removida
# e depois a uma cancelada.

# O sistema não permite o envio nos dois casos. [RN1]


# ---------------------------------------------------------------
# 🟠 [A5] - ARQUIVO INVÁLIDO

# O ator tenta enviar sem arquivo, sem nome, com formato .docx e com um
# arquivo de 6 MB.

# O sistema rejeita cada tentativa com mensagem de erro e não registra o
# comprovante. [RN5]


# ---------------------------------------------------------------
# 🟠 [A6] - ANEXAR SEM OBSERVAÇÕES

# O ator deixa as observações vazias.

# O sistema registra o comprovante normalmente. [RN5]


# ---------------------------------------------------------------
# 🟠 [A7] - COMPROVANTE DO TESOUREIRO NÃO ENTRA NA FILA DE VALIDAÇÃO

# O ator acessa a fila de comprovantes pendentes de validação.

# O sistema não exibe o comprovante da despesa, pois ele nasce "Aprovado" e
# não há segunda análise. [RN2]


# ---------------------------------------------------------------
# 🟣 [RN1] ESCOPO DO TESOUREIRO

# O tesoureiro só anexa comprovantes a parcelas não
# removidas nem canceladas.

# ---------------------------------------------------------------
# 🟣 [RN2] STATUS INICIAL

# O comprovante anexado pelo tesoureiro nasce "Aprovado".

# ---------------------------------------------------------------
# 🟣 [RN3] SUSTENTAÇÃO DO PAGAMENTO

# O comprovante sustenta o registro de pagamento da despesa.

# ---------------------------------------------------------------
# 🟣 [RN4] REMOÇÃO LÓGICA

# A remoção é lógica e o comprovante deixa de aparecer nas listagens.

# ---------------------------------------------------------------
# 🟣 [RN5] VALIDAÇÃO DO ARQUIVO

# Arquivo e nome são obrigatórios; formatos PDF, JPEG, JPG e PNG; tamanho
# máximo parametrizado (padrão 5 MB); observações opcionais.


# [DADOS] DADOS E RESULTADOS ESPERADOS
# ---------------------------------------------------------------

# Dados de teste:
# - Conta a pagar "Conta de energia da sede", parcela 1, R$ 800,00
# - Arquivos: "fatura_energia.pdf" e "fatura_energia_v2.pdf"
#
# Resultado esperado:
# - Após anexar: comprovante "Aprovado", com parcela e data de envio "10/11/2026".
# - Após substituir: novos dados exibidos.
# - Após o estorno: comprovante removido logicamente e fora das listagens.