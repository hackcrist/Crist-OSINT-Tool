# Verifica si un correo fue filtrado en bases públicas
import requests
email = input("📧 Ingresa un correo electrónico: ").strip()
print("🔍 Consultando API de brechas públicas (demo)...")
# Demo con URL simulada
print(f"🔒 El correo '{email}' fue encontrado en: breach_example.com (simulado)")