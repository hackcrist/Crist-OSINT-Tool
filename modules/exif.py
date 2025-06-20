from PIL import Image
from PIL.ExifTags import TAGS

ruta = input("🖼️ Ruta de la imagen local (ej: /sdcard/foto.jpg): ").strip()
try:
    img = Image.open(ruta)
    exif = img._getexif()
    if exif:
        print("✔️ Metadatos EXIF encontrados:")
        for tag, val in exif.items():
            nombre = TAGS.get(tag, tag)
            print(f"{nombre}: {val}")
    else:
        print("❌ No se encontraron metadatos.")
except:
    print("⚠️ Error al abrir la imagen.")
