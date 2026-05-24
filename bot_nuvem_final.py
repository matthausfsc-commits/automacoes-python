import requests
import time
import random

# 🔗 O SEU LINK REAL DO GOOGLE FORMS (Ajustado para enviar respostas)
URL_FORMULARIO = "https://docs.google.com/forms/d/e/1FAIpQLSdK_uR0DqppuqVv9CCnNCQ7BBAulzjz0gVUNdEkrelQBuaLww/formResponse"

# 🗂️ O SEU ID REAL DA PERGUNTA DO PRODUTO
ID_CAMPO_PRODUTO = "entry.1465902343"

# Seu catálogo de produtos para o teste
produtos_catalogo = ["Notebook Dell", "Monitor LG 29", "Teclado Mecanico"]

print("🚀 Iniciando o robô real conectado à SUA estrutura na nuvem...")

for i in range(len(produtos_catalogo)):
    produto = produtos_catalogo[i]
    print(f"\n🔄 Fazendo scraping de: {produto}...")
    
    # Simula a busca no site
    url_busca = f"https://duckduckgo.com/html/?q={produto}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    
    try:
        resposta = requests.get(url_busca, headers=headers, timeout=10)
        status = "SUCESSO" if resposta.status_code == 200 else f"FALHA ({resposta.status_code})"
    except Exception:
        status = "ERRO DE CONEXÃO"
        
    print(f"📊 Resultado do site: {status}")
    
    # 📡 ENVIANDO DIRETAMENTE PARA O SEU GOOGLE FORMS REAL
    print(f"📡 Gravando '{produto}' na sua planilha via Forms...")
    
    # Como por enquanto só temos 1 pergunta configurada lá, enviamos só ela
    dados_envio = {
        ID_CAMPO_PRODUTO: produto
    }
    
    try:
        resposta_google = requests.post(URL_FORMULARIO, data=dados_envio)
        if resposta_google.status_code == 200:
            print("✅ Sucesso! Dado computado com sucesso na nuvem.")
        else:
            print(f"⚠️ O Google recusou o envio (Status: {resposta_google.status_code})")
    except Exception as e:
        print(f"❌ Erro crítico de rede: {e}")
        
    # Pausa estratégica tática anti-block
    if i < len(produtos_catalogo) - 1:
        tempo_espera = random.uniform(3.0, 5.0)
        print(f"☕ Aguardando {tempo_espera:.2f}s para o próximo produto...")
        time.sleep(tempo_espera)

print("\n🏁 Robô finalizou 100%!")
print("Agora vá no seu navegador e abra a sua planilha ('Planilha sem título') para ver os dados!")