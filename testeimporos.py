import pyautogui
import time
import os

# --- 1. PREPARAÇÃO DOS DADOS (Back-end) ---
produtos = [
    {"nome": "Automação Python", "preco": 150.00},
    {"nome": "Curso de Linux", "preco": 80.00},
    {"nome": "Mentoria RPA", "preco": 250.00}
]

print("🤖 Robô iniciado... Prepare-se!")
time.sleep(2) # Tempo para você soltar o mouse

# --- 2. AUTOMAÇÃO DE INTERFACE (PyAutoGUI) ---
# Vamos abrir o Bloco de Notas (Notepad) pelo atalho do Windows
pyautogui.press('win')
time.sleep(1)
pyautogui.write('notepad')
pyautogui.press('enter')
time.sleep(2) # Espera o programa abrir

# Escrevendo o cabeçalho
pyautogui.write("=== RELATORIO DE VENDAS RPA ===")
pyautogui.press('enter')
pyautogui.press('enter')

# --- 3. LOOP DE AUTOMAÇÃO ---
for item in produtos:
    linha = f"Produto: {item['nome']} | Valor: R$ {item['preco']:.2f}"
    pyautogui.write(linha)
    pyautogui.press('enter')
    time.sleep(0.5) # Pequena pausa para parecer humano

pyautogui.press('enter')
pyautogui.write("Relatorio finalizado pelo bot do Coringa!")

print("✅ Missão cumprida!")