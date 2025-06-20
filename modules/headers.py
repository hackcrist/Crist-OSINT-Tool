import requests

url = input("🌐 Ingresa la URL (https://...): ").strip()
try:
    r = requests.get(url, timeout=5)
    print("✔️ Encabezados HTTP encontrados:")
    for k, v in r.headers.items():
        print(f"{k}: {v}")
except:
    print("⚠️ No se pudo acceder al sitio.")
