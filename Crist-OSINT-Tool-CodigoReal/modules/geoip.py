# Geolocalización IP real
import requests
ip = input("🌍 Ingresa una IP: ").strip()
try:
    r = requests.get(f"http://ip-api.com/json/{ip}").json()
    if r["status"] == "success":
        print(f"📍 Ciudad: {r['city']}, País: {r['country']}")
        print(f"🌐 ISP: {r['isp']}, Latitud: {r['lat']}, Longitud: {r['lon']}")
    else:
        print("❌ No se encontró información.")
except:
    print("❌ Error al consultar la IP.")
