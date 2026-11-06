'''
UC005 - Impedir envio de comprovante inválido

Objetivo: Garantir que o sistema recuse o envio quando o pagamento não for
válido, o arquivo ou seu nome não forem informados, ou a extensão não for
permitida.

Requisitos:
- Feature 03
- CA01, CA02, CA03
- US - Anexar comprovante de pagamento
- US - Anexar comprovante de pagamento de cobrança

Ator:
- Cooperado

Autor: Bianca Rodrigues Bandeira
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# Pré-condição: o cooperado está autenticado e existe um pagamento 1,
# não excluído.

# O ator acessa a cobrança e seleciona o pagamento 1.

# O ator tenta confirmar o envio SEM selecionar nenhum arquivo. [A1]

# O sistema não registra o comprovante e informa que o arquivo é
# obrigatório. [RN2]

# O ator verifica que nenhum comprovante foi vinculado ao pagamento, que
# nenhum arquivo foi armazenado e que o histórico da conta não ganhou
# ocorrência. [RN4]


# 🟠 [A1] - ARQUIVO SEM NOME INFORMADO
# ---------------------------------------------------------------

# O ator envia o arquivo, mas o nome do arquivo/título não é informado.

# O sistema não registra o comprovante. [RN2] [DÚVIDA D10]


# 🟠 [A2] - EXTENSÃO NÃO PERMITIDA
# ---------------------------------------------------------------

# O ator tenta enviar arquivos .txt, .docx, .exe e .gif, um por vez.

# O sistema rejeita todos, informando que o formato não é permitido. [RN3]


# 🟠 [A3] - ARQUIVO SEM EXTENSÃO
# ---------------------------------------------------------------

# O ator tenta enviar um arquivo sem extensão.

# O sistema rejeita o envio. [RN3] [DÚVIDA D11]


# 🟠 [A4] - PAGAMENTO INEXISTENTE
# ---------------------------------------------------------------

# Um envio é feito para o identificador de um pagamento que não existe.

# O sistema não registra o comprovante. [RN1]


# 🟠 [A5] - PAGAMENTO EXCLUÍDO
# ---------------------------------------------------------------

# Um envio é feito para um pagamento marcado como excluído.

# O sistema não registra o comprovante. [RN1]


# 🟠 [A6] - CORRIGIR E REENVIAR
# ---------------------------------------------------------------

# Após uma falha, o ator envia um arquivo .pdf válido com nome informado.

# O sistema registra o comprovante normalmente (ver UC004).


# 🟣 [RN1] O pagamento deve existir e não estar excluído.
# 🟣 [RN2] Arquivo válido e nome do arquivo são obrigatórios.
# 🟣 [RN3] Somente pdf, jpeg, jpg e png são aceitos.
# 🟣 [RN4] Envio recusado não gera comprovante, arquivo armazenado nem ocorrência no histórico.


# 📦 [DADOS] DADOS E RESULTADOS ESPERADOS
# ---------------------------------------------------------------

# Dados de teste: pagamento 1 (ativo); pagamento 2 (excluído); arquivos:
# "doc.txt", "planilha.docx", "script.exe", "imagem.gif", "semextensao".
#
# Resultado esperado:
# - Toda entrada inválida: comprovante NÃO registrado, arquivo NÃO armazenado,
#   histórico SEM nova ocorrência, aviso ao usuário.
