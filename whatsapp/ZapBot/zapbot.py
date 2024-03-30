"""
PRECISO AUTOMMATIZAR MINHAS MENSAGENS P/ MEUS CLIENTES
GOSTARIA DE SABER VALORES, E GOSTARIA QUE  ENTRASSEM EM
CONTATO COMIGO P/ EXPLICAR MELHOR, QUERO PODER MANDAR 
MENSAGENS DE COBRANÇA EM DETERMINADO DIA COM CLIENTES COM
VENCIMENTO DIFERENTE
"""

import openpyxl
# ler planilha e guardar informações sobre nome, telefone e data de vencimento

workbook = openpyxl.load_workbook('clientes.xlsx')
pagina_clientes = workbook['Planilha1']

for linha in pagina_clientes.iter_rows(min_row=2):
    # nome, telefone e data de vencimento
    nome = linha[0]



# criar links personalizados do whatsapp e enviar mensagens
# para cada cliente

#com base nos dados da planilna 


