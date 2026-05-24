import requests
import time
import random

# 🔗 LINK DO SEU FORMULÁRIO (Configurado no modo de resposta automática)
URL_FORMULARIO = "https://docs.google.com/forms/d/e/1FAIpQLSdK_uR0DqppuqVv9CCnNCQ7BBAulzjz0gVUNdEkrelQBuaLww/formResponse"

# 🗂️ IDs DOS CAMPOS (Mapeados para a sua planilha na nuvem)
ID_CAMPO_PRODUTO = "entry.1465902343"  # O ID real que você pegou
ID_CAMPO_STATUS = "entry.1111111111"   # Campo 2
ID_CAMPO_HORARIO = "entry.2222222222"  # Campo 3

# Seu catálogo de produtos para simular o Scraping do trampo
produtos_catalogo = ["Notebook Dell", "Monitor LG 29", "Teclado Mecanico"]

print("🚀 O 'estagiário' ligou o motor! Iniciando envio direto para a nuvem...")

for i in range(len(produtos_catalogo)):
    produto = produtos_catalogo[i]
    print(f"\n🔄 Coletando dados de: {produto}...")
    
    # Simulando a requisição do robô no site
    url_busca = f"https://duckduckgo.com/html/?q={produto}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    
    try:
        resposta = requests.get(url_busca, headers=headers, timeout=10)
        status = "SUCESSO" if resposta.status_code == 200 else f"FALHA ({resposta.status_code})"
    except Exception:
        status = "ERRO DE CONEXÃO"
        
    horario = time.strftime('%H:%M:%S')
    print(f"📊 Resultado: {status}")
    
    # 📡 ENVIANDO PARA O GOOGLE SHEETS VIA WEB-REQUEST (Sem precisar de chaves/cartão)
    print(f"📡 Jogando '{produto}' direto para a nuvem...")
    
    dados_envio = {
        ID_CAMPO_PRODUTO: produto,
        ID_CAMPO_STATUS: status,
        ID_CAMPO_HORARIO: horario
    }
    
    try:
        # Envia os dados simulando o preenchimento do formulário
        resposta_google = requests.post(URL_FORMULARIO, data=dados_envio)
        if resposta_google.status_code == 200:
            print("✅ Sucesso! Dados gravados na planilha da Nuvem.")
        else:
            print(f"⚠️ Google respondeu com aviso (Status: {resposta_google.status_code})")
    except Exception as e:
        print(f"❌ Falha de conexão ao enviar: {e}")
    
    # Sua pausa tática anti-bloqueio (Segurança de Dados corporativa)
    if i < len(produtos_catalogo) - 1:
        tempo_espera = random.uniform(3.0, 5.0)
        print(f"☕ Cadência inteligente: aguardando {tempo_espera:.2f}s...")
        time.sleep(tempo_espera)

print("\n🏁 Robô finalizou 100%! Abra a aba de 'Respostas' do seu Formulário ou a Planilha vinculada para ver a mágica!")