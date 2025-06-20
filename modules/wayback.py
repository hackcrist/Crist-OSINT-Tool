# Consulta historial web en Wayback
import requests
url = input("🔗 Ingresa la URL del sitio: ").strip()
try:
    api = f"http://archive.org/wayback/available?url={url}"
    r = requests.get(api).json()
    if "archived_snapshots" in r and "closest" in r["archived_snapshots"]:
        snapshot = r["archived_snapshots"]["closest"]
        print(f"📅 Fecha: {snapshot['timestamp']}")
        print(f"🌍 Snapshot: {snapshot['url']}")
    else:
        print("❌ No hay historial encontrado.")
except:
    print("❌ Error al consultar Wayback.")
