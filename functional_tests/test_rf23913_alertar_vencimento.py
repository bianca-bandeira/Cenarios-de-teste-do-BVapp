'''
UC004 - Verificação de contas/cobranças próximas do vencimento

Objetivo: Permitir que o cooperado visualize notificações (alertas) sobre suas contas 
e cobranças que estão próximas da data de vencimento diretamente na página inicial, 
evitando atrasos.

Requisitos:
- RF23913
- US - Verificação de contas/cobranças próximas do vencimento

Ator:
- Cooperado

Autor: Bianca Rodrigues Bandeira

Observação: A verificação é diária. O padrão de antecedência é de 7 dias corridos.
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# Pré-condição 1: O sistema já rodou a rotina diária de verificação de contas não pagas. [RN1]
# Pré-condição 2: O cooperado está autenticado no sistema.
# Pré-condição 3: O cooperado possui a opção de receber notificações habilitada. [RN2]

# O ator acessa a página inicial da plataforma.

# O sistema identifica que existe uma cobrança/conta em aberto cujo vencimento 
# está dentro do período de antecedência configurado (ex: próximos 7 dias). [RN1]

# O sistema verifica que o vencimento cai em um dia útil. [A2]

# O sistema exibe um pop-up com fundo amarelo no canto superior direito da tela.

# O ator visualiza o pop-up contendo a mensagem padrão:
# “Sócio(a) [NOME_DO_COOPERADO], faltam [QUANTIDADE_DE_DIAS] dias para o vencimento 
# da conta [IDENTIFICAÇÃO_DA_CONTA].”

# O ator também visualiza no alerta o Valor original e a Data de vencimento. [RN3]


# 🟠 [A1] - NOTIFICAÇÕES DESABILITADAS PELO COOPERADO
# ---------------------------------------------------------------

# O ator acessa a página inicial da plataforma.

# O sistema identifica que existem contas próximas do vencimento (em até 7 dias).

# O sistema verifica que o cooperado tem a opção de "receber notificações" DESABILITADA. [RN2]

# O sistema NÃO exibe nenhum pop-up de alerta.


# 🟠 [A2] - VENCIMENTO CAI EM DIA NÃO ÚTIL (FIM DE SEMANA/FERIADO)
# ---------------------------------------------------------------

# Durante o [FP], o sistema identifica que a cobrança/conta vence em um dia não útil. [RN4]

# O sistema exibe o pop-up com fundo amarelo no canto superior direito.

# O sistema exibe a mensagem padrão com os dados (Nome, dias, conta, valor, data).

# O sistema adiciona um destaque visual/textual informando que a data cai em um dia não útil.
# Texto em negrito informando : "Atenção: O vencimento cai em um fim de semana/feriado."


# 🟠 [A3] - NÃO HÁ CONTAS PRÓXIMAS AO VENCIMENTO
# ---------------------------------------------------------------

# O ator acessa a página inicial da plataforma.

# O sistema verifica a rotina diária e constata que o cooperado não possui contas/cobranças 
# não pagas com vencimento para os próximos 7 dias.

# O sistema NÃO exibe nenhum pop-up de alerta.


# 🟠 [A4] - CONTA RECENTEMENTE PAGA
# ---------------------------------------------------------------

# O ator possuía uma conta a 3 dias do vencimento e realizou o pagamento.

# O ator acessa a página inicial da plataforma.

# O sistema verifica que a conta não está mais com o status "Aberta". [RN1]

# O sistema NÃO exibe o pop-up de alerta para essa conta.


# 🟣 [RN1] VERIFICAÇÃO DIÁRIA E ELEGIBILIDADE
# ---------------------------------------------------------------
# O sistema realiza diariamente a verificação de contas e cobranças que ainda não 
# foram pagas. São elegíveis para notificação as contas cujo vencimento esteja 
# dentro dos próximos 7 dias (por padrão), contados em dias corridos.

# 🟣 [RN2] PERMISSÃO DO USUÁRIO
# ---------------------------------------------------------------
# O pop-up só será exibido se o cooperado tiver habilitado a opção de 
# "receber notificações" em suas configurações de perfil/plataforma.

# 🟣 [RN3] PADRONIZAÇÃO DO TEXTO E DADOS EXIBIDOS
# ---------------------------------------------------------------
# O pop-up (fundo amarelo, canto superior direito) deve exibir a junção da mensagem modelo 
# com os dados exigidos:
# - Nome do cooperado;
# - Identificação da conta/cobrança;
# - Quantidade de dias restantes;
# - Valor original;
# - Data de vencimento.

# 🟣 [RN4] DIAS CORRIDOS E DIAS NÃO ÚTEIS
# ---------------------------------------------------------------
# A contagem de dias (ex: faltam 3 dias) considera sempre dias corridos. 
# Caso a data exata do vencimento seja sábado, domingo ou feriado cadastrado, 
# o sistema deve destacar isso no alerta.


# [DADOS] DADOS E RESULTADOS ESPERADOS
# ---------------------------------------------------------------

# Dados de teste (fictícios):
# - Cooperado: "João Silva" (Notificações ON)
# - Identificação da Conta: "Mensalidade - Parcela 01"
# - Valor original: R$ 500,00
# - Data atual: 10/10/2026
# - Data de vencimento: 15/10/2026 (Quinta-feira, dia útil)
# - Dias restantes: 5 dias
#
# Resultado esperado (Ao acessar a home):
# - Pop-up amarelo no canto superior direito.
# - Texto exibido: "Sócio(a) João Silva, faltam 5 dias para o vencimento da 
#   conta Mensalidade - Parcela 01. Valor: R$ 500,00 | Vencimento: 15/10/2026."
#
# Dados de teste alternativo (Fim de semana):
# - Data de vencimento: 17/10/2026 (Sábado)
# Resultado esperado: O mesmo alerta acima, com o adendo em destaque: 
# "(Atenção: O vencimento cai em um fim de semana/feriado)."