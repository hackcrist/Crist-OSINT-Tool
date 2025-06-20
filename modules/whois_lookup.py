import socket

dominio = input("🔎 Ingresa un dominio o IP: ").strip()
try:
    ip = socket.gethostbyname(dominio)
    print(f"✔️ Dirección IP encontrada: {ip}")
except:
    print("❌ No se pudo obtener la IP.")
