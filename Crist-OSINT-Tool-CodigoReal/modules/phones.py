# Valida número telefónico
import phonenumbers
from phonenumbers import geocoder, carrier

numero = input("📱 Ingresa el número telefónico con código de país (+52...): ").strip()
try:
    parsed = phonenumbers.parse(numero, None)
    print("🌎 País:", geocoder.country_name_for_number(parsed, "es"))
    print("📶 Operador:", carrier.name_for_number(parsed, "es"))
except:
    print("❌ Número inválido")
