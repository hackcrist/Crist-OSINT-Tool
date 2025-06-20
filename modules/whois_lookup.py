# WHOIS simple
import socket
dominio = input("🔎 Ingresa un dominio o IP: ").strip()
try:
    print(f"🧠 Información de WHOIS para: {dominio}")
    print(socket.gethostbyname(dominio))
except:
    print("❌ No se pudo obtener el WHOIS")
