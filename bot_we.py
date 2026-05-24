import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# --- 1. CRIANDO DADOS (Simulando uma planilha de 5000 itens) ---
dados = {
    'Produto': ['Python Fluente', 'Monitor Gamer', 'Teclado Mecânico'],
    'Marca': ['O Reilly', 'Dell', 'Logitech']
}
df = pd.DataFrame(dados)
df.to_excel('produtos_para_pesquisa.xlsx', index=False)
print("📊 Planilha criada com sucesso!")

# --- 2. CONFIGURANDO O NAVEGADOR (Selenium) ---
# O Selenium vai abrir o Chrome. Certifique-se de que o Chrome está instalado.
driver = webdriver.Chrome() 

try:
    # --- 3. LENDO A PLANILHA ---
    planilha = pd.read_excel('produtos_para_pesquisa.xlsx')

    for index, linha in planilha.iterrows():
        produto = linha['Produto']
        marca = linha['Marca']
        termo_pesquisa = f"{produto} {marca}"

        print(f"🔎 Pesquisando por: {termo_pesquisa}")

        # Abre o Google
       from selenium.webdriver.chrome.options import Options

    options = Options()
# Isso evita que o Chrome feche sozinho ou dê erro de permissão em alguns PCs
options.add_argument("--start-maximized") 
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
        
        # Acha a barra de pesquisa
        caixa_busca = driver.find_element(By.NAME, "q")
        
        # Digita o nome do produto e dá ENTER
        caixa_busca.send_keys(termo_pesquisa)
        caixa_busca.send_keys(Keys.ENTER)

        time.sleep(3) # Tempo para você ver o resultado na tela
        
    print("✅ Todos os itens foram pesquisados!")

finally:
    time.sleep(2)
    driver.quit() # Fecha o navegador no final