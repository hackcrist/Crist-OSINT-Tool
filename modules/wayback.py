import requests

url = input("🔗 Ingresa la URL del sitio: ").strip()
try:
    r = requests.get(f"http://archive.org/wayback/available?url={url}", timeout=5).json()
    snap = r.get("archived_snapshots", {}).get("closest", None)
    if snap:
        print(f"✔️ Snapshot encontrado:")
        print(f"📅 Fecha: {snap['timestamp']}")
        print(f"🌍 URL: {snap['url']}")
    else:
        print("❌ No hay historial archivado.")
except:
    print("⚠️ Error al contactar con Wayback.")
