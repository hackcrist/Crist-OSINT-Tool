email = input("📧 Ingresa un correo electrónico: ").strip()
if "@" not in email:
    print("❌ Correo inválido.")
else:
    print(f"✔️ {email} fue encontrado en breach_example.com (simulado)")
