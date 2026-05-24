import pandas as pd

# 1. Criamos dados fictícios de vendas de um e-commerce filosófico
dados = {
    'ID_Pedido': [1001, 1002, 1003, 1004, 1005],
    'Produto': ['Livro - Meditações (Sêneca)', 'Curso - Automação com Python', 'Camiseta - O Mito da Caverna', 'Caneca - Code & Stoicism', 'Livro - Assim Falou Zarandustra'],
    'Quantidade': [2, 1, 1, 3, 1],
    'Preco_Unitario': [45.90, 299.00, 59.90, 35.00, 49.90],
    'Status': ['Enviado', 'Concluído', 'Pendente', 'Concluído', 'Enviado']
}

# 2. Transformamos o dicionário em um DataFrame do Pandas
df = pd.DataFrame(dados)

# 3. Criamos uma coluna calculada automaticamente (Burocracia que o Python ama!)
df['Total_Faturado'] = df['Quantidade'] * df['Preco_Unitario']

# 4. Salvamos os dados em uma planilha real do Excel
nome_arquivo = 'relatorio_vendas_ficticio.xlsx'
df.to_excel(nome_arquivo, index=False)

print(f"🔥 Sucesso! Planilha '{nome_arquivo}' gerada com valores fictícios.")