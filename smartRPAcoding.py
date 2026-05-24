import requests
import time
import random  # O segredo para deixar o "range" ainda mais humano

# Lista de produtos para simular o seu catálogo
produtos_catalogo = ["Notebook Dell", "Monitor LG 29", "Teclado Mecanico", "Mouse Corsair"]

print("🤖 Iniciando o robô com a estratégia de cadência...")

# O seu loop pegando cada item da lista
for i in range(len(produtos_catalogo)):
    produto = produtos_catalogo[i]
    print(f"\n🔄 [Item {i+1}/{len(produtos_catalogo)}] Processando: {produto}")
    
    # 1. Faz a requisição (o robô trabalha)
    url = f"https://duckduckgo.com/html/?q={produto}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    
    resposta = requests.get(url, headers=headers)
    
    if resposta.status_code == 200:
        print(f"✅ Dados de '{produto}' coletados!")
    else:
        print(f"⚠️ Status inesperado: {resposta.status_code}")
        
    # 2. A SUA ESTRATÉGIA: O robô "finge" que está lendo a página
    # Em vez de um tempo fixo, usamos o random para flutuar entre 4 e 8 segundos.
    # Por que? Porque humanos não esperam cravados 5 segundos em cada página.
    tempo_espera = random.uniform(4.0, 8.0)
    
    # Só não aplica a pausa no último item para o script não herdar tempo morto
    if i < len(produtos_catalogo) - 1:
        print(f"☕ Pausa tática de {tempo_espera:.2f}s para limpar o Rate Limit...")
        time.sleep(tempo_espera)

print("\n🚀 Relatório finalizado sem estourar o limite do servidor!")