# Lista de alvos (Input)
emails = ["chefe@empresa.com", "cliente@gmail.com", "contato@outlook.com", "vendas@gmail.com"]

print("--- Iniciando Filtragem ---")
for email in emails:
    # Lógica de Decisão
    if "@gmail.com" in email:
        # Manipulação de String: pega só o nome antes do @
        nome_usuario = email.split("@")[0]
        print(f"✅ ENVIAR: {nome_usuario.upper()} ({email})")
    else:
        print(f"❌ PULAR: {email} (Não é Gmail)")