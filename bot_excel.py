import requests
import time
import random
import pandas as pd  # Biblioteca que cria o Excel de forma profissional

# Lista de produtos para simular o seu catálogo
produtos_catalogo = ["Notebook Dell", "Monitor LG 29", "Teclado Mecanico", "Mouse Corsair"]

# Lista para acumular os dados na memória antes de salvar
dados_finais = []

print("🤖 Iniciando o robô com estratégia anti-captcha...")

for i in range(len(produtos_catalogo)):
    produto = produtos_catalogo[i]
    print(f"🔄 Coletando dados de: {produto}...")
    
    url = f"https://duckduckgo.com/html/?q={produto}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    
    try:
        resposta = requests.get(url, headers=headers, timeout=10)
        status = "SUCESSO" if resposta.status_code == 200 else f"FALHA ({resposta.status_code})"
    except Exception as e:
        status = f"ERRO DE CONEXÃO"
        
    print(f"📊 Resultado: {status}")
    
    # Em vez de texto puro, salvamos como um dicionário (estrutura de tabela)
    dados_finais.append({
        "Produto": produto,
        "Status do Acesso": status,
        "Horario do Log": time.strftime('%H:%M:%S')
    })
    
    # Sua pausa estratégica (Vibe Coding / Anti-Block)
    if i < len(produtos_catalogo) - 1:
        tempo_espera = random.uniform(3.0, 5.0)
        print(f"☕ Cadência inteligente: aguardando {tempo_espera:.2f}s...")
        time.sleep(tempo_espera)

# --- GRAVAÇÃO DIRETA NO EXCEL ---
print("\n📊 Convertendo dados para o formato do Excel...")

# O Pandas transforma a lista de dicionários em um DataFrame (uma tabela na memória)
df = pd.DataFrame(dados_finais)

# Salva a tabela como um arquivo .xlsx verdadeiro
nome_planilha = "relatorio_final.xlsx"
df.to_excel(nome_planilha, index=False)

print(f"🚀 Pronto! Planilha criada com sucesso: {nome_planilha}")