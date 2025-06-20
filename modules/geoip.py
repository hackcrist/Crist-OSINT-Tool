import requests

ip = input("🌍 Ingresa una IP: ").strip()
try:
    r = requests.get(f"http://ip-api.com/json/{ip}", timeout=5).json()
    if r["status"] == "success":
        print(f"✔️ Ciudad: {r['city']}, País: {r['country']}")
        print(f"🌐 ISP: {r['isp']}, Latitud: {r['lat']}, Longitud: {r['lon']}")
    else:
        print("❌ IP no encontrada.")
except:
    print("⚠️ Error al conectar con la API.")
