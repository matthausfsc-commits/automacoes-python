import requests
import time
import random
import gspread

print("🤖 Iniciando o robô de forma segura e 100% gratuita...")

try:
    # 🔐 AUTENTICAÇÃO OAUTH: Vai abrir o seu navegador na primeira vez
    # Ele vai criar uma pasta automática chamada 'gspread' no seu PC para salvar o acesso
    cliente_google = gspread.oauth(authorized_user_filename='authorized_user.json')
    
    # 📝 ABRE A PLANILHA: Busca o arquivo direto no seu Google Drive pelo nome
    planilha = cliente_google.open("Relatorio_RPA_Produtos").sheet1
    print("✅ Conectado ao Google Sheets com sucesso!")
except Exception as e:
    print(f"❌ Erro de Autenticação: {e}")
    print("💡 Certifique-se de que criou a planilha 'Relatorio_RPA_Produtos' no seu Google Drive.")
    exit()

# Seu catálogo de produtos para o scraping
produtos_catalogo = ["Notebook Dell", "Monitor LG 29", "Teclado Mecanico"]

# Garante que a planilha tem o cabeçalho se estiver vazia
try:
    if planilha.row_count == 0 or planilha.cell(1, 1).value == "":
        planilha.append_row(["Produto", "Status", "Horario Log"])
except Exception:
    # Se der erro ao ler célula vazia, nós inserimos o cabeçalho de qualquer forma
    planilha.append_row(["Produto", "Status", "Horario Log"])

print("\n🚀 Começando o Scraping e a alimentação da planilha...")

# Laço "for i in range" cuidando de cada índice com estratégia anti-bloqueio
for i in range(len(produtos_catalogo)):
    produto = produtos_catalogo[i]
    print(f"🔄 Scrapeando dados de: {produto}...")
    
    url = f"https://duckduckgo.com/html/?q={produto}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    
    try:
        resposta = requests.get(url, headers=headers, timeout=10)
        status = "SUCESSO" if resposta.status_code == 200 else f"FALHA ({resposta.status_code})"
    except Exception as e:
        status = "ERRO DE CONEXÃO"
        
    horario = time.strftime('%H:%M:%S')
    
    # ☁️ ENVIO EM TEMPO REAL: Salvando direto na nuvem do Google
    print(f"💾 Jogando '{produto}' para a planilha do Google...")
    planilha.append_row([produto, status, horario])
    
    # Pausa estratégica para segurança de dados / Anti-Block (Rate Limiting)
    if i < len(produtos_catalogo) - 1:
        tempo_espera = random.uniform(3.0, 5.0)
        print(f"☕ Cadência inteligente: aguardando {tempo_espera:.2f}s...")
        time.sleep(tempo_espera)

print("\n🏁 Robô finalizou com sucesso! Olhe a sua planilha no navegador, os dados já estão lá!")