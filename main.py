#!/usr/bin/env python3
import os
import sys
from time import sleep

# Colores
verde = "\033[92m"
azul = "\033[94m"
amarillo = "\033[93m"
rojo = "\033[91m"
reset = "\033[0m"

# Mensaje educativo
def mensaje_educativo():
    print(f"{amarillo}⚠️ Herramienta creada con fines educativos. El mal uso es responsabilidad del usuario.{reset}")
    sleep(1)

# Abrir canal de YouTube automáticamente
def abrir_youtube():
    os.system("xdg-open https://www.youtube.com/@TechConWin >/dev/null 2>&1 &")

# Menú principal
def mostrar_menu():
    os.system("clear")
    print(f"{verde}══════════ 🎯 Crist-OSINT-Tool 🎯 ══════════{reset}")
    print(f"{azul}          Proyecto ético de OSINT{reset}")
    print()
    print(f"{verde} 1.{reset} Buscar en redes sociales       {verde} 7.{reset} Verificar IP en blacklist")
    print(f"{verde} 2.{reset} Buscar correos filtrados       {verde} 8.{reset} Headers HTTP")
    print(f"{verde} 3.{reset} Buscar número de teléfono      {verde} 9.{reset} Historial web (Wayback)")
    print(f"{verde} 4.{reset} Extraer metadatos EXIF        {verde}10.{reset} Whois dominio/IP")
    print(f"{verde} 5.{reset} Geolocalización de IP         {verde}11.{reset} Analizar links sospechosos")
    print(f"{verde} 6.{reset} Generar reporte local          {verde}12.{reset} Guardar informe manual")
    print()
    print(f"{rojo} 0.{reset} Salir")
    print("══════════════════════════════════════════")

# Ejecutar módulo según opción
def ejecutar_opcion(op):
    modulos = {
        "1": "modules/redes.py",
        "2": "modules/leaks.py",
        "3": "modules/phones.py",
        "4": "modules/exif.py",
        "5": "modules/geoip.py",
        "6": "utils/save_report.py",
        "7": "modules/blacklist.py",
        "8": "modules/headers.py",
        "9": "modules/wayback.py",
        "10": "modules/whois_lookup.py",
        "11": "modules/linkcheck.py",
        "12": "utils/save_report.py"
    }
    if op in modulos:
        os.system(f"python3 {modulos[op]}")
    elif op == "0":
        print(f"{amarillo}Saliendo...{reset}")
        sys.exit()
    else:
        print(f"{rojo}❌ Opción inválida.{reset}")
        sleep(1)

if __name__ == "__main__":
    mensaje_educativo()
    abrir_youtube()
    while True:
        mostrar_menu()
        opcion = input(f"{azul}Selecciona una opción:{reset} ")
        ejecutar_opcion(opcion)
