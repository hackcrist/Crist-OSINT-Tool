#!/usr/bin/env python3
import os
import sys
from time import sleep
from pathlib import Path

# Colores
verde = "\033[92m"
azul = "\033[94m"
amarillo = "\033[93m"
rojo = "\033[91m"
reset = "\033[0m"

# Ruta base del proyecto (detecta automáticamente)
BASE_DIR = Path(__file__).resolve().parent
MODULES_DIR = BASE_DIR / "modules"
UTILS_DIR = BASE_DIR / "utils"

def mensaje_educativo():
    print(f"{amarillo}⚠️ Herramienta creada con fines educativos. El mal uso es responsabilidad del usuario.{reset}")
    sleep(1)

def abrir_youtube():
    os.system("xdg-open https://www.youtube.com/@TechConWin >/dev/null 2>&1 &")

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

def ejecutar_opcion(op):
    modulos = {
        "1": MODULES_DIR / "redes.py",
        "2": MODULES_DIR / "leaks.py",
        "3": MODULES_DIR / "phones.py",
        "4": MODULES_DIR / "exif.py",
        "5": MODULES_DIR / "geoip.py",
        "6": UTILS_DIR / "save_report.py",
        "7": MODULES_DIR / "blacklist.py",
        "8": MODULES_DIR / "headers.py",
        "9": MODULES_DIR / "wayback.py",
        "10": MODULES_DIR / "whois_lookup.py",
        "11": MODULES_DIR / "linkcheck.py",
        "12": UTILS_DIR / "save_report.py"
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
