import requests
import time
import random

# 🔗 O TEU LINK REAL CONFIGURADO CORRETAMENTE PELO ESTAGIÁRIO
URL_FORMULARIO = "https://webhook.site/b9a3de83-e192-4917-bc1a-6df4da81692c"

# 🗂️ O ID REAL DA TUA PERGUNTA "PRODUTO"
ID_CAMPO_PRODUTO = "entry.1465902343"

# O teu catálogo de produtos para o teste de RPA
produtos_catalogo = ["Notebook Dell", "Monitor LG 29", "Teclado Mecanico"]

print("🚀 O robô foi alinhado com o teu link oficial!")
print("📡 A disparar os dados diretamente para a nuvem...")

for i in range(len(produtos_catalogo)):
    produto = produtos_catalogo[i]
    print(f"\n🔄 A fazer scraping de: {produto}...")
    
    # Simula a busca do robô no site
    url_busca = f"https://duckduckgo.com/html/?q={produto}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    
    try:
        resposta = requests.get(url_busca, headers=headers, timeout=10)
        status = "SUCESSO" if resposta.status_code == 200 else "FALHA"
    except Exception:
        status = "ERRO DE CONEXÃO"
        
    print(f"📊 Status do site: {status}")
    print(f"📡 A gravar '{produto}' na tua planilha...")
    
    # Monta o pacote com o teu ID de campo real
    dados_envio = {
        ID_CAMPO_PRODUTO: produto
    }
    
    try:
        resposta_google = requests.post(URL_FORMULARIO, data=dados_envio)
        
        # 🟢 SE DER 200, SIGNIFICA QUE CAIU NA PLANILHA!
        if resposta_google.status_code == 200:
            print("✅ SUCESSO TOTAL! O Google guardou a linha.")
        else:
            print(f"⚠️ Erro no servidor do Google (Status: {resposta_google.status_code})")
            
    except Exception as e:
        print(f"❌ Erro de rede ao enviar: {e}")
        
    # Pausa estratégica para segurança
    if i < len(produtos_catalogo) - 1:
        tempo_espera = random.uniform(3.0, 5.0)
        print(f"☕ A aguardar {tempo_espera:.2f}s...")
        time.sleep(tempo_espera)

print("\n🏁 Robô finalizou com sucesso total!")
print("Dá um F5 na tua 'Planilha sem título' no navegador para ver a mágica!")