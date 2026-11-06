'''
UC004 - Anexar comprovante de pagamento

Objetivo: Permitir que o cooperado anexe um comprovante a um pagamento de uma
conta/cobrança, com armazenamento do arquivo, registro das informações e
registro no histórico da conta.

Requisitos:
- RF24035
- US - Anexar comprovante de pagamento
- US - Anexar comprovante de pagamento de cobrança

Ator:
- Cooperado

Autor: Bianca Rodrigues Bandeira
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# Pré-condição: o cooperado está autenticado e autorizado a enviar comprovantes; existe um pagamento associado à cobrança, não excluído.

# O ator acessa a cobrança e seleciona o pagamento correspondente.

# O sistema exibe a opção de anexar comprovante.

# O ator informa o título do comprovante e a descrição (opcional) e seleciona o arquivo "comprovante março #1.pdf". [A1] [A2] [A3]

# O ator confirma o envio.

# O sistema verifica que o pagamento existe e não está excluído. [RN1]

# O sistema valida que o arquivo e o nome foram informados [RN2] e que a
# extensão é permitida (pdf, jpeg, jpg ou png). [RN3]

# O sistema armazena o arquivo e registra seu caminho. [RN6]

# O sistema registra o comprovante com: título, descrição (se informada),
# formato, caminho, identificador do pagamento e identificador do usuário que
# enviou. [RN5]

# O sistema atribui o status "pendente". [RN7]

# O sistema registra no histórico da conta uma ocorrência com o usuário
# responsável e a descrição do envio do comprovante. [RN8]

# O sistema conclui a operação e disponibiliza o comprovante vinculado ao pagamento. [RN9]

# O ator verifica que o comprovante está vinculado ao pagamento selecionado.


# 🟠 [A1] - ENVIO SEM DESCRIÇÃO
# ---------------------------------------------------------------

# O ator não informa a descrição.

# O sistema registra o comprovante normalmente, sem descrição. [RN5]


# 🟠 [A2] - TODOS OS FORMATOS PERMITIDOS
# ---------------------------------------------------------------

# O ator envia, em tentativas separadas, arquivos .pdf, .jpeg, .jpg e .png.

# O sistema aceita todos e registra o formato correspondente. [RN3]


# 🟠 [A3] - HISTÓRICO DA CONTA
# ---------------------------------------------------------------

# Após o envio, o ator (ou o tesoureiro) consulta o histórico da conta.

# O sistema exibe a ocorrência do envio, com o usuário responsável e a
# descrição do envio do comprovante. [RN8]


# 🟣 [RN1] O pagamento deve existir e não estar excluído.
# 🟣 [RN2] Arquivo válido e nome do arquivo são obrigatórios.
# 🟣 [RN3] Extensões permitidas: pdf, jpeg, jpg e png.
# 🟣 [RN5] Registrar: título, descrição (quando informada), formato, caminho,identificador do pagamento, identificador do usuário e status.
# 🟣 [RN6] Após validar, armazenar o arquivo e registrar o caminho.
# 🟣 [RN7] Status = "pendente", após anexar o comprovante.
# 🟣 [RN8] Registrar ocorrência no histórico da conta (usuário e descrição).
# 🟣 [RN9] Concluir e disponibilizar o comprovante vinculado ao pagamento.


# 📦 [DADOS] DADOS E RESULTADOS ESPERADOS
# ---------------------------------------------------------------

# Dados de teste:
# - Cooperado A; pagamento 1 (não excluído) da cobrança "Mensalidade 11/2026"
# - Título: "Comprovante de novembro"; descrição: "Pagamento via Pix"
# - Arquivo: "comprovante março #1.pdf"
#
# Resultado esperado:
# - Caminho registrado.
# - Comprovante: formato "pdf"; pagamento 1; usuário = cooperado A;
#   status "pendente".
# - Histórico da conta com a ocorrência do envio.
