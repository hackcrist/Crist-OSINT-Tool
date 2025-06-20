# Ver encabezados HTTP de un sitio web
import requests
url = input("🌐 Ingresa la URL (https://...): ").strip()
try:
    r = requests.get(url)
    print("🧾 Encabezados:")
    for k, v in r.headers.items():
        print(f"{k}: {v}")
except:
    print("❌ No se pudo conectar al sitio.")
