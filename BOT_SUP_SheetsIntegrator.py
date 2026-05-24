import requests
import time
import random
import os
import gspread
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv

# 🛡️ SEGURANÇA DE DADOS: Carrega as variáveis de ambiente escondidas
load_dotenv()

# Configura as permissões que o robô terá no Google Drive/Sheets
SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

print("🤖 Iniciando autenticação segura com o Google Sheets...")
try:
    # O robô busca o arquivo de credenciais com menor privilégio
    credenciais = Credentials.from_service_account_file('credentials.json', scopes=SCOPES)
    cliente_google = gspread.authorize(credenciais)
    
    # 📝 ABRE A PLANILHA: Substitua pelo nome exato da sua planilha do Google
    planilha = cliente_google.open("Relatorio_RPA_Produtos").sheet1
    print("✅ Conectado ao Google Sheets com sucesso!")
except Exception as e:
    print(f"❌ Erro de Autenticação/Segurança: {e}")
    exit()

# Seu catálogo de produtos
produtos_catalogo = ["Notebook Dell", "Monitor LG 29", "Teclado Mecanico"]

# Garante que a planilha tem o cabeçalho se estiver vazia
if planilha.row_count == 0 or planilha.cell(1, 1).value == "":
    planilha.append_row(["Produto", "Status", "Horario Log"])

print("\n🚀 Começando o Scraping...")

# Laço estruturado cuidando de cada índice
for i in range(len(produtos_catalogo)):
    produto = produtos_catalogo[i]
    print(f"🔄 Scrapeando: {produto}...")
    
    url = f"https://duckduckgo.com/html/?q={produto}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    
    try:
        resposta = requests.get(url, headers=headers, timeout=10)
        status = "SUCESSO" if resposta.status_code == 200 else f"FALHA ({resposta.status_code})"
    except Exception as e:
        status = "ERRO DE CONEXÃO"
        
    horario = time.strftime('%H:%M:%S')
    
    # ☁️ ENVIO DIRETO PARA A NUVEM (Google Sheets)
    print(f"💾 Salvando '{produto}' direto na nuvem...")
    planilha.append_row([produto, status, horario])
    
    # Pausa estratégica para não tomar block e respeitar o servidor (Rate Limiting)
    if i < len(produtos_catalogo) - 1:
        tempo_espera = random.uniform(3.0, 5.0)
        print(f"☕ Evitando bloqueios, aguardando {tempo_espera:.2f}s...")
        time.sleep(tempo_espera)

print("\n🏁 Robô finalizou! Pode abrir o seu navegador que os dados já estão lá!")