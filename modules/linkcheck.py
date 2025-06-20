import requests

url = input("🔗 Ingresa la URL sospechosa: ").strip()
try:
    r = requests.get(url, timeout=5)
    if r.status_code == 200:
        print("✔️ Sitio accesible")
    else:
        print(f"❌ Código HTTP recibido: {r.status_code}")
except:
    print("⚠️ Sitio no accesible")
