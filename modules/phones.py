import phonenumbers
from phonenumbers import geocoder, carrier

numero = input("📱 Ingresa el número telefónico (+52...): ").strip()
try:
    parsed = phonenumbers.parse(numero, None)
    pais = geocoder.country_name_for_number(parsed, "es")
    operador = carrier.name_for_number(parsed, "es")
    if pais:
        print(f"✔️ País: {pais}")
        print(f"📶 Operador: {operador if operador else 'No disponible'}")
    else:
        print("❌ Número no reconocido")
except:
    print("⚠️ Error al procesar el número.")
