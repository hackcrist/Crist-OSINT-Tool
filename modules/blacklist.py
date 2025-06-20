ip = input("🔍 Ingresa la IP a verificar: ").strip()
print(f"🛑 Consultando bases públicas...")

# Modo educativo: simulación
if ip.startswith("127.") or ip == "0.0.0.0":
    print("❌ IP sospechosa (simulado)")
else:
    print("✔️ IP no aparece en listas negras conocidas (simulado)")
