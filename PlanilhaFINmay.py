import pandas as pd
from tabulate import tabulate

# ==========================================
# CONSTANTES - VARIÁVEIS DO SEU ORÇAMENTO
# ==========================================
SALARIO_FIM_MES = 927.84  # Líquido do Holerite
VALE_MEIO_MES = 709.00    # Seu Adiantamento

CASA_FIM_MES = 500.00     # Sua parte de casa no fim do mês
CASA_MEIO_MES = 325.00    # Sua parte de casa no meio do mês

PC_PARCELA_REDUZIDA = 100.00  # R$ 150 - R$ 50 (congelados para junho)
PC_PARCELA_EMENDADA = 100.00  # R$ 50 normal de junho + R$ 50 congelados

FATURA_CARTAO_ESTIMADA = 420.00  # R$ 300 originais + Pix no crédito (~R$ 66.68 + R$ 40 + taxas)
GATO_GASTO_MAIO = 112.84         # Limite máximo de gasto em dinheiro vivo com frutas/básico

# ==========================================
# ESTRUTURAÇÃO DO FLUXO DE CAIXA
# ==========================================

# 1. Dados da Etapa 1: Fim de Maio (Sobrevivência com Caixa Alto)
dados_maio = {
    "Métrica": [
        "(+) Entrada (Salário Líquido)",
        "(-) Conta de Casa",
        "(-) Parcelamento PC (Esposo da Mãe)",
        "(=) SALDO LIVRE NA CONTA",
        "(-) Gasto com Frutas/Essencial (Até 09/06)",
        "(=) DINHEIRO GUARDADO PARA JUNHO"
    ],
    "Valor (R$)": [
        SALARIO_FIM_MES,
        -CASA_FIM_MES,
        -PC_PARCELA_REDUZIDA,
        SALARIO_FIM_MES - CASA_FIM_MES - PC_PARCELA_REDUZIDA,
        -GATO_GASTO_MAIO,
        (SALARIO_FIM_MES - CASA_FIM_MES - PC_PARCELA_REDUZIDA) - GATO_GASTO_MAIO
    ],
    "Status / Instrução": [
        "Cai na conta na próxima semana",
        "Depósito sagrado da sua parte",
        "R$ 50 congelados aceitos pelo padrasto",
        "Dinheiro físico disponível na conta",
        "Segurar a onda com rédea curta aqui!",
        "NÃO MEXER! Reservado para matar o cartão"
    ]
}

# 2. Dados da Etapa 2: Meio de Junho (O Abatimento Total)
dinheiro_guardado = dados_maio["Valor (R$)"][5]
sobra_vale = VALE_MEIO_MES - CASA_MEIO_MES - PC_PARCELA_EMENDADA

dados_junho = {
    "Métrica": [
        "(+) Entrada (Vale/Adiantamento)",
        "(-) Conta de Casa",
        "(-) Parcelamento PC (Quitação + Junho)",
        "(=) Sobra Limpa do Vale",
        "(+) Dinheiro Guardado de Maio",
        "(=) CAIXA TOTAL PARA O CARTÃO",
        "(-) Quitação da Fatura (Vencimento)",
        "(=) SALDO FINAL PÓS-CRISE"
    ],
    "Valor (R$)": [
        VALE_MEIO_MES,
        -CASA_MEIO_MES,
        -PC_PARCELA_EMENDADA,
        sobra_vale,
        dinheiro_guardado,
        sobra_vale + dinheiro_guardado,
        -FATURA_CARTAO_ESTIMADA,
        (sobra_vale + dinheiro_guardado) - FATURA_CARTAO_ESTIMADA if 'dinero_guardado' not in locals() else (sobra_vale + dinheiro_guardado) - FATURA_CARTAO_ESTIMADA
    ],
    "Status / Instrução": [
        "Cai dia 15 de Junho",
        "Sua metade da quinzena",
        "Paga os R$ 50 de junho + R$ 50 de maio. Dívida com ele em dia!",
        "Dinheiro limpo do mês corrente",
        "Dinheiro que você segurou bravamente em maio",
        "Sua emenda perfeita de valores",
        "Pago no dia do vencimento. JURO ZERO!",
        "CARTÃO 100% LIVRE E EMPRESA NO GREEN!"
    ]
}

# Convertendo para DataFrames do Pandas
df_maio = pd.DataFrame(dados_maio)
df_junho = pd.DataFrame(dados_junho)

# Formatando a coluna de valores para ficar em Moeda Real (R$)
df_maio["Valor (R$)"] = df_maio["Valor (R$)"].map("R$ {:.2f}".format)
df_junho["Valor (R$)"] = df_junho["Valor (R$)"].map("R$ {:.2f}".format)

# ==========================================
# OUTPUT NO TERMINAL (PRINTS DETALHADOS)
# ==========================================
print("\n" + "="*80)
print("             SISTEMA DE FLUXO DE CAIXA: OPERAÇÃO ANTI-JUROS 2026")
print("="*80)

print("\n### ETAPA 1: FIM DE MAIO (Garantir dinheiro em conta e segurar o cartão)")
print(tabulate(df_maio, headers='keys', tablefmt='fancy_grid', showindex=False))

print("\n### ETAPA 2: MEIO DE JUNHO (A Emenda dos valores e Libertação do Cartão)")
print(tabulate(df_junho, headers='keys', tablefmt='fancy_grid', showindex=False))

print("\n" + "="*80)
print(" NOTA DO SISTEMA: Seguindo esse script, o juro do cartão é R$ 0.00!")
print("="*80 + "\n")