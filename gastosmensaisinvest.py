import pandas as pd
from tabulate import tabulate

# ==========================================
# VARIÁVEIS REAIS DOS SEUS HOLERITES
# ==========================================
VALE_DIA_15 = 709.00
SALARIO_FIM_MES = 927.84

# Divisão exata dos seus gastos fixos
CASA_VALE = 325.00
CASA_SALARIO = 500.00

# MUDANÇA DA QUITAÇÃO: Você paga os R$ 100 finais no dia 15/06 e zera!
QUITACAO_PC_JUNHO = 100.00 

# Divisão das suas metas de investimento por quinzena
FUNDO_POR_QUINZENA = 40.00  # Total de R$ 80 no mês
ACOES_POR_QUINZENA = 12.50  # Total de R$ 25 no mês (1 ou 2 ações baratas)

# ==========================================
# PROCESSAMENTO DOS FLUXOS (LOGICA DE CAIXA)
# ==========================================

# 1. Fluxo do Vale (Dia 15 de Junho) - Mês da Quitação
sobra_vale_junho = VALE_DIA_15 - CASA_VALE - QUITACAO_PC_JUNHO - FUNDO_POR_QUINZENA - ACOES_POR_QUINZENA
fluxo_vale = {
    "Fluxo Quinzena 1 (Vale - Junho)": [
        "(+) Entrada (Adiantamento/Vale)",
        "(-) Conta de Casa (Metade)",
        "(-) QUITAÇÃO FINAL DO PC (Últimos R$ 100)",
        "(-) Fundo de Emergência",
        "(-) Investimento (1ª Ação)",
        "(=) DINHEIRO LIVRE NA QUINZENA"
    ],
    "Valor (R$)": [
        VALE_DIA_15,
        -CASA_VALE,
        -QUITACAO_PC_JUNHO,
        -FUNDO_POR_QUINZENA,
        -ACOES_POR_QUINZENA,
        sobra_vale_junho
    ],
    "Nota de Execução": [
        "Cai todo dia 15",
        "Sua parte da 1ª quinzena",
        "R$ 50 de Junho + R$ 50 de Maio. Adeus dívida!",
        "Guardar direto na Caixinha CDI",
        "Enviar para a Corretora",
        "Dinheiro livre mesmo quitando o PC!"
    ]
}

# 2. Fluxo do Salário (Fim do Mês) - Daqui para a frente (SEM PC)
sobra_salario_futuro = SALARIO_FIM_MES - CASA_SALARIO - FUNDO_POR_QUINZENA - ACOES_POR_QUINZENA
fluxo_salario = {
    "Fluxo Quinzena 2 (Salário - Futuro)": [
        "(+) Entrada (Salário Líquido)",
        "(-) Conta de Casa (Metade restante)",
        "(-) Parcela do PC",
        "(-) Fundo de Emergência",
        "(-) Investimento (2ª Ação)",
        "(=) DINHEIRO LIVRE NA QUINZENA"
    ],
    "Valor (R$)": [
        SALARIO_FIM_MES,
        -CASA_SALARIO,
        0.00,  # ZERADO!
        -FUNDO_POR_QUINZENA,
        -ACOES_POR_QUINZENA,
        sobra_salario_futuro
    ],
    "Nota de Execução": [
        "Cai no final do mês",
        "Sua parte da 2ª quinzena",
        "CUSTO DELETADO! R$ 0.00",
        "Guardar direto na Caixinha CDI",
        "Enviar para a Corretora",
        "Sobrou muito mais dinheiro limpo!"
    ]
}

# Convertendo para DataFrames do Pandas
df_vale = pd.DataFrame(fluxo_vale)
df_salario = pd.DataFrame(fluxo_salario)

# Formatando os valores para exibição em Real (R$)
df_vale["Valor (R$)"] = df_vale["Valor (R$)"].map("R$ {:.2f}".format)
df_salario["Valor (R$)"] = df_salario["Valor (R$)"].map("R$ {:.2f}".format)

# ==========================================
# OUTPUT NO TERMINAL
# ==========================================
print("\n" + "="*85)
print("          SISTEMA ATUALIZADO: PARCELA DO PC DELETADA COM SUCESSO!")
print("="*85)

print("\n[EXECUÇÃO] DIA 15 DE JUNHO: MÊS DA QUITAÇÃO")
print(tabulate(df_vale, headers='keys', tablefmt='fancy_grid', showindex=False))

print("\n[EXECUÇÃO] DAQUI PRA FRENTE: SEU SALÁRIO LIVRE DA DÍVIDA DO PC")
print(tabulate(df_salario, headers='keys', tablefmt='fancy_grid', showindex=False))

print("\n" + "="*85)
print(f" NOVO CENÁRIO: Sem a parcela do PC, sua sobra no fim do mês pula para R$ {sobra_salario_futuro:.2f}!")
print("="*85 + "\n")