import requests
import time
import random

# Lista de produtos para o teste
produtos_catalogo = ["Notebook Dell", "Monitor LG 29", "Teclado Mecanico"]

nome_arquivo = "relatorio_produtos.txt"
resultados = []  # Lista temporária para guardar as informações na memória

print("🤖 Iniciando o robô...")

for i in range(len(produtos_catalogo)):
    produto = produtos_catalogo[i]
    print(f"🔄 Solicitando dados de: {produto}...")
    
    url = f"https://duckduckgo.com/html/?q={produto}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    
    try:
        resposta = requests.get(url, headers=headers, timeout=10)
        if resposta.status_code == 200:
            status = "SUCESSO"
        else:
            status = f"FALHA (Status: {resposta.status_code})"
    except Exception as e:
        status = f"ERRO DE CONEXÃO ({e})"
        
    print(f"📊 Resultado: {status}")
    
    # Guarda o texto na nossa lista temporária
    linha = f"Item: {produto} | Status: {status} | Horário: {time.strftime('%H:%M:%S')}\n"
    resultados.append(linha)
    
    # Sua pausa tática para evitar captcha
    if i < len(produtos_catalogo) - 1:
        tempo_espera = random.uniform(3.0, 5.0)
        print(f"☕ Aguardando {tempo_espera:.2f}s...")
        time.sleep(tempo_espera)

# --- GRAVAÇÃO DOS DADOS (Só acontece no final) ---
print("\n💾 Salvando o relatório definitivo...")
with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.write("=== RELATÓRIO DE PROCESSAMENTO RPA ===\n\n")
    for linha in resultados:
        arquivo.write(linha)

print(f"🚀 Concluído! Agora feche o Bloco de Notas antigo e abra de novo.")