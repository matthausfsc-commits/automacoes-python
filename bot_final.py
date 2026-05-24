import os
import time

# --- AUTO-INSTALAÇÃO DE BIBLIOTECAS ---
# Isso garante que o openpyxl e pandas estejam aí
try:
    import pandas as pd
    import openpyxl
    from selenium import webdriver
except ImportError:
    print("Instalando bibliotecas faltantes... aguarde.")
    os.system('pip install pandas openpyxl selenium')
    import pandas as pd
    from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# --- 1. PREPARAÇÃO DOS DADOS ---
dados = {
    'Produto': ['Python Fluente', 'Monitor Gamer', 'Teclado Mecânico'],
    'Marca': ['Livro', 'Dell', 'Logitech']
}
df = pd.DataFrame(dados)
df.to_excel('lista_pesquisa.xlsx', index=False)
print("✅ Planilha 'lista_pesquisa.xlsx' criada!")

# --- 2. CONFIGURAÇÃO DO NAVEGADOR ---
import os
import time

# --- AUTO-INSTALAÇÃO DE BIBLIOTECAS ---
# Isso garante que o openpyxl e pandas estejam aí
try:
    import pandas as pd
    import openpyxl
    from selenium import webdriver
except ImportError:
    print("Instalando bibliotecas faltantes... aguarde.")
    os.system('pip install pandas openpyxl selenium')
    import pandas as pd
    from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# --- 1. PREPARAÇÃO DOS DADOS ---
dados = {
    'Produto': ['Python Fluente', 'Monitor Gamer', 'Teclado Mecânico'],
    'Marca': ['Livro', 'Dell', 'Logitech']
}
df = pd.DataFrame(dados)
df.to_excel('lista_pesquisa.xlsx', index=False)
print("✅ Planilha 'lista_pesquisa.xlsx' criada!")

# --- 2. CONFIGURAÇÃO DO NAVEGADOR ---
chrome_options = Options()
chrome_options.add_experimental_option("detach", True) # Mantém o navegador aberto
chrome_options.add_argument("--start-maximized")       # Abre em tela cheia

try:
    print("🤖 Iniciando o Chrome...")
    driver = webdriver.Chrome(options=chrome_options)

    # --- 3. PROCESSO DE RPA ---
    for index, linha in df.iterrows():
        termo = f"{linha['Produto']} {linha['Marca']}"
        
        print(f"🔎 Pesquisando: {termo}")
        driver.get("https://www.google.com")
        
        # Espera 1 segundo para o Google carregar
        time.sleep(1) 
        
        # Localiza a barra de pesquisa (o nome do campo no Google é 'q')
        caixa_busca = driver.find_element(By.NAME, "q")
        caixa_busca.send_keys(termo)
        caixa_busca.send_keys(Keys.ENTER)
        
        # Espera 3 segundos para você ver o resultado antes de ir para o próximo
        time.sleep(3)

    print("🚀 Automação finalizada com sucesso!")

except Exception as e:
    print(f"❌ Ocorreu um erro: {e}")

# driver.quit() # Descomente esta linha se quiser que o Chrome feche sozinho no fim
chrome_options.add_experimental_option("detach", True) # Mantém o navegador aberto
chrome_options.add_argument("--start-maximized")       # Abre em tela cheia

try:
    print("🤖 Iniciando o Chrome...")
    driver = webdriver.Chrome(options=chrome_options)

    # --- 3. PROCESSO DE RPA ---
    for index, linha in df.iterrows():
        termo = f"{linha['Produto']} {linha['Marca']}"
        
        print(f"🔎 Pesquisando: {termo}")
        driver.get("https://www.google.com")
        
        # Espera 1 segundo para o Google carregar
        time.sleep(1) 
        
        # Localiza a barra de pesquisa (o nome do campo no Google é 'q')
        caixa_busca = driver.find_element(By.NAME, "q")
        caixa_busca.send_keys(termo)
        caixa_busca.send_keys(Keys.ENTER)
        
        # Espera 3 segundos para você ver o resultado antes de ir para o próximo
        time.sleep(3)

    print("🚀 Automação finalizada com sucesso!")

except Exception as e:
    print(f"❌ Ocorreu um erro: {e}")

# driver.quit() # Descomente esta linha se quiser que o Chrome feche sozinho no fim